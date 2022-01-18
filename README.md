# HotelReservation
## A simple hotel reservation system
To get the code running, please download the repo and run **main.py**, you can select a test case (**testCases.py**). Please look at the test cases to see how the program is initialized.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This program is a basic hotel reservation system. It is my first true OOP based project. A hotel can be defined with any number of rooms of 3 different suites: Standard, Deluxe, Executive (varying prices). The features are:

1. Any number of customers can be added and stored in a database. Each customer has a unique ID which is used to create/modify/cancel a booking.
2. Each room has a calendar that keeps track of bookings. The calendar length is customizable - i.e. the booking date range can be up to the user (90-120 days ahead is a good value). This is meant for realism, you can't book something 10 years in advance!
3. Reservations can be cancelled or modified. Refunds are also provided.
4. Each customer has an Invoice which prints the bill at the end and is updated if the reservation is cancelled or modified.
5. The program shows the user which rooms are available on the selected dates, along with the range of booking dates possible (how late the checkout date can be). If a room is sold out for the dates requested, it will not show up on the list.

## The following describes the current limitations of the program, as the degree of complexity is endless:

1. There is only one Hotel
2. If the user inputs incorrect values or data types, there is an error message provided, however the function has to be re-initialized again. However to avoid this happening, the program provides prompts throughout - as in point 5 above.
3. There is no housekeeping or receptionist assigned to each room. 
4. The price of each suite type is uniform and holidays are not considered.
5. If 2 customers have the same first name and last name letter, along with the same last 4 digits of phone number, this will conflict the ID, however what are the chances of that in real life!

## The following edge cases are considered:

1. Sold out Hotel
2. Incorrect customer ID selected
3. Overlapping of booking dates between two customers of the same room (when modifying or creating a new reservation)
4. Dates falling outside the booking database limits 
5. Double booking of the same customer

Please read the 5 test cases of which cases 1-4 cover the above edge cases.

## The time complexity for some of the methods is as follows: Let the variables represent:

1. **nRooms** = number of total Rooms
2. **nDays** = number of Calendar days (per room)
3. **nBookedDays** = number of days booked by the customer (<nDays) - (checkOutDate - checkInDate)

1. **checkIfHotelBooked()**: nRooms - since it has to search each room to see if it's booked or not.

2. **checkReservationDates()**: 2*nDays + 2*nBookedDays - since this method first extracts all the dates from the Calendar list, then checks if the checkinDate and checkOutDate falls within this list, along with getting their indices within the list. Obtaining these indices are important since then the second operation (+ nBookedDays) goes directly to the section of the calendar between the check-in/out dates. The second iteration of nBookedDays checks if the ID is 'none' or assigned to a customer ID. Each of these days has to be checked. NOTE: To see if the check

3. **bookCustomer()**: nBookedDays - this method assigns the customer ID to the section of the calendar within the check-in/out dates, to each booked day. Since it is called after checkReservationDates(), there is no need to check again if the ID assigned to the room date is 'none' prior to booking. If this check was added here, the complexity would be 2*nBookedDays. The reservation flag inside checkReservationDates() value tells the makeReservation() method if the dates fall within the range and if there is no active booking present simultaneously.

## Class Diagram

![classDiagram](https://user-images.githubusercontent.com/56367517/150004359-aa561ada-2a76-4819-a04a-0cf8bd3cc724.png)

## Activity Diagram - Make a Reservation

![makeReservation](https://user-images.githubusercontent.com/56367517/150004410-2abf0e8b-fe1d-49c2-b4d4-6d7908926cdf.png)

## Activity Diagram - Modify a Reservation

![modReservation](https://user-images.githubusercontent.com/56367517/150004420-0773bd6c-6ecf-42d4-b569-3c854eda6f9d.jpg)

## Activity Diagram - Cancel a Reservation

![cancelReservation](https://user-images.githubusercontent.com/56367517/150004426-c645f91e-516d-42db-b951-cd8945731c5e.png)
