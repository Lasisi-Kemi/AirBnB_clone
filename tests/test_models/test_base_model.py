"""
    The base_model.py file test module

"""

import unittest

from models.base_model import BaseModel


class testBaseModel(unittest.TestCase):
    """
        The base_model file test suites

    """
    def test_base_class_membership(self):
        """ tests if obj. is an instance of base_class """
        model_1 = BaseModel()
        self.assertIsInstance(model_1, BaseModel)

    def test_base_class_attr_setting(self):
        """ test setting attribute on the base class """
        model_2 = BaseModel("My second Model", 80)
        self.assertEqual(model_2.name, "My second Model")
        self.assertEqual(model_2.my_number, 80)
        model_2.name = "My name changed"
        model_2.my_number = 81
        
        self.assertEqual(model_2.name, "My name changed")
        self.assertEqual(model_2.my_number, 81)

    def test_str_method(self):
        """ test the str method of the base_class """
        model3 = BaseModel("model three", 82)
        string = model3.__str__()
        self.assertIsInstance(string, str)

    def test_save_method(self):
        """ tests the save method """
        model4 = BaseModel("model four", 83)
        current_time  = model4.updated_at
        model4.save()
        print(current_time, model4.updated_at)
        self.assertNotEqual(current_time, model4.updated_at)
        
    def test_to_dict_method(self):
        """ tests the to_dict method of the base class """
        model5 = BaseModel("model 5", 84)
        model_dict = model5.to_dict()
        self.assertIs(type(model_dict), dict)
    
    def test_to_dict_key_type(self):
        """ checks the type of key returned from the to_dict method """
        
        model6 = BaseModel("model 6", 85)
        m_dict = model6.to_dict()
        for key in m_dict.keys():
            self.assertIs(type(key), str)
