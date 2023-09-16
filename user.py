# (c) 2018 Manikandan

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bids = []

    def place_bid(self, artwork, amount):
        if amount > artwork.current_bid:
            artwork.place_bid(amount)
            self.bids.append((artwork, amount))

    def __str__(self):
        return f'Username: {self.username}\nBids:\n{"".join([f"{artwork.title} - ${amount}\n" for artwork, amount in self.bids])}'
