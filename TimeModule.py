import copy
from enum import IntEnum

#A representation of "Days"
class Days(IntEnum):
    LUNES = 0
    MARTES = 1
    MIERCOLES = 2
    JUEVES = 3
    VIERNES = 4

    def __str__(self):
        if(self.value == 0): return "Lunes"
        elif(self.value == 1): return "Martes"
        elif(self.value == 2): return "Miércoles"
        elif(self.value == 3): return "Jueves"
        elif(self.value == 4): return "Viernes"

    def getColumn(self):
        if(self.value == 0): return "B"
        elif(self.value == 1): return "C"
        elif(self.value == 2): return "D"
        elif(self.value == 3): return "E"
        elif(self.value == 4): return "F"

    def fromString(string):
        if (string == "Lunes"): return Days.LUNES
        elif (string == "Martes"): return Days.MARTES
        elif (string == "Miércoles"): return Days.MIERCOLES
        elif (string == "Jueves"): return Days.JUEVES
        elif (string == "Viernes"): return Days.VIERNES

    def fromStringArray(stringArr):
        daysArray = []
        for x in stringArr:
            daysArray.append(Days.fromString(x))
        return daysArray

class Time:

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def fromString(timeString):
        time = timeString.split(':')
        timeObj = Time(int(time[0]), int(time[1]))
        return timeObj

    def __str__(self):
        if (self.minutes > 9):
            return "{}:{}".format(self.hours, self.minutes)
        else:
            return "{}:0{}".format(self.hours, self.minutes)

    def add(self, minutes):
        self.hours += (self.minutes + minutes) // 60
        self.minutes = (self.minutes + minutes) % 60

    def isLater(self, otherTime):
        return (self.hours > otherTime.hours) or (self.hours == otherTime.hours and self.minutes > otherTime.minutes)

    def isEqual(self, otherTime):
        return (self.hours == otherTime.hours) and (self.minutes == otherTime.minutes)

    def distance(time1, time2):
        totalMin = 0
        if time1<=time2:
            minutes = time2.minutes - time1.minutes
            hours = time2.hours - time1.hours
            totalMin = hours*60 + minutes
        else:
            minutes = time1.minutes - time2.minutes
            hours = time1.hours - time2.hours
            totalMin = hours*60 + minutes
        return totalMin

    def __lt__(self, otherTime):
        return not(self.isLater(otherTime)) and not(self.isEqual(otherTime))

    def __le__(self, otherTime):
        return not(self.isLater(otherTime))

    def __eq__(self, otherTime):
        return self.isEqual(otherTime)

    def __ge__(self, otherTime):
        return self.isLater(otherTime) or self.isEqual(otherTime)

    def __gt__(self, otherTime):
        return self.isLater(otherTime)

class TimeRange:
    def __init__(self, initial, final):
        self.initial = initial
        self.final = final

    def __str__(self):
        return "{} - {}".format(str(self.initial), str(self.final))

    def __len__(self):
        return Time.distance(self.initial, self.final)

    def timeRangeArray(timeRange, step=30):
        timeList = []
        current = copy.deepcopy(timeRange.initial)
        while(current <= timeRange.final):
            timeList.append(copy.deepcopy(current))
            current.add(step)
        return timeList

    def rangesOverlap(firstRange, secondRange):
        return ((firstRange.initial >= secondRange.initial) and (firstRange.initial < secondRange.final)
               or (firstRange.final>secondRange.initial) and (firstRange.final <= secondRange.final)
               or (secondRange.initial >= firstRange.initial) and (secondRange.initial < firstRange.final)
               or (secondRange.final > firstRange.initial) and (secondRange.final <= firstRange.final))

    def findTimeRange(subjectList):
        lowestTime = subjectList[0].timeRange.initial
        highestTime = subjectList[0].timeRange.final
        for subject in subjectList:
            if(subject.timeRange.initial < lowestTime): lowestTime = subject.timeRange.initial
            if(subject.timeRange.final > highestTime): highestTime = subject.timeRange.final
        return TimeRange(lowestTime, highestTime)

    #True if second range contains first
    def timeRangesInside(first, second):
        return (first.initial >= second.initial) and (first.final <=  second.final)
