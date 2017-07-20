from SubjectEntryModule import *
from TimeTableModule import *
from SubjectsPermutations import *
from TimeModule import TimeRange
import sys

# TODO:
# - Implement module for subjects
# - Implement blank cells style
# - Implement table borders style
# - Implement days and time style
# - Implement modules styles

VERSION = 0.1

# Main entry of the program
def main():
    #Reading arguments from console for: JSON filename, initial time and final time
    if(len(sys.argv) < 4):
        print("Incorrect number of parameters!")
        print("You must have: json filename, initial time and final time as parameters")
        exit()

    jsonName = sys.argv[1]
    initialTime = Time.fromString(sys.argv[2])
    finalTime = Time.fromString(sys.argv[3])

    #Welcome message
    welcomeMessage(jsonName, initialTime, finalTime)

    #Counter for amount of tables generated
    table_number = 0
    myTimeRange = TimeRange(initialTime, finalTime)

    #Calculating posible combinations of subjects
    tableOfChoices = generateTableFromJSON("Resources/{}".format(jsonName))

    while(not allTrueInTable(tableOfChoices)):
        #Generate one posible combination
        choices = generateNext(tableOfChoices)
        #Grab the info for that combination
        subjects = SubjectEntry.parseJSONWithChoices("Resources/{}".format(jsonName), choices)

        #Checking if the list of subjects is compatible, and generating the table if true
        if(checkSubjectList(subjects, False)):
            myTimeTable = TimeTable(subjects)
            if(TimeRange.timeRangesInside(myTimeTable.baseTimeRange, myTimeRange)):
                myTimeTable.generateTable("Generated Tables/timeTable{}.xlsx".format(table_number))
                table_number += 1

    #Output result
    print("{} tables were generated.".format(table_number))

#Generate a list of lists of Choices from the json file
def generateTableFromJSON(filepath):
    myFile = open(filepath, encoding="utf-8-sig")
    myJSON = json.load(myFile)
    myTable = []
    for subject in myJSON:
        choices_list = []
        for choice in myJSON[subject]:
            if(choice != "name" and choice != "module"):
                choices_list.append(Choice(subject, choice))
        myTable.append(choices_list)
    return myTable


#Checks if the subject list doesn't have any overlapping subjects (overlapping timerange and same day)
def checkSubjectList(subjectList, printing=True):
    overlapingList = SubjectEntry.subjectListOverlap(subjectList)
    if (overlapingList == []): return True
    elif(printing):
        print("The following subjects are overlaping: ")
        for pair in overlapingList:
            print("{} ({}) and {} ({}) with days in common: {}".format(pair[0].name, pair[0].timeRange, pair[1].name, pair[1].timeRange, [str(day) for day in SubjectEntry.daysInCommon(pair[0],pair[1])]))
        return False

#Simple welcome message
def welcomeMessage(jsonfile, initial, final):
    print("=============================================")
    print(" TimeTable Generator ver. {}".format(VERSION))
    print("=============================================")
    print("Current settings:")
    print("   - JSON filename: {}".format(jsonfile))
    print("   - Initial Time: {}".format(initial))
    print("   - Final Time: {}".format(final))
    print("\nGenerating...\n")

if __name__ == "__main__":
    main()
