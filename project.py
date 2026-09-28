print("================================")
print("     MOVIE TICKET BOOKING")
print("================================")

movies = {
    1: ["Avengers", 200, 50],
    2: ["Spider-Man", 180, 40],
    3: ["Interstellar", 150, 30]
}

bookings = []

while True:
    print("\n1. Show Movies")
    print("2. Book Ticket")
    print("3. View Bookings")
    print("4. Cancel Booking")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("\nAvailable Movies:")

        for key in movies:
            print(key, ".", movies[key][0],
                  "- Rs.", movies[key][1],
                  "- Seats:", movies[key][2])

    elif choice == "2":
        print("\nAvailable Movies:")

        for key in movies:
            print(key, ".", movies[key][0],
                  "- Rs.", movies[key][1])

        movie_no = int(input("\nEnter movie number: "))

        if movie_no in movies:
            name = movies[movie_no][0]
            price = movies[movie_no][1]
            seats = movies[movie_no][2]

            if seats > 0:
                customer = input("Enter your name: ")
                tickets = int(input("Number of tickets: "))

                if tickets > 0 and tickets <= seats:
                    total = tickets * price

                    movies[movie_no][2] -= tickets

                    bookings.append([
                        customer, name, tickets, total
                    ])

                    print("\nTicket booked successfully!")
                    print("Customer:", customer)
                    print("Movie:", name)
                    print("Tickets:", tickets)
                    print("Total amount: Rs.", total)

                else:
                    print("Sorry, seats are not available.")

            else:
                print("Housefull!")

        else:
            print("Invalid movie number.")

    elif choice == "3":
        if len(bookings) == 0:
            print("\nNo bookings found.")

        else:
            print("\nYour Bookings:")

            for i in range(len(bookings)):
                print("\nBooking", i + 1)
                print("Name:", bookings[i][0])
                print("Movie:", bookings[i][1])
                print("Tickets:", bookings[i][2])
                print("Amount: Rs.", bookings[i][3])

    elif choice == "4":
        if len(bookings) == 0:
            print("\nNo bookings to cancel.")

        else:
            for i in range(len(bookings)):
                print(i + 1, ".", bookings[i][0],
                      "-", bookings[i][1])

            cancel = int(input("\nEnter booking number to cancel: "))

            if cancel > 0 and cancel <= len(bookings):
                booking = bookings[cancel - 1]

                for key in movies:
                    if movies[key][0] == booking[1]:
                        movies[key][2] += booking[2]

                bookings.pop(cancel - 1)

                print("Booking cancelled successfully.")

            else:
                print("Invalid booking number.")

    elif choice == "5":
        print("\nThank you for using our system!")
        break

    else:
        print("Invalid choice. Please try again.")
