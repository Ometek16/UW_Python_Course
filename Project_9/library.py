import json
from random import randint

class Item:
	def __init__(self, title, creator, year):
		self.title = title
		self.creator = creator
		self.year = year
		
	def display_info(self, tabs=0): pass
 
	def __eq__(self, other):
		return self.__dict__ == other.__dict__

class Book(Item):
	def __init__(self, title, creator, year, genre, isbn):
		super().__init__(title, creator, year)
		self.genre = genre
		self.isbn = isbn

	def __str__(self):
		return f'"{self.title}" by {self.creator}'
	
	def __repr__(self):
		return f"Title: {self.title}\nCreator: {self.creator}\nYear: {self.year}\nGenre: {self.genre}\nISBN: {self.isbn}"

	def display_info(self, tabs=0):
		indent = tabs * '\t'
		print(f"{indent}Title: {self.title}")
		print(f"{indent}Creator: {self.creator}")
		print(f"{indent}Year: {self.year}")
		print(f"{indent}Genre: {self.genre}")
		print(f"{indent}ISBN: {self.isbn}")

class Movie(Item):
	def __init__(self, title, creator, year, genre, duration):
		super().__init__(title, creator, year)
		self.genre = genre
		self.duration = duration
	
	def __str__(self):
		return f'"{self.title}" by {self.creator}'

	def __repr__(self):
		return f"Title: {self.title}\nCreator: {self.creator}\nYear: {self.year}\nGenre: {self.genre}\nDuration: {self.duration}"

	def display_info(self, tabs=0):
		indent = tabs * '\t'
		print(f"{indent}Title: {self.title}")
		print(f"{indent}Creator: {self.creator}")
		print(f"{indent}Year: {self.year}")
		print(f"{indent}Genre: {self.genre}")
		print(f"{indent}Duration: {self.duration}")
  	
class Library:
	def __init__(self):
		self.products = {"books" : [], "movies" : [], "items" : []}
  
	def __iter__(self):
		return iter([item for group in self.products for item in self.products[group]])

	def add_item(self, item):
		if (isinstance(item, Book)):
			self.products["books"].append(item)
		elif (isinstance(item, Movie)):
			self.products["movies"].append(item)
		elif (isinstance(item, Item)):
			self.products["items"].append(item)
		else:
			print(f"[ERROR] Could not add item {item} to library {self}")
   
	def display_items(self):
		empty = True
		for group in self.products:
			if (len(self.products[group])):
				print("===== ===== =====", group.capitalize(), "===== ===== =====")	
				for i, item in enumerate(self.products[group]):
					if (i != 0):
						print()
					print(i + 1, end="")
					item.display_info(1)
					empty = False
		if not empty:
			print("===== ===== ===== ===== ===== ===== =====")

    
	def save_to_file(self, filename):
		with open(filename, 'w') as file:
			library = {}
			for group in self.products:
				library[group] = [item.__dict__ for item in self.products[group]]
			
			json.dump(library, file, indent=4)
   
	def load_from_file(self, filename):
		with open(filename, 'r') as file:
			library = json.load(file)
			for group in self.products:
				for params in library[group.lower()]:
					class_name = globals().get(group.capitalize()[:-1])
					self.add_item(class_name(**params))
    
	def recommend(self, ideal_item):
		by_genre = list()
		by_creator = list(filter(lambda item: item.creator == ideal_item.creator and item != ideal_item, self))
		by_year = list(filter(lambda item: abs(ideal_item.year - item.year) < 3 and item != ideal_item, self))
		by_duration = list()
		try:
			genre = ideal_item.genre
			for group in self.products:
				for item in self.products[group]:
					try:
						if (genre == item.genre and item != ideal_item):
							by_genre.append(item)
					except: pass
		except: pass
		try:
			duration = ideal_item.duration
			for group in self.products:
				for item in self.products[group]:
					try:
						if (abs(duration - item.duration) < 10 and item != ideal_item):
							by_duration.append(item)
					except: pass
		except: pass
  
		all_items = by_genre + by_creator + by_year + by_duration

		best_fit = None	
		best_score = 0
		for item in all_items:
			score = 0
			if item in by_genre:
				score += 3
			if item in by_creator:
				score += 2
			if item in by_year:
				score += 1
			if item in by_duration:
				score += 1
			if score > best_score:
				best_score = score
				best_fit = item
    
		if (not best_fit):
			all_items = [item for group in self.products for item in self.products[group]]
			if (len(all_items)):
				best_fit = all_items[randint(0, len(all_items) - 1)]
		return best_fit
  
	
library = Library()

book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic", "978-3-16-148410-0")
movie1 = Movie("Inception", "Christopher Nolan", 2010, "Sci-Fi", 148)
movie2 = Movie("Interstellar", "Christopher Nolan", 2014, "Sci-Fi", 169)
movie3 = Movie("Shutter Island", "Martin Scorsese", 2010, "Mystery", 138)

library.add_item(book)
library.add_item(movie1)
library.add_item(movie2)
library.add_item(movie3)

library.save_to_file("my_library")

library2 = Library()
library2.load_from_file("my_library")

library2.display_items()

best_movie = Movie("Inception", "Christopher Nolan", 2010, "Sci-Fi", 148)
best_book = Book("The Hobbit, or There and Back Again", "J. R. R. Tolkien", 1937, "Fantasy", "978-0-00-752550-8")

print(library2.recommend(best_movie))
print(library2.recommend(best_book))
