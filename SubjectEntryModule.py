from TimeModule import *
import json
import io

class SubjectModule(IntEnum):
    TEORICO = 0
    PRACTICO = 1
    TEOPRA = 2
    CONSULTA = 3

    def __str__(self):
        if(self.value == 0): return "Teórico"
        elif(self.value == 1): return "Práctico"
        elif(self.value == 2): return "Teórico/Práctico"
        elif(self.value == 3): return "Consulta"

    def fromString(moduleName):
        if(moduleName == "Teórico"): return SubjectModule.TEORICO
        elif(moduleName == "Práctico"): return SubjectModule.PRACTICO
        elif(moduleName == "Teo-Pra"): return SubjectModule.TEOPRA
        elif(moduleName == "Consulta"): return SubjectModule.CONSULTA

class SubjectEntry:
    def __init__(self, name, module, timeRange, days):
        self.name = name
        self.module = module
        self.timeRange = timeRange
        self.days = days

    def printEntry(self):
        print("-------------------------")
        print("Subject : {}\nInitial Time : {}\nFinal Time : {}\nDays : {}".format(self.name, self.timeRange.initial, self.timeRange.final, [str(day) for day in self.days]))
        print("-------------------------")

    def parseJSON(filepath):
        allSubjects = []
        myfile = open(filepath, encoding="utf-8-sig")
        myJSON = json.load(myfile)
        for subject in myJSON:
            subJSON = myJSON[subject]
            newSubjectEntry = SubjectEntry(subJSON["name"],
                                    SubjectModule.fromString(subJSON["module"]),
                                    TimeRange(Time.fromString(subJSON["initialTime"]),
                                    Time.fromString(subJSON["finalTime"])),
                                    Days.fromStringArray(subJSON["days"]))
            allSubjects.append(newSubjectEntry)
        return allSubjects

    def parseJSONWithChoices(filepath, choices):
        allSubjects = []
        myfile = open(filepath, encoding="utf-8-sig")
        myJSON = json.load(myfile)
        for subject in myJSON:
            subJSON = myJSON[subject]
            newSubjectEntry = SubjectEntry(subJSON["name"],
                                    SubjectModule.fromString(subJSON["module"]),
                                    TimeRange(Time.fromString(subJSON[choices[subject]]["initialTime"]),
                                    Time.fromString(subJSON[choices[subject]]["finalTime"])),
                                    Days.fromStringArray(subJSON[choices[subject]]["days"]))
            allSubjects.append(newSubjectEntry)
        return allSubjects

    def daysInCommon(firstSubject, secondSubject):
        return list(set(firstSubject.days).intersection(secondSubject.days))

    def subjectsOverlap(firstSubject, secondSubject):
        return (SubjectEntry.daysInCommon(firstSubject, secondSubject) != []) and TimeRange.rangesOverlap(firstSubject.timeRange, secondSubject.timeRange)

    def subjectListOverlap(subjectList):
        overlapingList = []
        for i in range(len(subjectList) - 1):
            for j in range(i+1, len(subjectList)):
                if(SubjectEntry.subjectsOverlap(subjectList[i], subjectList[j])):
                    overlapingList.append([subjectList[i], subjectList[j]])
        return overlapingList
