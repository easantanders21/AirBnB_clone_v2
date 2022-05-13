#!/usr/bin/python3
"""Test module Amenity"""


from models.base_model import BaseModel
from models.amenity import Amenity
import unittest
import datetime
import os


class TestAmenity(unittest.TestCase):
    """New class to test class Amenity"""

    def test_doc_class(self):
        """Test if the class documentation exist"""
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_is_an_instance(self):
        """Test if a object is instance"""
        new_object = Amenity()
        self.assertIsInstance(new_object, Amenity)

    def test_att_in_class(self):
        """Test if a attr is in class"""
        new_object = Amenity()
        self.assertTrue(hasattr(new_object, 'id'))
        self.assertTrue(hasattr(new_object, 'updated_at'))
        self.assertTrue(hasattr(new_object, 'created_at'))
        self.assertTrue(hasattr(new_object, 'name'))

    def test_type_att(self):
        """Test if a attr is type"""
        new_object = Amenity()
        self.assertIsInstance(new_object.name, str)

    def test_subclass(self):
        """Test to check the inheritance"""
        new_object = Amenity()
        self.assertTrue(issubclass(new_object.__class__, BaseModel))

    def test_obj_from_dic(self):
        """Test create new obj from dic"""
        new_object = Amenity()
        dict_new_object = new_object.to_dict()
        new_object2 = Amenity(**dict_new_object)
        self.assertIsInstance(new_object2, Amenity)
        self.assertTrue(issubclass(new_object2.__class__, BaseModel))
        self.assertIsNot(new_object, new_object2)


if __name__ == '__main__':
    unittest.main()
