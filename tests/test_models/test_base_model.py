#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def test_doc_class(self):
        """Test if the class documentation exist"""
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except FileNotFoundError:
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

    list_met = [BaseModel.__init__, BaseModel.__str__,
                BaseModel.save, BaseModel.to_dict]

    def setUp(self):
        """create a instance"""

    def test_doc_class(self):
        """Test if the class documentation exist"""
        self.assertTrue(len(BaseModel.__doc__) > 0)

    def test_doc_method(self):
        """Test if the method documentation exist"""
        for met in self.list_met:
            self.assertTrue(len(met.__doc__) > 0)

    def test_is_an_instance(self):
        """Test if a object is instance"""
        new_object = BaseModel()
        self.assertIsInstance(new_object, BaseModel)

    def test_att_in_class(self):
        """Test if a attr is in class"""
        new_object = BaseModel()
        self.assertTrue(hasattr(new_object, 'id'))
        self.assertTrue(hasattr(new_object, 'updated_at'))
        self.assertTrue(hasattr(new_object, 'created_at'))

    def test_str(self):
        """Test str function"""
        new_object = BaseModel()
        str_test = "[BaseModel] ({}) {}".format(new_object.id,
                                                new_object.__dict__)
        self.assertEqual(str_test, new_object.__str__())

    def test_save(self):
        """ Test that info is saved to file. """
        new_object = BaseModel()
        new_object.save()
        with open("file.json", 'r') as f:
            self.assertIn(new_object.id, f.read())

    def test_constructor_kwargs(self):
        """
        - Test constructor that has kwargs as attributes values.
        """
        new_object = BaseModel()
        new_dict = new_object.to_dict()
        new_object2 = BaseModel(**new_dict)

        self.assertIsInstance(new_object2, BaseModel)
        self.assertIsInstance(new_dict, dict)
        self.assertIsNot(new_object, new_object2)

    def test_uuid(self):
        """check if two ids are the same"""
        obj_1 = BaseModel()
        obj_2 = BaseModel()
        self.assertNotEqual(obj_1.id, obj_2)
