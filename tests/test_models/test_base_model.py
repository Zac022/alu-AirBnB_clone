#!/usr/bin/python3
import unittest
from datetime import datetime
from base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.bm = BaseModel()
        self.bm.name = "My First Model"
        self.bm.my_number = 89

    def test_save(self):
        before_save = self.bm.updated_at
        self.bm.save()
        after_save = self.bm.updated_at
        self.assertNotEqual(before_save, after_save)

    def test_to_dict(self):
        bm_dict = self.bm.to_dict()
        self.assertEqual(bm_dict["__class__"], "BaseModel")
        self.assertEqual(bm_dict["created_at"], self.bm.created_at.isoformat())
        self.assertEqual(bm_dict["updated_at"], self.bm.updated_at.isoformat())
        self.assertEqual(bm_dict["id"], self.bm.id)
        self.assertEqual(bm_dict["name"], self.bm.name)
        self.assertEqual(bm_dict["my_number"], self.bm.my_number)

    def test_str(self):
        s_bm = str(

