
# Movie Ticket Booking System

# Movie details
movies = {
    1: {"name": "Avengers", "price": 200, "seats": 50},
    2: {"name": "Spider-Man", "price": 180, "seats": 40},
    3: {"name": "Interstellar", "price": 150, "seats": 30}
}

# Store bookings during the current session
bookings = {}
booking_id = 1001


# Display available movies
def show_movies():
    print("\n----- AVAILABLE MOVIES -----")

    for key, movie in movies.items():
        print(key, ".", movie["name"],
              "| Price: Rs.", movie["price"],
              "| Seats:", movie["seats"])


# Book tickets
def book_ticket():
    global booking_id

    show_movies()

    try:
        choice = int(input("\nSelect movie number: "))

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

        name = input("Enter your name: ").strip()

        if name == "":
            print("Name cannot be empty!")
            return

        total = seats * movie["price"]

        # Generate booking ID
        current_id = str(booking_id)
        booking_id += 1

        # Store booking
        booking = {
            "name": name,
            "movie": movie["name"],
            "tickets": seats,
            "total": total
        }

        bookings[current_id] = booking

        # Update available seats
        movie["seats"] -= seats

        print("\n----- BOOKING CONFIRMED -----")
        print("Booking ID:", current_id)
        print("Name:", name)
        print("Movie:", movie["name"])
        print("Tickets:", seats)
        print("Total amount: Rs.", total)

    except ValueError:
        print("Please enter a valid number!")


# View booking
def view_booking():
    booking_id = input("\nEnter booking ID: ")

    if booking_id in bookings:
        b = bookings[booking_id]

        print("\n----- BOOKING DETAILS -----")
        print("Booking ID:", booking_id)
        print("Name:", b["name"])
        print("Movie:", b["movie"])
        print("Tickets:", b["tickets"])
        print("Total amount: Rs.", b["total"])

    else:
        print("Booking not found!")


# Cancel booking
def cancel_booking():
    booking_id = input("\nEnter booking ID: ")

    if booking_id in bookings:
        b = bookings[booking_id]

        # Return seats to the movie
        for movie in movies.values():
            if movie["name"] == b["movie"]:
                movie["seats"] += b["tickets"]
                break

        del bookings[booking_id]

        print("Booking cancelled successfully!")

    else:
        print("Booking not found!")


# Main program
while True:
    print("\n===== MOVIE TICKET BOOKING =====")
    print("1. Show Movies")
    print("2. Book Tickets")
    print("3. View Booking")
    print("4. Cancel Booking")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        show_movies()

    elif choice == "2":
        book_ticket()

    elif choice == "3":
        view_booking()

    elif choice == "4":
        cancel_booking()

    elif choice == "5":
        print("\nThank you for using Movie Ticket Booking System!")
        print("All session bookings have been cleared.")
        break

    else:
        print("Invalid choice! Please try again.")
