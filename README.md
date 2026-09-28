
# 🎬 Movie Ticket Booking System

## 📌 Project Overview
The Movie Ticket Booking System is a Python-based console application that allows users to book movie tickets, view booking details, and cancel bookings.

The system displays available movies, ticket prices, and remaining seats. It also generates a unique booking ID and stores booking information in a JSON file.

This project is developed as a beginner-friendly Python project to demonstrate programming concepts such as functions, dictionaries, loops, file handling, exception handling, and JSON.

## ✨ Features

- **Show Movies:** Displays available movies, ticket prices, and remaining seats.
- **Book Tickets:** Allows users to select a movie and book tickets.
- **View Booking:** Retrieves booking details using a booking ID.
- **Cancel Booking:** Cancels an existing booking and returns the seats.
- **Automatic Price Calculation:** Calculates the total ticket price.
- **Booking ID Generation:** Generates a random booking ID for each booking.
- **Data Storage:** Saves booking information in a JSON file.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| JSON | Stores booking details |
| os module | Checks whether the booking file exists |
| random module | Generates booking IDs |

## 🎥 Available Movies

| Movie | Ticket Price | Initial Seats |
|---|---:|---:|
| Avengers | ₹200 | 50 |
| Spider-Man | ₹180 | 40 |
| Interstellar | ₹150 | 30 |

## ⚙️ Installation and Setup

### 1. Install Python

Download Python from the official website:

https://www.python.org/downloads/

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/movie-ticket-booking.git
```

### 3. Navigate to the Project Folder

```bash
cd movie-ticket-booking
```

### 4. Run the Program

If your Python file is named `main.py`, run:

```bash
python3 main.py
```

No external libraries are required because the project uses Python's built-in modules.

## 🚀 How to Use

1. Run the Python program.
2. Select an option from the main menu.
3. Choose a movie and enter the number of tickets.
4. Enter your name to confirm the booking.
5. Note the generated booking ID.
6. Use the booking ID to view or cancel your booking.
7. Select Exit to close the program.

## 📋 Main Menu

```text
===== MOVIE TICKET BOOKING =====
1. Show Movies
2. Book Tickets
3. View Booking
4. Cancel Booking
5. Exit
```

## 📂 Project Structure

```text
Movie-Ticket-Booking/
│
├── main.py
├── bookings.json
└── README.md
```

**Note:** The `bookings.json` file is created automatically when booking data is saved.

## 🧠 Python Concepts Used

- Variables and data types
- Dictionaries and nested dictionaries
- Functions and function arguments
- Loops and conditional statements
- File handling
- JSON data serialization
- Exception handling using try-except
- Random number generation

## 🔮 Future Improvements

- Add user login and registration.
- Implement permanent seat availability storage.
- Add specific seat selection.
- Integrate online payment functionality.
- Develop a graphical user interface (GUI).

## 👨‍💻 Author

**Animesh kumar Singh**

## 📄 License

This project is developed for educational purposes.
