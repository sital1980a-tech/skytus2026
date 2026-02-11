class Flight:
    def __init__(self, flight_number, total_seats):
        self.flight_number = flight_number
        self.total_seats = total_seats
        self.booked_seats = 0

    def book_seat(self):
        if self.booked_seats < self.total_seats:
            self.booked_seats += 1
            print("Seat booked successfully!")
            print("Remaining seats:", self.total_seats - self.booked_seats)
        else:
            print("Sorry, no seats available.")

    def display_status(self):
        print("Flight Number:", self.flight_number)
        print("Total Seats:", self.total_seats)
        print("Booked Seats:", self.booked_seats)
        print("Available Seats:", self.total_seats - self.booked_seats)


flight1 = Flight("AI101", 3)

flight1.display_status()
flight1.book_seat()
flight1.book_seat()
flight1.book_seat()
flight1.book_seat()  
flight1.display_status()
