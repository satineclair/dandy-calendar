import os
import random

startYear = 1306
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'New Year']        
weekDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
moonCycles = ['New Moon', 'Waxing Crescent Moon', 'First Quarter Moon', 'Waxing Gibbous Moon', 'Full Moon', 'Waning Gibbous Moon', 'Third Quarter Moon', 'Waning Crescent Moon']
moon = ""
cycleLength = 26
halfLength = 40

for year in range(startYear, startYear + 5):
    j = 0
    moonProgress = 3/cycleLength
    for month in months:
        j = j + 1

        monthDays = 28
        
        if month == 'New Year':
            monthDays = 2
        
        for date in range(1, (monthDays + 1)):
            if not os.path.exists(os.getcwd() + os.sep + str(year) + os.sep + str(j) + '-' + month):
                os.makedirs(os.getcwd() + os.sep + str(year) + os.sep + str(j) + '-' + month)
            dayFile = open(os.path.join(os.getcwd(), str(year), str(j) + '-' + month,(str(date).zfill(2) + '.txt')), "w+")
            
            for i in range(8):
                if ((i/8 <= moonProgress) and (moonProgress < ((i+1)/8))):
                    moon = moonCycles[i]
            moonProgress = moonProgress + 1/cycleLength
            if (moonProgress > 1):
                moonProgress = moonProgress - 1
            
            week = date
            while week > 7:
                week = week - 7
            for i in range (1,8):
                if (week % i == 0):
                    weekDay = weekDays[i - 1]

            if month != 'New Year':
                dateLine = weekDay + ', ' + month + ' ' + str(date) + ', ' + str(year)
            else:
                if date == 1:
                    dateLine = 'Last Day of Year ' + str(year)
                else:
                    dateLine = 'First Day of Year ' + str(year + 1)
            dateAppend = len(dateLine)
            dateLine = dateLine.rjust(halfLength, '-')
            dateAppend = halfLength - dateAppend
            charAppend = ''
            charAppend = charAppend.rjust(dateAppend, '-')
            dateLine = dateLine + charAppend
            dayFile.write(dateLine + "\n")
            pageWidth = len(dateLine)
            
            moonLine = moon.rjust((len(dateLine + moon)//2), ' ')
            dayFile.write(moonLine + "\n\n")
            
            dayFile.write('Notable Events:' + "\n\t\n")
            dayFile.write('Party Activity:' + "\n\t\n")
            dayFile.write('Creatures:' + "\n\t\n")

            
            
            
    
            dayFile.close()







