# (c) 2018 Manikandan

class Artwork:
    def __init__(self, title, artist, description, current_bid=0):
        self.title = title
        self.artist = artist
        self.description = description
        self.current_bid = current_bid

    def place_bid(self, amount):
        if amount > self.current_bid:
            self.current_bid = amount

    def __str__(self):
        return f'Title: {self.title}\nArtist: {self.artist}\nDescription: {self.description}\nCurrent Bid: ${self.current_bid}'
