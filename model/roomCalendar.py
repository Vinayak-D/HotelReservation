#Calendar Class
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

class Calendar():
    
    def __init__(self, n):
        
        if n > 0:
            self.nDays = int(n)
        else:
            print('Calendar must look ahead more than 1 day!, defaulting to 1 day')
            self.nDays = 1
        self.bookingDays = []
        #Get today's date (string)
        startDate = date.today()
        self.bookingDate = startDate.strftime('%Y-%m-%d')
        #Get date 'nMonths' from now 
        #the person must CHECK OUT before this
        endDate = startDate + relativedelta(days = self.nDays)
        self.finalDate = endDate.strftime('%Y-%m-%d')
        
        #Get all days from today to 'nMonths' ahead
        delta = endDate - startDate
        for i in range(delta.days + 1):
            day = startDate + timedelta(days = i)
            #since nobody is initially booked, append 'none' to each day
            x = list((day, 'none'))
            self.bookingDays.append(x)

    def returnAllbookingDays(self):
        return self.bookingDays        

    def returnAvailableDateRange(self):
        return self.bookingDate, self.finalDate


        
        
        
        
        