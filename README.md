
## AirBnB clone project

![hbnb logo](hbnb.png)

## INTRO

This project is part of ALX SE Project series aiming towards cloning the [AirBnb web app](https://www.airbnb.com). 

THis version of project implements the console to control the **file storage engine** storing the classes objects or instance amd also to manipulate the object datas easily.

## Usage

The console is a command line format and just like any other command line interpreter, it takes in command and perform certain action based on the command instruction.

## starting the console
clone the repo and cd into AirBnB_clone folder

The console can be run:
1. Interactively
**E.g**
	`./console.py`
output:
	`(hbnb) `
To see a list of commands accepted in iteractive mode:
       	 `(hbnb) help or ?`
output:
	`Documented commands (type help <topic>):
	 ========================================
	 EOF  all  create  destroy  help  quit  show  update`
You can also type:
        `(hbnb) help command_name to see infomation about each command`

2. Non-interactively;
E.g     `$ echo "help" | ./console.py`

Output:
	
	`Documented commands (type help <topic>):
         ========================================
         EOF  all  create  destroy  help  quit  show  update`

List of *classes* that can be created and updated:

- BaseModel
- User
- Place
- State
- City
- Amenity
- Review

Example:

	`(hbnb) create BaseModel`

Output: 
	`49faff9a-6318-451f-87b6-910505c55907`

**Note**: your own ouput may the different as the id are randomely generated