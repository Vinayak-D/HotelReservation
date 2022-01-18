#Invoice Class
import datetime

class Invoice:
    def __init__(self):
        self.creationTime = datetime.datetime.today()
        
    def printBill(self,hname,fname,lname,guests,number,roomSel,amountDue,chkInDate,chkOutDate,ID):
        print('---------------------------------------------')
        print('Hotel Name:',hname)
        print('Created on:',self.creationTime)
        print('Name:',fname+' '+lname)
        print('# of Guests:',guests)
        print('Phone #: ',number)
        print('Room Booked:',roomSel)
        print('Check In Date:',chkInDate)
        print('Check Out Date:',chkOutDate)
        print('\n')
        print('Your Reservation ID:',ID)
        print('Amount Due:',amountDue)
        print('---------------------------------------------')
        print('\n')