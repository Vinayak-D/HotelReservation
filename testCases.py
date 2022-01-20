#All the Test Cases
from model.reservation import Reservation
from operator import attrgetter
from datetime import date
from dateutil.relativedelta import relativedelta
#Please read first!------------------------------------------------------------

#The Reservation class takes 4 parameters: number of standard rooms, number of 
#deluxe rooms, and number of executive rooms, along with the number of days the
#calendar looks ahead.
#Example: R = Reservation(10,10,10,30) means that there are 10 of each room in
#the hotel, and the user can book up to 30 days ahead.

#The addCustomer() method takes in first/last name, number of guests, and phone #
#The makeReservation() and modifyReservation() methods require the ID, and the check 
#in/out dates for the customer. The ID is generated automatically when the customer is added, it's the
#first and last initial along with last 4 digits of the phone number.

#------------------------------------------------------------------------------

#Since you will download this program at a different date, everything is relative to the 
#date you run the program, i.e. 'today's date'

#------------------------------------------------------------------------------
#get today's date and convert to a tuple
dateToday = date.today()
#------------------------------------------------------------------------------

def testCase1():
    
    #Description---------------------------------------------------------------
    
    #This is the simplest test case
    #The user accidentally has entered 0 rooms and 0 days, in which case the hotel defaults
    #to having 1 standard room only. The calendar defaults to looking 1 day ahead.
    #This means that the user can only book today's date in 1 room!
    
    #Purpose-------------------------------------------------------------------
    #The purpose of this test is to add 2 customers, book the first customer which
    #sells out the hotel, and ensure that the second customer is not able to book
    
    #get the date tuple from the object via 'attrgetter()'
    dateIn = attrgetter(*Reservation.attrs)(dateToday)
    dateOut = dateToday + relativedelta(days = 1)
    dateOut = attrgetter(*Reservation.attrs)(dateOut)
    reservation = Reservation(0, 0, 0, 0)
    reservation.addCustomer('Vin', 'Desh', 0, 1234567891)
    reservation.makeReservation('VD7891', dateIn, dateOut)
    reservation.addCustomer('John', 'Doe', 0, 1234567891)
    #this should return the 'Sold Out' message
    reservation.makeReservation('JD7891', dateIn, dateOut)
    
    #Expected output: 'JD7891 Hotel is sold out for your selected dates!'

def testCase2():
    
    #Description---------------------------------------------------------------
    #Similar to test 1 with correct inputs
    
    #Purpose-------------------------------------------------------------------
    #The purpose of this test is to add 2 customers, book the first customer which
    #sells out the hotel, cancel and refund customer 1, and then book customer 2

    dateIn = attrgetter(*Reservation.attrs)(dateToday)
    dateOut = dateToday + relativedelta(days = 1)
    dateOut = attrgetter(*Reservation.attrs)(dateOut)
    
    reservation = Reservation(1, 0, 0, 1)
    reservation.addCustomer('Vin', 'Desh', 0, 1234567891)
    reservation.addCustomer('John', 'Doe', 0, 1234567891)
    reservation.makeReservation('VD7891', dateIn, dateOut)
    reservation.cancelReservation('VD7891')
    #John should be able to make a reservation 
    reservation.makeReservation('JD7891', dateIn, dateOut)
    
    #Expected output, both reservation invoices
    
def testCase3():
    
    #Description---------------------------------------------------------------
    #3 rooms are available and the user accidentally does a double booking, and then
    #the user accidentally books the other customer in the same room (with overlapping dates)
    
    #Purpose-------------------------------------------------------------------
    #The purpose of this test is to ensure that a double booking does not occur, and another
    #customer cannot book the same room as the first active customer.

    #tomorrow's date
    dateVin = dateToday + relativedelta(days = 1)
    dateVin = attrgetter(*Reservation.attrs)(dateVin)
    #next week
    dateVout = dateToday + relativedelta(days = 7)
    dateVout = attrgetter(*Reservation.attrs)(dateVout)
    #11 days from today
    dateVout2 = dateToday + relativedelta(days = 11)
    dateVout2 = attrgetter(*Reservation.attrs)(dateVout2)    
    #5 days from today
    dateJin = dateToday + relativedelta(days = 5)
    dateJin = attrgetter(*Reservation.attrs)(dateJin)   
    #13 days from today
    dateJout = dateToday + relativedelta(days = 13)
    dateJout = attrgetter(*Reservation.attrs)(dateJout)  
    
    reservation = Reservation(1, 1, 1, 30)
    reservation.addCustomer('Vin', 'Desh', 0, 123456789)
    reservation.addCustomer('John', 'Doe', 0, 123456789)
    reservation.makeReservation('VD6789', dateVin, dateVout)
    #This reservation should not be booked
    reservation.makeReservation('VD6789', dateVin, dateVout2)
    #This reservation should not show Vin's room selection due to overlapping dates
    #since dateJin is before dateVout
    reservation.makeReservation('JD6789', dateJin, dateJout)
    
def testCase4():
    
    #Description---------------------------------------------------------------
    #1 room is available, the calendar is available 6 days ahead from today, customer 1 books
    #first 3 days, customer 2 books next 3. Customer 1 attempts to modify their reservation
    #whilst choosing dates that overlap with customer 2's booking
    
    #Purpose-------------------------------------------------------------------
    #The purpose of this test is to ensure that Customer 1 should not be able to modify his
    #reservation since customer 2 has a conflicting booking
    
    dateVIn = attrgetter(*Reservation.attrs)(dateToday)
    #3 days from today
    dateOut = dateToday + relativedelta(days = 3)
    dateOut = attrgetter(*Reservation.attrs)(dateOut) 
    #6 days from today
    dateOut2 = dateToday + relativedelta(days = 6)
    dateOut2 = attrgetter(*Reservation.attrs)(dateOut2) 
    #4 days from today
    dateOut3 = dateToday + relativedelta(days = 4)
    dateOut3 = attrgetter(*Reservation.attrs)(dateOut3) 
    
    reservation = Reservation(0, 1, 0, 6)
    reservation.addCustomer('Vin', 'Desh', 0, 123456789)
    reservation.addCustomer('John', 'Doe', 0, 123456789)
    reservation.makeReservation('VD6789', dateVIn, dateOut)
    reservation.makeReservation('JD6789', dateOut, dateOut2)
    #Vin's reservation should not be able to modify due to conflict
    #Attempt to modify dates with checkout date conflicting with John
    reservation.modifyReservation('VD6789', dateVIn, dateOut3)
    #The expected output should be the dates resetting and Vin being able to rebook the same room

def testCase5():
    
    #Description---------------------------------------------------------------
    #This is a normal test case, with 10 rooms in each suite, 45 days lookahead, and 2 random bookings
    
    #Purpose-------------------------------------------------------------------
    #The purpose of these tests is to ensure that these 2 bookings can be made and
    #modified, provided you choose the correct rooms (as per prompt)
    
    date1 = attrgetter(*Reservation.attrs)(dateToday)
    #3 days from today
    date2 = dateToday + relativedelta(days = 3)
    date2 = attrgetter(*Reservation.attrs)(date2) 
    #6 days from today
    date3 = dateToday + relativedelta(days = 6)
    date3 = attrgetter(*Reservation.attrs)(date3) 
    #9 days from today
    date4 = dateToday + relativedelta(days = 9)
    date4 = attrgetter(*Reservation.attrs)(date4)      
    
    reservation = Reservation(10, 10, 10, 45)
    reservation.addCustomer('Vin', 'Desh', 0, 123456789)
    reservation.addCustomer('David', 'Venuto', 0, 123456789)
    #Choose different dates to completely avoid any conflicts
    reservation.makeReservation('VD6789', date1, date2)
    reservation.makeReservation('DV6789', date3, date4)
    
    #This is your choice, you can choose any random dates here, and modify anyone
    reservation.modifyReservation('VD6789', date1, date4)
    
    
    
    