#!/usr/bin/python3
""" test model for main base class"""
import unittest
from time import sleep
import unittest
from models.base_model import BaseModel

"""
class TestCaseBaseModel(unittest.TestCase):
    def setUp(self):
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89
        print(self.my_model)
        self.my_model.save()
        print(self.my_model)
        my_model_json = self.my_model.to_dict()
        print(my_model_json)
        print("JSON of my_model:")
        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
"""


class TestCaseBaseModel(unittest.TestCase):

    def setUp(self):
        """ setting up the various
        components for the test """
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def test_customName(self):
        """ comparison on name """
        # print(self.my_model)
        self.my_model.save()

        # my_model_json = self.my_model.to_dict()
        # print(type(my_model_json))

        # print("JSON of my_model:")
        # for key in my_model_json.keys():
        #   print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

        self.assertEqual(self.my_model.name, "My First Model")

    def test_NumberAdded(self):
        """testing number added """
        self.assertEqual(self.my_model.my_number, 89)

    def test_classType(self):
        """ testing class type """
        self.assertEqual(self.my_model.__class__.__name__, 'BaseModel')

    def test_toDict(self):
        """ to dict returns a dictionary
        testing return type"""
        self.assertEqual(type(self.my_model.to_dict()), dict)

    def test_createdAt(self):
        """ testing if created at is a string
        that can be access with key create_at """
        my_model_json = self.my_model.to_dict()
        self.assertEqual(type(my_model_json['created_at']), str)

    def test_updatedAt(self):
        """ testing if updated at is a string
        that acn be access with key updated at"""
        my_model_json = self.my_model.to_dict()
        self.assertEqual(type(my_model_json['updated_at']), str)

    def test_save(self):
        """ checking if calling save updates the time"""
        old_time = self.my_model.to_dict()['updated_at']
        sleep(1)
        self.my_model.save()
        mode = BaseModel()
        new_time = mode.to_dict()['updated_at']
        # new_time = self.my_model.to_dict()['updated_at']
        self.assertNotEqual(old_time, new_time)

    def test_id(self):
        """ ensuring the id does not
        change for a single instance
        over operations """
        self.my_model.save()
        my_model_json = self.my_model.to_dict()
        self.assertEqual(my_model_json['id'], self.my_model.__dict__['id'])

    def test_str_(self):
        """ test for string print function """
        # clas_name = self.my_model.__class__.__name__
        # the_id = self.my_model.id
        # the_dict = self.my_model.__dict__
        temp_hold = str(self.my_model)
        self.assertEqual(temp_hold.split(" ")[0], "[BaseModel]")
        self.assertEqual(temp_hold.split(" ")[1], "({})".format(self.my_model.id))
        # self.assertEqual(eval(temp_hold.split(" ")[2]), self.my_model.__dict__)

    def test_sizeofDict(self):
        """ensuring the dictionary is the expected length
        as converting to json has one additional value """
        self.assertEqual(len(self.my_model.to_dict()), len(self.my_model.__dict__) + 1)
