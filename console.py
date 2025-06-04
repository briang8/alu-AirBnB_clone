#!/usr/bin/python3
"""
Command Interpreter Module for HBNB Project
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

MODELS = {
    "BaseModel": BaseModel,
    "User": User,
    "City": City,
    "Place": Place,
    "Review": Review,
    "State": State,
    "Amenity": Amenity,
}


def validate_args(args_list):
    """
    Validates command arguments to ensure they meet requirements.
    """
    if not args_list:
        print("** class name missing **")
        return False

    class_name = args_list[0]
    if class_name not in MODELS:
        print("** class doesn't exist **")
        return False

    if len(args_list) < 2:
        print("** instance id missing **")
        return False

    return True


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Handles EOF to exit the program (Ctrl+D)."""
        return True

    def do_create(self, cls_name):
        """Creates an instance of a Model"""
        if not cls_name:
            print("** class name missing **")
            return
        if cls_name not in MODELS:
            print("** class doesn't exist **")
            return

        new_model = MODELS[cls_name]()
        new_model.save()
        print(new_model.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance
        Use: show <class name> <id>
        """
        args_list = str.split(args)

        if not validate_args(args_list):
            return

        class_name = args_list[0]
        instance_id = args_list[1]
        key = "{}.{}".format(class_name, instance_id)
        objects = storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance\nUse: destroy <class name> <id>"""
        args_list = str.split(args)
        if not validate_args(args_list):
            return

        class_name = args_list[0]
        instance_id = args_list[1]
        objects = storage.all()
        key = "{}.{}".format(class_name, instance_id)
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, cls):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        objects = storage.all()
        obj_list = []

        # If no class name is provided, print all instances
        if not cls:
            for obj in objects.values():
                obj_list.append(str(obj))
        # If class name is provided and valid, print only
        # instances of that class
        elif cls in MODELS:
            for key, obj in objects.items():
                if key.split(".")[0] == cls:
                    obj_list.append(str(obj))
        else:
            print("** class doesn't exist **")
            return

        print(obj_list)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        by adding or updating an attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args_list = args.split()

        # Validate class name and id
        if not validate_args(args_list):
            return

        # Check if attribute name is provided
        if len(args_list) < 3:
            print("** attribute name missing **")
            return

        # Check if attribute value is provided
        if len(args_list) < 4:
            print("** value missing **")
            return

        class_name = args_list[0]
        instance_id = args_list[1]
        attr_name = args_list[2]

        # Handle the case where attribute value might contain spaces
        # Join the remaining args as the attribute value
        attr_value = args.split(" ", 3)[3]

        # Remove quotes if present
        if attr_value.startswith('"') and attr_value.endswith('"'):
            attr_value = attr_value[1:-1]

        # Skip update for protected attributes
        if attr_name in ["id", "created_at", "updated_at"]:
            return

        # Find the instance and update it
        key = "{}.{}".format(class_name, instance_id)
        objects = storage.all()

        if key in objects:
            instance = objects[key]

            # Try to cast the value to the appropriate type
            try:
                # First try to convert to int or float if possible
                if attr_value.isdigit():
                    attr_value = int(attr_value)
                else:
                    try:
                        attr_value = float(attr_value)
                    except ValueError:
                        # Keep it as string if conversion fails
                        pass

                # Update the instance attribute
                setattr(instance, attr_name, attr_value)
                instance.save()

            except Exception as e:
                print(f"Error updating attribute: {e}")
        else:
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
