import json, os

class Book:
    def load(self, book_name):
        book_file = open(book_name, "r")
        self.__book = json.load(book_file)
        self.book_name = book_name

        self.__exe_date = self.__book["exe_date"]
        self.__incomes = self.__book["incomes"]
        self.__expenses = self.__book["expenses"]

        book_file.close()

    def save(self):
        book_file = open(self.book_name, "w")
        json.dump(self.__book, book_file)

        book_file.close()

    def delete(self):
        os.remove(self.book_name)

    def clear(self):
        self.book_name = None
        self.__book = {}

        self.__exe_date = None
        self.__incomes = {}
        self.__expenses = {}

    def add_item(self, item):
        kind = item.get("kind")
        name = item.get("name")
        category = item.get("category")
        budget = item.get("budget")
        
        
