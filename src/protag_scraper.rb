require 'rubygems'
require 'open-uri'
require 'nokogiri'


class ProtagScraper
	def initialize(url_tmpl)
		@stories = []
		@url = url_tmpl
	end
	
	attr_reader :stories

	def get_stories(url = nil, page=0)
		doc = Nokogiri::HTML(open(url || @url))

		count = 0
		doc.css('#browseListing .story-block .story h4 a').each do |link|
			count = count + 1
			@stories << Story.new(link.inner_text.strip, link['href'], link['title'])
		end

		unless count < 30
			page=page+1
			get_stories("#{@url}&page=#{page}", page)
		end
		return @stories
	end

	def to_s
		@stories.join("\n\n")
	end
end

class Story
    def initialize(title, url, description)
        @title = title
        @url = "http://www.protagonize.com#{url}"
        @description = description
        @pages = []
    end
    
    attr_reader :pages, :title, :description
    
    def get_pages(url = nil)
        doc = Nokogiri::HTML(open(url || @url))

        next_page = nil
        content = (doc.css('#primaryContent #pageBody')[0].children.map do |c| 
            out = nil
            if c.children.empty?
                out = c.inner_text.strip
            else
                out = c.children.map do |n| 
                    n.inner_text.strip
                end
            end
            out
        end || []).flatten.join("\n").strip
		@pages << Page.new(
            doc.css('#primaryContent article header h1 span')[0].inner_text.strip,
            url,
            content
        )
        next_page_node = doc.css('#primaryContent #workPages a.page')[0]
        if next_page_node && !next_page_node['href'].match(/(\/edit$)|\#/)
            next_page = next_page_node['href']
        end

		if next_page
			get_pages("http://www.protagonize.com#{next_page}")
		end
		return @pages
    end
    
    def to_s
        out = "Story: #{@title}\n"
        @pages.each do |p|
            out += "\t#{p}\n"
        end
        out
    end
end

class Page
    def initialize(title, url, content)
        @title = title
        @url = "http://www.protagonize.com#{url}"
        @content = content || ""
    end
    
    attr_reader :title, :content
    
    def to_s
        "Page: #{@title} (#{@content.split(' ').size} words)"
    end
end

scraper = ProtagScraper.new('http://www.protagonize.com/authors/works.aspx?browseBy=author&storyType=linear&handle=darkliquid&stories=true&published=true')
scraper.get_stories.each { |story| story.get_pages }
puts scraper

scraper.stories.each do |s|
    File.open("./data/#{s.title.downcase.strip.gsub(' ', '-').gsub(/[^\w-]/, '')}.txt", 'w') do |file| 
        file.write("Title: #{s.title}")
        file.write("\n\n")
        file.write("Description: #{s.description}")
        file.write("\n\n\n")
        s.pages.each_with_index do |p, i|
            file.write("Chapter #{i+1}: #{p.title}")
            file.write("\n\n")
            file.write(p.content)
            file.write("\n\n")
        end
    end
end