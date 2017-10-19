# TimeTable-Generator
Console program written in Python 3 that generates all posible time arrangenments for subjects given a JSON file with the options
# Files you need
In orfer to run the program you need a JSON file with correct format (last section) inside Resources
# How to run
In order to run the program you must have installed Python 3.
Then you simply run:
```
python TimeTableGenerator.py jsonFileName initialTime finalTime
```
Where ```jsonFileName``` is the file name of the JSON file inside folder "Resources" with the posible choices for the subjects (More on this in next section). 
The parameters ```initalTime``` and ```finalTime``` are a way of choosing only the tables that have all the subjects between those times.

# JSON File
For this program to work you need to create a folder called ```Resources``` and include inside of it a JSON file. This file will have all subjects with all the posible time intervals.
The format to use is the one in ```Resorces/jsonTemplate.json```.
Where ```module``` can be ```{"Teórico, "Práctico", "Teo-Pra", "Consulta"}```, both ```initialTime``` and ```finishTime``` are given by a 24 hour representation and ```days``` can be ```{"Lunes", "Martes", "Miércoles", "Jueves", "Viernes"}```.

# Dependencies
This program uses ```openpyxl```.
# TODO
There's still a lot of work to do, but the main ones right now are:

- Automate JSON file creation with either a UI or cmd prompts.
- Fix language variations on days and modules.


