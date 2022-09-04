#!/usr/bin/python3

"""
    The console.py module, provides a single class

"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """ The command class to manupulate the args """

    prompt = "(hbnb) "
    class_list = [
        'BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review'
    ]

    # ______basic commands_________
    def do_quit(self, arg):
        """ quits the cmd interpreter """
        return True

    def do_EOF(self, arg):
        """ exits the cmd """
        return True

    def emptyline(line):
        return False

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if not line:
            print('** class name missing **')
            return False
        try:
            new_model = eval(line + '()')
            new_model.save()
            print(new_model.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ Prints the string representation
        of an instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.

        """
        if not line:
            print('** class name missing **')
            return False
        cmd_list = shlex.split(line)
        if len(cmd_list) > 0:
            if len(cmd_list) == 1:
                print("** instance id missing **")
                return False
            try:
                all_inst = storage.all()
                eval(cmd_list[0] + '()')
                ins_id = "{}.{}".format(cmd_list[0], cmd_list[1])
                instance = all_inst[ins_id]
                print(instance)
            except NameError:
                print("** class doesn't exist **")
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, line):
        """
            Deletes an instance based on the class
            name and id (save the change into the JSON file).
            Ex: $ destroy BaseModel 1234-1234-1234
        """

        if not line:
            print('** class name missing **')
            return False
        cmd_list = line.split()
        if len(cmd_list) > 0:
            if len(cmd_list) == 1:
                print("** instance id missing **")
                return False
            try:
                all_inst = storage.all()
                eval(cmd_list[0] + '()')
                ins_id = "{}.{}".format(cmd_list[0], cmd_list[1])
                instance = all_inst[ins_id]
                all_inst.pop(ins_id)
                del instance
                storage.save()
            except NameError:
                print("** class doesn't exist **")
            except KeyError:
                print("** no instance found **")

    def do_all(self, line):
        """
           Prints all string representation of all
        instances based or not on the class name.
        Ex: $ all BaseModel or $ all

        """
        all_inst = storage.all()
        inst_list = []
        if line:
            if line not in self.class_list:
                print("** class doesn't exist **")
                return False
            else:
                for key, val in all_inst.items():
                    if key.startswith(line):
                        inst_list.append(val.__str__())
                print(inst_list)
        else:
            for instance in all_inst.values():
                inst_list.append(instance.__str__())
            print(inst_list)

    def do_update(self, line):
        """
           Updates an instance based on the class name and id
           by adding or updating attribute
           Ex: $ update BaseModel 1234-1234-1234 email
        """
        if not line:
            print("** class name missing **")
        else:
            cmd_list = shlex.split(line)
            if cmd_list[0] not in self.class_list:
                print("** class doesn't exist **")
                return False
            if len(cmd_list) == 1:
                print("** instance id missing **")
                return False
            elif len(cmd_list) == 2:
                print("** attribute name missing **")
                return False
            elif len(cmd_list) == 3:
                print("** value missing **")
                return False
            else:
                not_to_be_updated = ["id", "created_at", "updated_at"]
            if cmd_list[2] not in not_to_be_updated:
                try:
                    all_objs = storage.all()
                    obj_id = "{}.{}".format(cmd_list[0], cmd_list[1])
                    obj = all_objs[obj_id]
                    attr = cmd_list[2]
                    value = cmd_list[3]
                    setattr(obj, attr, value)
                    storage.save()
                except KeyError:
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
