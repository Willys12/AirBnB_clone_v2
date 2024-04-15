#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
from console import HBNBCommand
import json
import os


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

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
