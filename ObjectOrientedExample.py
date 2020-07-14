# this is from Using Python to Access Database, week 1, chapter 14
# Object Oriented 
# in this example, s, j are 2 objects or instances, there are two x's, two names,
# but they are independently stored in each of these objects. 
# Two PartyAnimals were constructed, 

class PartyAnimal:
	x=0
	name = ""
	def __init__(self,z):
		self.name = z
		print (self.name,"constructed")

	def party(self):
		self.x = self.x + 1
		print (self.name,"party count",self.x)

s = PartyAnimal('Sally')
s.party()

j = PartyAnimal("Jim")
j.party()
s.party()

