
movies = {
    1: {"name": "Avengers", "price": 200, "seats": 50},
    2: {"name": "Spider-Man", "price": 180, "seats": 40},
    3: {"name": "Interstellar", "price": 150, "seats": 30}
}

bookings = {}
bid = 1001


def show_movies():
    print("\nAvailable Movies")

    for i in movies:
        print(i, movies[i]["name"],
              "Price:", movies[i]["price"],
              "Seats:", movies[i]["seats"])


def book_ticket():
    global bid

    show_movies()

    try:
        n = int(input("Select movie number: "))

        if n not in movies:
            print("Wrong choice!")
            return

        seats = int(input("Enter tickets: "))

        if seats <= 0:
            print("Invalid number of tickets!")
            return

        if seats > movies[n]["seats"]:
            print("Seats not available!")
            return

        name = input("Enter your name: ")

        if name == "":
            print("Enter your name!")
            return

        total = seats * movies[n]["price"]

        bookings[bid] = {
            "name": name,
            "movie": movies[n]["name"],
            "tickets": seats,
            "total": total
        }

        movies[n]["seats"] -= seats

        print("\nTicket booked!")
        print("Booking ID:", bid)
        print("Name:", name)
        print("Movie:", movies[n]["name"])
        print("Tickets:", seats)
        print("Amount: Rs.", total)

        bid += 1

    except ValueError:
        print("Enter a valid number!")


def view_booking():
    try:
        n = int(input("Enter booking ID: "))

        if n in bookings:
            b = bookings[n]

            print("\nBooking Details")
            print("Name:", b["name"])
            print("Movie:", b["movie"])
            print("Tickets:", b["tickets"])
            print("Amount:", b["total"])

        else:
            print("Booking not found!")

    except ValueError:
        print("Invalid booking ID!")


def cancel_booking():
    try:
        n = int(input("Enter booking ID: "))

        if n in bookings:
            b = bookings[n]

            for i in movies:
                if movies[i]["name"] == b["movie"]:
                    movies[i]["seats"] += b["tickets"]

            del bookings[n]

            print("Booking cancelled!")

        else:
            print("Booking not found!")

    except ValueError:
        print("Invalid booking ID!")


while True:
    print("\nMovie Ticket Booking")
    print("1. Show Movies")
    print("2. Book Tickets")
    print("3. View Booking")
    print("4. Cancel Booking")
    print("5. Exit")

    ch = input("Enter your choice: ")

    if ch == "1":
        show_movies()

    elif ch == "2":
        book_ticket()

    elif ch == "3":
        view_booking()

    elif ch == "4":
        cancel_booking()

    elif ch == "5":
        print("Thank you!")
        break

    else:
        print("Wrong choice!")
