class Album:

    # class constructor
    # __methodName__ is a magic method
    def __init__(self, id, title, genre, artist, price, year):
        self.id = id
        self.title = title
        self.genre = genre
        self.artist = artist
        self.price = price
        self.release_year = year
        self.songs = []

    def __str__(self):
        price = "${:,.2f}".format(self.price)
        return f"{self.id} - {self.artist} - {self.title} - {price}"
