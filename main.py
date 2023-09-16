# (c) 2018 Manikandan
from artwork import Artwork
from user import User
from admin import Admin

# Initialize sample data
artworks = [Artwork("Sunset", "Artist1", "Beautiful sunset painting", 100),
            Artwork("Abstract", "Artist2", "Colorful abstract artwork", 200),
            Artwork("Portrait", "Artist3", "Realistic portrait painting", 150)]

users = [User("user1", "password1"),
         User("user2", "password2")]

admin = Admin("admin", "adminpassword")

def main():
    while True:
        print("Digital Art Gallery & Auction")
        print("1. Browse Art Gallery")
        print("2. Login")
        print("3. Admin Login")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Art Gallery:")
            for i, artwork in enumerate(artworks):
                print(f"{i + 1}. {artwork.title} by {artwork.artist} - Current Bid: ${artwork.current_bid}")

        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user = next((u for u in users if u.username == username and u.password == password), None)

            if user:
                while True:
                    print("User Menu:")
                    print("1. Browse Art Gallery")
                    print("2. Place Bid")
                    print("3. My Bids")
                    print("4. Logout")
                    user_choice = input("Enter your choice: ")

                    if user_choice == '1':
                        print("Art Gallery:")
                        for i, artwork in enumerate(artworks):
                            print(f"{i + 1}. {artwork.title} by {artwork.artist} - Current Bid: ${artwork.current_bid}")

                    elif user_choice == '2':
                        artwork_index = int(input("Enter the artwork number to bid on: ")) - 1
                        if 0 <= artwork_index < len(artworks):
                            amount = int(input("Enter your bid amount: "))
                            user.place_bid(artworks[artwork_index], amount)
                            print(f"Your bid of ${amount} on {artworks[artwork_index].title} has been placed.")

                    elif user_choice == '3':
                        print(user)

                    elif user_choice == '4':
                        break

                    else:
                        print("Invalid choice. Please try again.")

            else:
                print("Invalid username or password.")

        elif choice == '3':
            admin_username = input("Enter admin username: ")
            admin_password = input("Enter admin password: ")

            if admin_username == admin.username and admin_password == admin.password:
                while True:
                    print("Admin Dashboard:")
                    print("1. View Artworks")
                    print("2. Add Artwork")
                    print("3. Logout")
                    admin_choice = input("Enter your choice: ")

                    if admin_choice == '1':
                        print("Art Gallery:")
                        for i, artwork in enumerate(artworks):
                            print(f"{i + 1}. {artwork}")

                    elif admin_choice == '2':
                        title = input("Enter artwork title: ")
                        artist = input("Enter artist name: ")
                        description = input("Enter artwork description: ")
                        price = int(input("Enter starting bid price: "))
                        new_artwork = Artwork(title, artist, description, price)
                        artworks.append(new_artwork)
                        print(f"Artwork '{title}' by {artist} has been added to the gallery.")

                    elif admin_choice == '3':
                        break

                    else:
                        print("Invalid choice. Please try again.")

            else:
                print("Invalid admin credentials.")

        elif choice == '4':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
