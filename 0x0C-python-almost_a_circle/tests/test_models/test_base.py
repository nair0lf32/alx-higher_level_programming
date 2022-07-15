#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Test Base class """

    def setUp(self):
        """ a method for each test """
        Base._Base__nb_objects = 0

    def test_id(self):
        """ Test id """
        b = Base(2)
        self.assertEqual(b.id, 2)

    def test_id_nb_objects(self):
        """ Test nb object attribute """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
