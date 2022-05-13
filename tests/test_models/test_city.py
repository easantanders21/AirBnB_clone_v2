#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_doc_class(self):
        """Test if the class documentation exist"""
        self.assertTrue(len(City.__doc__) > 0)

    def test_is_an_instance(self):
        """Test if a object is instance"""
        new_object = City()
        self.assertIsInstance(new_object, City)

    def test_att_in_class(self):
        """Test if a attr is in class"""
        new_object = City()
        self.assertTrue(hasattr(new_object, 'id'))
        self.assertTrue(hasattr(new_object, 'updated_at'))
        self.assertTrue(hasattr(new_object, 'created_at'))
        self.assertTrue(hasattr(new_object, 'name'))
        self.assertTrue(hasattr(new_object, 'state_id'))

    def test_type_att(self):
        """Test if a attr is type"""
        new_object = City()
        self.assertIsInstance(new_object.name, str)
        self.assertIsInstance(new_object.state_id, str)

    def test_subclass(self):
        """Test to check the inheritance"""
        new_object = City()
        self.assertTrue(issubclass(new_object.__class__, BaseModel))

    def test_obj_from_dic(self):
        """Test create new obj from dic"""
        new_object = City()
        dict_new_object = new_object.to_dict()
        new_object2 = City(**dict_new_object)
        self.assertIsInstance(new_object2, City)
        self.assertTrue(issubclass(new_object2.__class__, BaseModel))
        self.assertIsNot(new_object, new_object2)