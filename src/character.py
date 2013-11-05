import random
import gzip

random.seed()

class Person:
	def __init__(self):
		self.sex = random.choice(['Male', 'Female'])
		
		if(self.sex == 'Male'):
			with gzip.open('./corpus/dist.male.first.gz', 'r') as f:
				self.first_name = random.choice(f.readlines()).split()[0].title()
		
		else:
			with gzip.open('./corpus/dist.female.first.gz', 'r') as f:
				self.first_name = random.choice(f.readlines()).split()[0].title()
		
		with gzip.open('./corpus/dist.all.last.gz', 'r') as f:
			self.last_name = random.choice(f.readlines()).split()[0].title()
		
		with gzip.open('./corpus/jobs.txt.gz', 'r') as f:
			self.occupation = random.choice(f.readlines()).strip()

		with gzip.open('./corpus/us_cities.txt.gz', 'r') as f:
			self.location = random.choice(f.readlines()).strip()

	def __str__(self):
		return "Name: {0} {1}\nSex: {2}\nOccupation: {3}\nLocation: {4}".format(
			self.first_name, self.last_name, self.sex, self.occupation,
			self.location
		)

print Person()