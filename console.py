#!/usr/bin/python3
"""
Console module

This module provides a command interpreter for managing AirBnB objects.
"""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for managing AirBnB objects.

    Attributes:
        prompt (str): The command prompt string
    """

    prompt = "(hbnb) "

    # Map of valid class names
    __classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """
        Create a new instance of a class, save it, and print the id.
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        class_name = args[0]

        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        new_instance = HBNBCommand.__classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """
        Print the string representation of an instance.
        Usage: show <class name> <id>
        """
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        class_name = args[0]

        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all()

        if key not in all_objs:
            print("** no instance found **")
            return

        print(all_objs[key])

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        Usage: destroy <class name> <id>
        """
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)
        class_name = args[0]

        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all()

        if key not in all_objs:
            print("** no instance found **")
            return

        del all_objs[key]
        storage.save()

    def do_all(self, arg):
        """
        Print string representation of all instances or all instances of a class.
        Usage: all [class name]
        """
        all_objs = storage.all()
        obj_list = []

        if not arg:
            # Print all instances
            for obj in all_objs.values():
                obj_list.append(str(obj))
        else:
            args = shlex.split(arg)
            class_name = args[0]

            if class_name not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return

            # Print instances of specified class
            for key, obj in all_objs.items():
                if key.startswith(class_name + '.'):
                    obj_list.append(str(obj))

        print(obj_list)

    def do_update(self, arg):
        """
        Update an instance based on the class name and id.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)

        if len(args) < 1:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all()

        if key not in all_objs:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        obj = all_objs[key]
        attr_name = args[2]
        attr_value = args[3]

        # Don't update id, created_at, updated_at
        if attr_name in ['id', 'created_at', 'updated_at']:
            return

        # Try to cast the value to the appropriate type
        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            try:
                attr_value = attr_type(attr_value)
            except (ValueError, TypeError):
                pass
        else:
            # Try to infer the type
            try:
                attr_value = int(attr_value)
            except ValueError:
                try:
                    attr_value = float(attr_value)
                except ValueError:
                    pass  # Keep as string

        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
