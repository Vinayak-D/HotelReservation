# makeReservation Class (Top Level)
from HotelClass import Hotel
from CustomerClass import Customer
from operator import attrgetter

class Reservation:
    
    #date attribute
    attrs = ('year','month','day')
    
    def __init__(self,nSRooms,nDRooms,nERooms,n):
        self.H = Hotel('Hotel 1',nSRooms,nDRooms,nERooms,n)
        #Initialize Empty Customer Hash Table (instance and ID)
        self.customerData = {}
        self.customerData['ID'] = []
        self.customerData['Customers'] = []
        #The current selected Customer
        self.currentCustomer = None
        #The current customer select flag
        self.cFlag = 0
        #The successful reservation booking flag
        self.bookedFlag = 0
        #The current active Room
        self.activeRoom = None
        self.cindex = 0
        #Print the booking date range (same for all rooms - customer should see this)
        anyRoom = self.H.returnRoomsData()['Room'][0]
        print('Your check in and check out dates must be within:')
        print(anyRoom.returnRoomCalendarRange())
    
    #add a customer and create a unique reservation ID
    def addCustomer(self,fname,lname,numGuests,number):
        c = Customer(fname,lname,numGuests,number)
        cRID = c.returnReservationID()
        if cRID not in self.customerData['ID']:
            self.customerData['Customers'].append(c)
            self.customerData['ID'].append(cRID)
        else:
            print('Customer already exists!')

    #below methods are for the current Customer
    def makeReservation(self,ID,chkInDate,chkOutDate):
        #reset booking flag at the start
        self.bookedFlag = 0
        #switch to the current customer
        if self.getCurrentCustomer(ID):
            #assign dates to the customer
            self.currentCustomer.assignCustomerDates(chkInDate,chkOutDate)
            dateIn, dateOut = self.currentCustomer.returnCustomerDates()
            if self.H.checkIfHotelBooked(dateIn, dateOut) == 0:
                if self.currentCustomer.returnCustomerRooms() == []:
                    try:
                        print('\nBooking for ID',ID)
                        roomSel = input('Choose a room from the available list: ').upper()
                        self.activeRoom = self.H.findSpecificRoom(roomSel)
                        flag = self.activeRoom.checkReservationDates(dateIn, dateOut)[0]
                        if flag == 1:
                            self.activeRoom.bookCustomer(ID)
                            self.currentCustomer.assignCustomerRoom(roomSel)
                            amount = self.currentCustomer.returnCustomerDays()*self.activeRoom.returnRoomPrice()
                            self.currentCustomer.chargeCustomer(amount)
                            self.returnReservationDetails(ID)
                            self.bookedFlag = 1
                        else:
                            print('Booking unsuccessful for customer ID:',ID)
                            print('Failed to assign customer booking dates')
                    except (ValueError, AttributeError):
                        print('Incorrect Room Selection Choice')
                else:
                    print('\n')
                    print(ID,'is already booked in Room:',self.currentCustomer.returnCustomerRooms())
                    print('\n')
            else:
                print(ID,':Hotel is sold out for the selected dates!')
        else:
            print('Invalid ID')
        return self.bookedFlag
        
    def cancelReservation(self,ID):
        #find customer by ID index, go to that customer
        if self.getCurrentCustomer(ID):
            try:
                roomsAssigned = self.currentCustomer.returnCustomerRooms()[0]
            except IndexError:
                roomsAssigned = []
                print('Either the index is out of range or there is no room booking!')
            if roomsAssigned != []:
                    room = self.H.findSpecificRoom(roomsAssigned)
                    #cancel reservation in room calendar (remove ID)
                    room.cancelBookingByID(ID)
                    amount = self.currentCustomer.returnCustomerCharge()
                    self.currentCustomer.refundCustomer(amount)
                    self.currentCustomer.resetCustomerData()
                    print('Reservation',ID, 'Cancelled')
                    #Delete customer data from the reservation database
                    del self.customerData['ID'][self.cIndex]
                    del self.customerData['Customers'][self.cIndex]
            else:
                print('No rooms assigned for customer',ID)
        else:
            print('Invalid ID')
        
    def returnReservationDetails(self,ID):
        #find customer by ID index, go to that customer
        if self.getCurrentCustomer(ID):
            hname = self.H.returnName()
            (fname,lname,guests,number) = self.currentCustomer.returnCustomerDetails()
            totCharge = self.currentCustomer.returnCustomerCharge()
            rooms = self.currentCustomer.returnCustomerRooms()
            dates = self.currentCustomer.returnCustomerDates()
            if len(rooms) != 0:
                rSel = rooms[0]
            else:
                rSel = rooms
            self.currentCustomer.cInvoice.printBill(hname,fname,lname,guests,number,rSel,totCharge,dates[0],dates[1],ID)
        else:
            print('Invalid ID')
    
    def modifyReservation(self,ID,newInDate,newOutDate):
        #find customer by ID index, go to that customer
        if self.getCurrentCustomer(ID):
            rooms = self.currentCustomer.returnCustomerRooms()
            if rooms:
                #Store old data incase modification not successful
                (fname,lname,numGuests,number) = self.currentCustomer.returnCustomerDetails()
                oldDates = self.currentCustomer.returnCustomerDates()
                print(ID,'has room',rooms,'booked between',oldDates[0],'and',oldDates[1])
                #Cancel and re-initialize customer
                self.cancelReservation(ID)
                self.addCustomer(fname,lname,numGuests,number)
                #Reserve with new dates
                bFlag = self.makeReservation(ID,newInDate,newOutDate)
                if not bFlag:
                #Reserve with old dates as before
                    print('Modification unsuccessful since another customer is booked, resetting dates...\n')
                    oldcInDate = attrgetter(*Reservation.attrs)(oldDates[0])
                    oldcOutDate = attrgetter(*Reservation.attrs)(oldDates[1])
                    self.makeReservation(ID,oldcInDate,oldcOutDate)
            else:
                print('No rooms booked!')
        else:
            print('Invalid ID')
        
    def getCurrentCustomer(self,ID):
        try:
            self.cIndex = self.customerData['ID'].index(str(ID))
            self.currentCustomer = self.customerData['Customers'][self.cIndex]
            self.cFlag = 1
        except ValueError:
            print('The selected customer does not exist within the database')
            self.cFlag = 0
        return self.cFlag