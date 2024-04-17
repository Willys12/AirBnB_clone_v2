#!/usr/bin/python3
import unittest
from console import HBNBCommand
import os

class test_console(unittest.TestCase):
    """ """

    def test_create_valid_parameters(self):
        """
        Creating obj with valid params
        """
        command = HBNBCommand()
        args = "User name=\"John Doe\" email=johndoe@gmail.com"
        command.do_create(args)
        user = storage.get("User", command.output)
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.email, "johndoe@gmail.com")

    def test_craete_invalid_parameters(self):
        """
        Test creating an object with invalid params
        """
        command = HBNBCommand()
        args = "User name=John Doe email=johndoe@gmail.com age=25.5"
        command.do_create(args)
        self.assertEqual(command.output, "Invalid parameter value for age: 25.5")

    def test_create_missing_class_name(self):
        """
        Test creating an object with missing class name.
        """
        command = HBNBCommand()
        args = "name=\"John Doe\" email=johndoe@gmail.com"
        command.do_create(args)
        self.assertEqual(command.output, "** Class name missing **")

    def test_create_nonexistent_class(self):
        """
        Test creating an object with non-existent class
        """
        command = HBNBCommand()
        args = "MyClass name=\"John Doe\" email=johndoe@gmail.com"
        command.do_create(args)
        self.assertEqual(command.output, "** class name doesn't exist **")


if __name__ == "__main__":
    unittest.main()
