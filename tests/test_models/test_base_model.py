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
        instance = BaseModel()
        new = self.value()
        self.assertEqual(type(new.id), str)

        # Check that the returned dictionary contains all the expected keys
        dictionary = instance.to_dict()
        self.assertIn('__class__', dictionary)
        self.assertIn('id', dictionary)
        self.assertIn('created_at', dictionary)
        self.assertIn('updated_at', dictionary)

        # Check that the returned dictionary does not contain the _sa_instance_state key
        self.assertNotIn('_sa_instance_state', dictionary)

        # Check that the created_at and updated_at keys are in the correct format
        self.assertIsInstance(dictionary['created_at'], str)
        self.assertIsInstance(dictionary['updated_at'], str)

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

    def test_delete(self):
        """_summary_
        """
        instance = BaseModel()

        # Check that the instance is in the storage
        from models import storage
        self.assertIn(instance, storage.all())

        # Delete the instance
        instance.delete()

        # Check that the instance is no longer in the storage
        self.assertNotIn(instance, storage.all())

        # Check that the instance's id is no longer in the storage
        self.assertNotIn(instance.id, storage.all().keys())

        # Check that the instance's created_at and updated_at attributes are no longer in the storage
        self.assertNotIn(instance.created_at, storage.all().values())
        self.assertNotIn(instance.updated_at, storage.all().values())
    

if __name__ == "__main__":
    unittest.main()
