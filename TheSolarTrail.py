#steel, water, copper, food, crew, uranium, thorium, filters, diamond, titanium
#include a time component for travel

print("Checkpoint1")
import random

class Item:
	def __init__(self,name,cat,price,info):
		self.name = name
		self.cat = cat
		self.price = price
		self.info = info

class City:
	def __init__(self,name,info,distance):
		self.name = name
		self.info = info
		self.distance = distance

class Player:
	def __init__(self,name):
		self.name = name
	cash = 5000
	
	_Water = 1000
	_Copper = 0
	_Helium = 0
	_Crew = 4
	_Fuel = 200

	def check_inv(self):
		print (" ")
		print ("I N V E N T O R Y :")
		print (" ")
		print ("Cash:    ", self.cash)
		print (" ")
		print ("Water:  ", self._Water)
		print ("Copper: ", self._Copper)
		print ("Helium:  ", self._Helium)
		print ("Crew:    ", self._Crew)
		print ("Fuel:     ", self._Fuel)
		print (" ")
		print ("----")
		print (" ")

class Map:
         cities = []
         inner = 1.000
         jovian = 1.000
         belter = 1.000

         def __init__(self,location,city1,city2,city3,city4,city5,city6,city7,city8,city9,city10,city11,city12):
            self.location = location
            self.cities.append(city1)
            self.cities.append(city2)
            self.cities.append(city3)
            self.cities.append(city4)
            self.cities.append(city5)
            self.cities.append(city6)
            self.cities.append(city7)
            self.cities.append(city8)
            self.cities.append(city9)
            self.cities.append(city10)
            self.cities.append(city11)
            self.cities.append(city12)

         def travel(self, city):
            self.location = city
            print (" ")
            print ("You Have arrived at ", self.location.name)
            print (" ")
            #set new rates
            if (self.location.name == 'Mercury' or self.location.name == 'Venus' or self.location.name == 'Earth' or self.location.name == 'Luna'):
               self.inner = round(random.uniform(0.1,1.5),3)
               self.belter = round(random.uniform(0.1,2.7),3)
               self.jovian = round(random.uniform(1.2,3.5),3)
            if (self.location.name == 'Eros' or self.location.name == 'Ceres'):
               self.inner = round(random.uniform(0.5,2.7),3)
               self.belter = round(random.uniform(0.1,1.5),3)
               self.jovian = round(random.uniform(0.5,3.0),3)
            if (self.location.name == 'Ganymede' or self.location.name == 'Io' or self.location.name == 'Titan' or self.location.name == 'Enceladus' or self.location.name == 'Tycho Station'):
               self.inner = round(random.uniform(1.5,3.5),3)
               self.belter = round(random.uniform(0.5,2.7),3)
               self.jovian = round(random.uniform(0.1,1.0),3)
               
               
               
           
         def check_demand(self):
            print (" ")
            print ("D E M A N D :")
            print ("Current Location market multiplier: ", self.location.name)
            print (" ")
            print ("Ship items: ",self.inner,"X")
            print ("Asteroid Belt Resources: ",self.belter,"X")
            print ("Jovian System Resources: ",self.jovian,"X")
            print (" ")
            print ("Water:  $",round(float(Water.price)*float(self.belter),1))
            print ("Copper: $",round(float(Copper.price)*float(self.belter),1))
            print ("Helium: $",round(float(Helium.price)*float(self.jovian),1))
            print ("Crew:   $",round(float(Crew.price)*float(self.inner),1))
            print ("Fuel:   $",round(float(Fuel.price)*float(self.inner),1))
            print ("----")
            print (" ")

         def check_location(self):
            print (" ")
            print ("L O C A T I O N :")
            print ("Current Location: ", self.location.name)
            print (" ")
            print ("Location Information: ")
            print (self.location.info)
            print (self.location.name, " is ", self.location.distance, "AU away from the sun.")
            print (" ")
            print ("----")
            print (" ")

         def check_map(self):
            print (" ")
            print ("M A P :")
            print (" ")
            print ("Current Location: ", self.location.name)
            print (" ")
            print (self.cities[0].name," is ", abs(round((self.location.distance-self.cities[0].distance),3)),"AU away.")
            print (self.cities[1].name," is ", abs(round((self.location.distance-self.cities[1].distance),3)),"AU away.")
            print (self.cities[2].name," is ", abs(round((self.location.distance-self.cities[2].distance),3)),"AU away.")
            print (self.cities[3].name," is ", abs(round((self.location.distance-self.cities[3].distance),3)),"AU away.")
            print (self.cities[4].name," is ", abs(round((self.location.distance-self.cities[4].distance),3)),"AU away.")
            print (self.cities[5].name," is ", abs(round((self.location.distance-self.cities[5].distance),3)),"AU away.")
            print (self.cities[6].name," is ", abs(round((self.location.distance-self.cities[6].distance),3)),"AU away.")
            print (self.cities[7].name," is ", abs(round((self.location.distance-self.cities[7].distance),3)),"AU away.")
            print (self.cities[8].name," is ", abs(round((self.location.distance-self.cities[8].distance),3)),"AU away.")
            print (self.cities[9].name," is ", abs(round((self.location.distance-self.cities[9].distance),3)),"AU away.")
            print (self.cities[10].name," is ", abs(round((self.location.distance-self.cities[10].distance),3)),"AU away.")
            print (self.cities[11].name," is ", abs(round((self.location.distance-self.cities[11].distance),3)),"AU away.")
            print (" ")
            print ("----")
            print (" ")

#trying to get fuel consumption working for ver3
def Travel():
   cost = round(random.uniform(0.1,20.0),3)
   currentloc = m1.location.name
   currentlocd = m1.location.distance
   print("Current location: ", currentloc)
   destination = input("Where to?: ")
   destination = destination.title()
   found = False
   for x in range(0,len(m1.cities)):
      if (destination == m1.cities[x].name):
         print ("Found ",m1.cities[x].name," on the map...")
         trip = round(abs(currentlocd-m1.cities[x].distance),3)
         tripfuel = round(trip*50,1)
         tripwater = round(trip*100,1)
         print (m1.cities[x].name, " is ", trip, "AU away from your current location.")
         print ("Traveling to ", m1.cities[x].name, " will use ", tripfuel, "fuel pellets and ", tripwater, "L of water.")
         if p1._Fuel >= tripfuel and p1._Water >= tripwater:
            found = True
            p1._Fuel -= tripfuel
            p1._Water -= tripwater
            city = m1.cities[x]
            print ("Working ")
            m1.travel(city)
         elif p1._Fuel < tripfuel or p1._Water < tripwater:
            print ("You don't have the resources to make the journey! Try again later...")
            print (" ")
         else:
            print("I can't find this place.")
            print(" ")

			

def Sell():
   found = False
   item = input("Sell what?: ")
   item = item.title()
   amt = input("Ok, how much do you want to sell?: ")
   if(amt.isdigit()==True):
          print ("Selling",amt,"",item,".")
          print (" ")
   else:
          print ("Please enter an integer for the amount.")
          print (" ")

   if (item == "Water"):
          found = True
          if(p1._Water >= int(amt)):
                  price = round((float(Water.price)*m1.belter)*float(amt),1)
                  p1._Water = p1._Water -int(amt)
                  p1.cash = p1.cash + (price)
                  print ("Sold",item,"for",price)
                  print (" ")
          else:
                  print ("You don't have enough of that!")
                  print (" ")

   elif (item == "Helium"):
          found = True
          if(p1._Helium >= int(amt)):
                  price = round((float(Helium.price)*m1.jovian)*float(amt),1)
                  p1._Helium = p1._Helium -int(amt)
                  p1.cash = p1.cash + (price)
                  print ("Sold",item,"for",price)
          else:
                  print ("You don't have enough of that!")
                  print (" ")

   elif (item == "Copper"):
          found = True
          if(p1._Copper >= int(amt)):
                  price = round((float(Copper.price)*m1.belter)*float(amt),1)
                  p1._Copper = p1._Copper -int(amt)
                  p1.cash = p1.cash + (price)
                  print ("Sold",item,"for",price)
          else:
                  print ("You don't have enough of that!")
                  print (" ")

   elif (item == "Crew"):
          found = True
          if(p1._Crew >= int(amt)):
                  price = round((float(Crew.price)*m1.inner)*float(amt),1)
                  p1._Crew = p1._Crew -int(amt)
                  p1.cash = p1.cash + (price)
                  print ("Sold",item,"for",price)
          else:
                  print ("You don't have enough of that!")
                  print (" ")

   elif (item == "Fuel"):
          found = True
          if(p1._Fuel >= int(amt)):
                  price = round((float(Fuel.price)*m1.inner)*float(amt),1)
                  p1._Fuel = p1._Fuel -int(amt)
                  p1.cash = p1.cash + (price)
                  print ("Sold",item,"for",price)
          else:
                  print ("You don't have enough of that!")
                  print (" ")

   else:
          print ("I can't find this item.")


def Buy():
   found = False
   item = input("Buy what?: ")
   item = item.title()
   amt = input("Ok, how much do you want to buy?: ")
   if(amt.isdigit()==True):
          print ("Buying",float(amt),"",item,".")
          print (" ")
   else:
          print ("Please enter an integer for the amount.")
          print (" ")

   if (item == "Water"):
          found = True
          price = round((float(Water.price)*m1.belter)*float(amt),1)
          if(p1.cash >= price):
                  p1._Water = p1._Water +int(amt)
                  p1.cash = p1.cash - (price)
                  print ("Bought",item,"for",price)
                  print (" ")
          else:
                  print ("You don't have enough cash to buy that!")
                  print (" ")

   elif (item == "Crew"):
          found = True
          price = round((float(Crew.price)*m1.inner)*float(amt),1)
          if(p1.cash >= price):
                  p1._Crew = p1._Crew +int(amt)
                  p1.cash = p1.cash - (price)
                  print ("Bought",item,"for",price)
          else:
                  print ("You don't have enough cash to buy that!")
                  print (" ")

   elif (item == "Helium"):
          found = True
          price = round((float(Helium.price)*m1.jovian)*float(amt),1)
          if(p1.cash >= price):
                  p1._Helium = p1._Helium +int(amt)
                  p1.cash = p1.cash - (price)
                  print ("Bought",item,"for",price)
          else:
                  print ("You don't have enough cash to buy that!")
                  print (" ")

   elif (item == "Copper"):
          found = True
          price = round((float(Copper.price)*m1.belter)*float(amt),1)
          if(p1.cash >= price):
                  p1._Copper = p1._Copper +int(amt)
                  p1.cash = p1.cash - (price)
                  print ("Bought",item,"for",price)
          else:
                  print ("You don't have enough cash to buy that!")
                  print (" ")

   elif (item == "Fuel"):
          found = True
          price = round((float(Fuel.price)*m1.inner)*float(amt),1)
          if(p1.cash >= price):
                  p1._Fuel = p1._Fuel +int(amt)
                  p1.cash = p1.cash - (price)
                  print ("Bought",item,"for",price)
          else:
                  print ("You don't have enough cash to buy that!")
                  print (" ")

   else:
          print ("I can't find this item.")
	
def Help():
	print("BASIC COMMANDS: \ntravel - Go to a new place (costs some money)\nmap - Check your map\nlocation - Info about your current location\ninv - Check your stock\ndemand - Check the price of resources in your current location\nbuy - Buy Items\nsell - Sell Items ")

def GameLoop():
	running = True
	waiting = True
	cmd = ""
	while (running == True):
		cmd = input("Cmd: ")
		cmd = cmd.lower()
		if (cmd == "map" or cmd == "check map"):
			m1.check_map()
		elif (cmd == "location"):
			m1.check_location()
		elif(cmd == "inv" or cmd == "inventory" or cmd == "resources" or cmd == "stock"):
			p1.check_inv()
		elif(cmd == "go" or cmd == "travel"):
			Travel()
		elif(cmd == "demand"):
			m1.check_demand();
		elif(cmd == "sell"):
			Sell()
		elif(cmd == "buy"):
			Buy()
		#utility
		elif(cmd == "help"):
			Help()
		elif(cmd == "exit" or cmd == "quit"):
			running = False	
		elif (cmd == "clear"):
			for x in range(0, 300):
				print ("\n")	
		#unknown command
		else:
			print ("Unknown Command!")
			print (" ")

		#print (i)
#ITEMS
Water = Item('Water','belter','1','Required substance for sustaining life and controlling reactor heat. Your ship requires 100L water 1AU traveled.')
Copper = Item('Copper','belter','5','Resource always in demand, but cheap and heavy.')
Helium = Item('Helium','jovian','1000','Very expensive resource that is collected in the Jovian System.')
Crew = Item("Crew Members",'inner','50000','Your ship requires 4 crew members to operate well, but can accommodate 12. Crew members consume food and water, but they keep losses to a minimum.') 
Fuel = Item('Fuel','inner','50','Your ship requires 50 fuel pellets per 1AU travelled.')

#CITY
Mercury = City("Mercury", "Inner Planets", 0.34)
Venus = City("Venus", "Inner Planets", 0.61)
Earth = City("Earth", "Inner Planets", 1.0)
Luna = City("Luna", "Inner Planets", 1.002)
Mars = City("Mars", "Inner Planets", 1.46)
Eros = City("Eros", "The Belt", 3.38)
Ceres = City("Ceres", "The Belt", 4.82)
Ganymede = City("Ganymede", "Jovian System", 5.1)
Io = City("Io", "Jovian System", 5.2)
Titan = City("Titan", "Jovian System", 9.5)
Enceladus = City("Enceladus", "Jovian System", 10.1)
Tycho = City("Tycho", "Jovian System", 18.82)


p1 = Player('Kris')
m1 = Map(Earth, Mercury, Venus, Earth, Luna, Mars, Eros, Ceres, Ganymede, Io, Titan, Enceladus, Tycho)
#m1.distance = [1.0, 0.34, 0.61, 0.612, 1.0, 1.14, 1.46, 3.38, 4.82, 5.1, 5.2, 9.5, 10.1, 18.82]



print("W E L C O M E   T O   T H E   S O L A R   T R A I L")
print("A solar sytem trading game")
Help()
print(" ")
print(" ")
GameLoop()
