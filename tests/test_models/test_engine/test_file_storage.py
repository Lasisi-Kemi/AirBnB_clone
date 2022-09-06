#!/usr/bin/python3
"""
   file testing the file_storage module

"""

import unittest
import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class testFileStorage(unittest.TestCase):
    """ the file storage module test class """

    def test_file_storage_class_membership(self):
        "checks the instantiation of the file_storage class"
        storage = FileStorage() 
        self.assertIsInstance(storage, FileStorage)

    def test_all_method(self):
        """ checks the file_storage all() method """
        storage = FileStorage()
        self.assertIs(type(storage.all()), dict)

    def test_new_method(self):
        """ test the new method """
        storage = FileStorage()
        dic = {
            'name': "model 1",
            'number': 56,
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'id': str(uuid.uuid4())
        }
        storage.new(BaseModel(**dic))
        all_objs = storage.all()
        obj_key = "BaseModel.{}".format(dic['id'])
        self.assertIsInstance(all_objs[obj_key], BaseModel)

    def teste_save_method(self):
        """ tests the filestorage save mehthod """
        base = BaseModel()
        storage = FileStorage()
        key = "{}.{}".format(type(base).__name__, base.id)
        self.assertTrue(key in storage.all())
