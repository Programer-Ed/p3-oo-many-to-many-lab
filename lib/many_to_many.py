from datetime import datetime
class Author:
    def __init__(self,name) -> None:
        self.name = name
        self._contracts = []  # Initialize the list to store contracts

    def add_contract(self, contract):
        if not isinstance(contract, Contract):
            raise TypeError("Expected a Contract instance")
        if contract not in self._contracts:
            self._contracts.append(contract)

    def contracts(self):
        """Return a list of contracts related to this author."""
        return self._contracts

    def books(self):
        """Return a list of books related to this author through contracts."""
        return list(set(contract.book for contract in self._contracts))

    def sign_contract(self, book, date, royalties):
        """Create and return a new Contract between this author and the specified book."""
        if not isinstance(book, Book):
            raise TypeError("Expected a Book instance")
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        if not isinstance(royalties, int) or royalties < 0:
            raise ValueError("Royalties must be a non-negative integer")
        
        contract = Contract(self, book, date, royalties)
        self.add_contract(contract)
        return contract

    def total_royalties(self):
        """Return the total amount of royalties earned from all contracts."""
        return sum(contract.royalties for contract in self._contracts)
        pass
    pass


class Book:
    def __init__(self, title):
        self.title = title
        self._contracts = []  # Initialize the list to store contracts
        self._authors = []  # Initialize the list to store authors

    def add_contract(self, contract):
        if not isinstance(contract, Contract):
            raise TypeError("Expected a Contract instance")
        if contract not in self._contracts:
            self._contracts.append(contract)
        if contract.author not in self._authors:
            self._authors.append(contract.author)

    def contracts(self):
        return self._contracts

    def authors(self):
        
        return self._authors
    pass


class Contract:
     all = []
     def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of the Author class")
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of the Book class")
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        if not isinstance(royalties, int) or royalties < 0:
            raise ValueError("royalties must be a non-negative integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        # Add contract to the class-level list
        Contract.all.append(self)
        # Add contract to author's and book's list of contracts
        author.add_contract(self)
        book.add_contract(self)

     @classmethod
     def contracts_by_date(cls, date):
        """Return all contracts that have the specified date."""
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        
        # Convert the input date to datetime object for comparison
        input_date = datetime.strptime(date, '%m/%d/%Y')
        
        # Filter and sort contracts by the specified date
        return sorted(
            (contract for contract in cls.all if datetime.strptime(contract.date, '%m/%d/%Y') == input_date),
            key=lambda c: c.date
        )