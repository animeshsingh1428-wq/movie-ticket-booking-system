
import json
import os
import random

FILE = "bookings.json"

# Movie details
movies = {
    1: {"name": "Avengers", "price": 200, "seats": 50},
    2: {"name": "Spider-Man", "price": 180, "seats": 40},
    3: {"name": "Interstellar", "price": 150, "seats": 30}
}


# Load bookings
def load_bookings():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}


# Save bookings
def save_bookings(bookings):
    with open(FILE, "w") as f:
        json.dump(bookings, f, indent=4)


# Display movies
def show_movies():
    print("\n----- AVAILABLE MOVIES -----")

    for key, movie in movies.items():
        print(key, movie["name"],
              "| Price: Rs.", movie["price"],
              "| Seats:", movie["seats"])


# Book tickets
def book_ticket(bookings):
    show_movies()

    try:
        choice = int(input("Select movie number: "))

        if choice not in movies:
            print("Invalid movie selection!")
            return

        movie = movies[choice]

        seats = int(input("Enter number of tickets: "))

        if seats <= 0:
            print("Enter a valid number of tickets!")
            return

        if seats > movie["seats"]:
            print("Not enough seats available!")
            return

        name = input("Enter your name: ")

        total = seats * movie["price"]

        booking_id = str(random.randint(1000, 9999))

        booking = {
            "name": name,
            "movie": movie["name"],
            "tickets": seats,
            "total": total
        }

        bookings[booking_id] = booking

        movie["seats"] -= seats

        save_bookings(bookings)

        print("\n----- BOOKING CONFIRMED -----")
        print("Booking ID:", booking_id)
        print("Name:", name)
        print("Movie:", movie["name"])
        print("Tickets:", seats)
        print("Total amount: Rs.", total)

    except ValueError:
        print("Please enter a valid number!")


# View booking
def view_booking(bookings):
    booking_id = input("Enter booking ID: ")

    if booking_id in bookings:
        b = bookings[booking_id]

        print("\n----- BOOKING DETAILS -----")
        print("Name:", b["name"])
        print("Movie:", b["movie"])
        print("Tickets:", b["tickets"])
        print("Total: Rs.", b["total"])
    else:
        print("Booking not found!")


# Cancel booking
def cancel_booking(bookings):
    booking_id = input("Enter booking ID: ")

    if booking_id in bookings:
        b = bookings[booking_id]

        # Return seats to the movie
        for movie in movies.values():
            if movie["name"] == b["movie"]:
                movie["seats"] += b["tickets"]
                break

        del bookings[booking_id]
        save_bookings(bookings)

        print("Booking cancelled successfully!")
    else:
        print("Booking not found!")


# Main program
bookings = load_bookings()

while True:
    print("\n===== MOVIE TICKET BOOKING =====")
    print("1. Show Movies")
    print("2. Book Tickets")
    print("3. View Booking")
    print("4. Cancel Booking")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_movies()

    elif choice == "2":
        book_ticket(bookings)

    elif choice == "3":
        view_booking(bookings)

    elif choice == "4":
        cancel_booking(bookings)

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")