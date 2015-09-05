#! /usr/bin/env python


def CalculateAge(self,Date):
    '''Calculates the age and days until next birthday from the given birth date'''
    try:
        Date = Date.split('.')
        BirthDate = datetime.date(int(Date[0]), int(Date[1]), int(Date[2]))
        Today = datetime.date.today()

        if (Today.month > BirthDate.month):
            NextYear = datetime.date(Today.year + 1, BirthDate.month, BirthDate.day)
        elif (Today.month < BirthDate.month):
            NextYear = datetime.date(Today.year, Today.month + (BirthDate.month - Today.month), BirthDate.day)
        elif (Today.month == BirthDate.month):
            if (Today.day > BirthDate.day):
                NextYear = datetime.date(Today.year + 1, BirthDate.month, BirthDate.day)
            elif (Today.day < BirthDate.day):
                NextYear = datetime.date(Today.year, BirthDate.month, Today.day + (BirthDate.day - Today.day))
            elif (Today.day == BirthDate.day):
                NextYear = 0

        print (NextYear)
        Age = Today.year - BirthDate.year

        if NextYear == 0: #if today is the birthday
            return '%d, days until %d: %d' % (Age, Age+1, 0)
        else:
            DaysLeft = NextYear - Today
            return '%d, days until %d: %d' % (Age, Age+1, DaysLeft.days)

    except:
        return 'Wrong date format'

# if __name__ == "__main__":
# CalculateAge()
Date = '2000.05.05'
print (CalculateAge(Date))
