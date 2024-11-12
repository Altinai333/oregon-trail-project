class BookStore():
	def __init__(self):
		self.Bnum = 0
		self._Books = {} 
		self._UIn = "n"
		self._Name = "n"
		self._Author = "n"
		self._Price = float(0)
		self._discount = 0
		self._cash = float(1000)
		self.fileload = "n"

	def add(self):
		self._Name = input("enter the name of the book you would like to add: \n").upper()
		try:
			str(self._Name)
			self._Author = input("enter the Author of the book you have just added: \n").upper()
			if self._Author:
				self._Price = float(input("Enter the listing price of the book:  \n"))
				if self._Price > 0 and self._Price <= self._cash:
					self._Books[self._Name] = {'Author': self._Author, 'Price': self._Price}
					self._cash = self._cash - (self._Price*.9)
					print (self._Books)
					print("the remaining store balance is:", "${:,.2f}".format(self._cash))
		except:
			print("Please enter a book title")
			
	def sell(self):
		self._Name = input("enter the name of the book you would like to sell: \n").upper()
		try: 
			str(self._Name)
			if self._Name in self._Books:
				self._cash = self._cash + self._Books[self._Name]['Price'] 
				self._Books.pop(self._Name)
				print("the new store balance is:", "${:,.2f}".format(self._cash))
		except:
			print("Please enter a book title")

	def reduceA(self):
		for x in self._Books:
			self._Books[x]['Price'] = (self._Books[x]['Price']) * .98
			print("the new cost of", self._Books[x]['Author'] + "'s", x, "is:", "${:,.2f}".format(self._Books[x]['Price']))

	def increaseA(self):
		for x in self._Books:
			self._Books[x]['Price'] = (self._Books[x]['Price']) * 1.02
			print("the new cost of", self._Books[x]['Author'] + "'s", x, "is:", "${:,.2f}".format(self._Books[x]['Price']))

	def showbook(self):
		for x, y in self._Books.items():
			print("\nBook title: "+ x +"\nAuthor: "+ self._Books[x]['Author'])
			print("Buying Price:", "${:,.2f}".format(self._Books[x]['Price']*.9))
			print("Selling Price:", "${:,.2f}".format(self._Books[x]['Price']))
			print("Revenue from sale:",  "${:,.2f}".format(self._Books[x]['Price']*.1))
		print("The Stores balance is:", "${:,.2f}".format(self._cash))

	def printout(self):
		self.Bnum = 0
		self.fileload = input("enter the file name you would like to print the inventory to: \n")
		Writeout = open(self.fileload, "w")
		for x, y in self._Books.items():
			self.Bnum = self.Bnum + 1
			Writeout.write(f'/* {self.Bnum} */\n')
			Writeout.write(x+"\n")
			Writeout.write(self._Books[x]['Author']+"\n")
			Writeout.write(str(self._Books[x]['Price'])+"\n")
		Writeout.write("The Stores balance is: " + "${:,.2f}".format(self._cash)+"\n\n")
		print("The inventory has been successfully saved to: " + self.fileload)

	def loadin(self):
		self.fileload = input("enter the name of the file you would like to load the inventory from: \n")
		infile = open(self.fileload, "r")
		endcheck = infile.read(3)
		while endcheck != "the":
			line = infile.readline()
			line = infile.readline()
			self._Name = line.strip()
			line = infile.readline()
			self._Author = line.strip()
			line = infile.readline()
			self._Price = line.strip()
			self._Price = float(self._Price)
			self._Books[self._Name] = {'Author': self._Author, 'Price': self._Price}
			endcheck = infile.read(3)
		self._cash = line.lstrip("Storebalnci: $")
		infile.close

	def qui(self, foop):
		self._foop = False
		return self._foop

