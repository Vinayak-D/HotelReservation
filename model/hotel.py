#Hotel Class
from model.room import Room

class Hotel:
    def __init__(self, name, nSRooms, nDRooms, nERooms, n):

        try:
            self.name = str(name)
            if int(nSRooms + nDRooms + nERooms) > 0:
                self.nSRooms = int(nSRooms)
                self.nDRooms = int(nDRooms)
                self.nERooms = int(nERooms)
            else:
                print('Hotel must have more than 1 room!, defaulting to 1 standard room..')
                self.nSRooms = 1
                self.nDRooms = 0
                self.nERooms = 0
        except ValueError:
            print('Invalid Data Type, defaulting to 1 standard room')
            self.nSRooms = 1
            self.nDRooms = 0
            self.nERooms = 0         
        
        self.totalRooms = self.nSRooms + self.nDRooms + self.nERooms
               
        #data structure containing room instances, search by customer (r) 
        self.roomsData = {}
        self.roomsData['ID'] = []
        self.roomsData['Room'] = []
        self.fullyBooked = 0
        
        #Append instances of room/customer based on standard rooms
        for i in range(self.nSRooms):
            r = Room('S', n)
            self.roomsData['ID'].append(str(i+1) + 'S')
            self.roomsData['Room'].append(r)
            
        #Append instances of room/customer based on deluxe rooms
        for i in range(self.nDRooms):
            r = Room('D', n)
            self.roomsData['ID'].append(str(i+1) + 'D')
            self.roomsData['Room'].append(r)
        
        #Append instances of room/customer based on executive rooms
        for i in range(self.nERooms):
            r = Room('E', n)
            self.roomsData['ID'].append(str(i+1) + 'E')
            self.roomsData['Room'].append(r)
            
    def displayRoomsOfType(self, stype):
        stype = str(stype)
        if stype == 'S':
            roomOptions = self.roomsData['ID'][0:self.nSRooms]
            print('Standard Rooms:')
            print(roomOptions)
        elif stype == 'D':
            roomOptions = self.roomsData['ID'][self.nSRooms:self.nSRooms+self.nDRooms]
            print('Deluxe Rooms')
            print(roomOptions)
        elif stype == 'E':
            roomOptions = self.roomsData['ID'][self.nSRooms+self.nDRooms:self.nSRooms+self.nDRooms+self.nERooms]
            print('Executive Rooms')
            print(roomOptions)
        else:
            print('Room type does not exist!')
            
    def checkIfHotelBooked(self, chkInDate, chkOutDate):
        numBooked = 0
        for i in range(len(self.roomsData['Room'])):
            (a, b) = self.roomsData['Room'][i].checkReservationDates(chkInDate,chkOutDate)
            if b == Room.reservedStatus['2']:
                numBooked += 1
            else:
                print('Room #:', self.roomsData['ID'][i], 'is available for your chosen dates')
        if numBooked == self.totalRooms:
            self.fullyBooked = 1
        else:
            self.fullyBooked = 0
        return self.fullyBooked
            
    def findSpecificRoom(self, roomSel):
        #select a room by finding it's index within hash table and returning instance
        self.roomIndex = self.roomsData['ID'].index(roomSel)
        self.room = self.roomsData['Room'][self.roomIndex]
        return self.room
    
    def returnRoomsData(self):
        return self.roomsData
    
    def returnName(self):
        return self.name
