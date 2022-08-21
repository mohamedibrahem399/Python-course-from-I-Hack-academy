import random
class human():
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def talking(self,talk):
		self.talk=talk
	def walking(self,walk):
		self.walk=walk
	def eat(self,eat):
		self.eat=eat
		

human1=human('mohamed',25)
human1.talk='hey i can talk'
human1.walk='i can walk also'
print(f'hi i am {human1.name} and my age is {human1.age}')
print (f"{human1.talk} and {human1.walk} ")
