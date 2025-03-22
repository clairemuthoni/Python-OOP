class Seat:
    def __init__(self, seat_number, is_booked=False):
        self.seat_number = seat_number
        self.is_booked = is_booked

    def __str__(self):
        return f"Seat Number {self.seat_number}"


class MovieTheater:
    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        # Initialize the seats list with Seat objects
        self.seats = [Seat(seat_number) for seat_number in range(1, total_seats + 1)]

    def display_available_seats(self):
        # Display all available seats (not booked)
        available_seats = [seat.seat_number for seat in self.seats if not seat.is_booked]
        print(f"Available seats: {available_seats}")

    def book_seat(self, seat_number):
        # Check if the seat exists
        for seat in self.seats:
            if seat.seat_number == seat_number:
                if not seat.is_booked:
                    seat.is_booked = True
                    print(f"Seat {seat_number} successfully booked.")
                    return
                else:
                    print(f"Seat {seat_number} is already booked.")
                    return
        # If the loop completes without finding the seat
        print(f"Seat {seat_number} does not exist.")

    def cancel_booking(self, seat_number):
        # Check if the seat exists
        for seat in self.seats:
            if seat.seat_number == seat_number:
                if seat.is_booked:
                    seat.is_booked = False
                    print(f"Booking for seat {seat_number} has been cancelled.")
                    return
                else:
                    print(f"Seat {seat_number} is not booked.")
                    return
        # If the loop completes without finding the seat
        print(f"Seat {seat_number} does not exist.")

    def get_booked_seats(self):
        # Get all booked seats
        booked_seats = [seat.seat_number for seat in self.seats if seat.is_booked]
        print(f"Booked seats: {booked_seats}")


# Example Usage
theater = MovieTheater("Grand Cinema", 5)

theater.display_available_seats()
# Output: Available seats: [1, 2, 3, 4, 5]

theater.book_seat(3)
# Output: Seat 3 successfully booked.

theater.book_seat(3)
# Output: Seat 3 is already booked.

theater.cancel_booking(3)
# Output: Booking for seat 3 has been cancelled.

theater.get_booked_seats()
# Output: Booked seats: []