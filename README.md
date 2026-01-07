# AirBnB Clone - The Console

## Project Description

This is the first step towards building a full web application: an AirBnB clone. This project implements a command interpreter to manage AirBnB objects, which will serve as the foundation for subsequent projects involving HTML/CSS templating, database storage, API development, and front-end integration.

The console provides a simple command-line interface to create, retrieve, update, and delete objects such as Users, States, Cities, Places, Amenities, and Reviews. All data is persisted to a JSON file, implementing a complete serialization/deserialization flow.

## Command Interpreter

The command interpreter is similar to a shell but is limited to managing AirBnB objects. It allows you to:

- Create new objects (User, State, City, Place, etc.)
- Retrieve objects from file storage
- Perform operations on objects (count, compute stats, etc.)
- Update object attributes
- Destroy objects

### How to Start the Console

To start the console in interactive mode, run:

```bash
./console.py
```

### How to Use the Console

Once the console is running, you'll see the prompt `(hbnb)`. You can then enter commands.

**Available Commands:**

- `quit` or `EOF` - Exit the console
- `help` - Display help information
- `help <command>` - Display help for a specific command
- `create <class>` - Create a new instance of a class
- `show <class> <id>` - Display the string representation of an instance
- `destroy <class> <id>` - Delete an instance
- `all [class]` - Display all instances or all instances of a class
- `update <class> <id> <attribute> <value>` - Update an instance attribute

### Examples

**Interactive Mode:**

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit  create  show  destroy  all  update

(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) quit
$
```

**Non-Interactive Mode:**

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit  create  show  destroy  all  update
(hbnb) 
$
$ echo "create BaseModel" | ./console.py
(hbnb) 49faff9a-6318-451f-87b6-910505c55907
(hbnb)
$
```

## Project Structure

```
alu-AirBnB_clone/
├── console.py          # Command interpreter
├── models/             # Model classes
│   ├── __init__.py
│   ├── base_model.py   # Base class for all models
│   ├── user.py         # User model
│   ├── state.py        # State model
│   ├── city.py         # City model
│   ├── amenity.py      # Amenity model
│   ├── place.py        # Place model
│   ├── review.py       # Review model
│   └── engine/         # Storage engine
│       ├── __init__.py
│       └── file_storage.py  # File storage implementation
├── tests/              # Unit tests
│   └── test_models/
│       ├── test_base_model.py
│       ├── test_user.py
│       └── ...
├── AUTHORS             # List of contributors
└── README.md           # This file
```

## Testing

All tests are located in the `tests/` directory and use the Python `unittest` module.

To run all tests:

```bash
python3 -m unittest discover tests
```

To run a specific test file:

```bash
python3 -m unittest tests/test_models/test_base_model.py
```

Tests can also be run in non-interactive mode:

```bash
echo "python3 -m unittest discover tests" | bash
```

## Requirements

- Python 3.8.5 or higher
- Ubuntu 20.04 LTS
- Code must be PEP8 compliant (pycodestyle version 2.7.*)
- All files must be executable
- All modules, classes, and functions must have documentation

## Authors

See the [AUTHORS](AUTHORS) file for a list of contributors to this project.
