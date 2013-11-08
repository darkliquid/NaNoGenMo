require 'rubygems'
require 'open-uri'
require 'nokogiri'


class ProtagScraper
	def initialize(url_tmpl)
		@stories = []
		@url = url_tmpl
	end

	def get_stories(url = nil, page=0)
		doc = Nokogiri::HTML(open(url || @url))

		count = 0
		doc.css('.story-block .story h4 a').each do |link|
			count = count + 1
			@stories << { title: link.content, url: link['href'], desc: link['title'] }
		end

		unless count < 30
			page=page+1
			get_stories("#{@url}&page=#{page}", page)
		end
	end

	def to_s
		@stories.join("\n")
	end
end

scraper = ProtagScraper.new('http://www.protagonize.com/authors/works.aspx?browseBy=author&storyType=linear&handle=darkliquid&stories=true&published=true')
scraper.get_stories
puts scraper