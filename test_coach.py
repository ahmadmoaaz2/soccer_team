#! /usr/bin/env python3

from sports_team import SportsTeam
import unittest
from unittest import TestCase
from coach import Coach
import inspect


class TestCoach(TestCase):
    """ Class for Test Coach """

    def setUp(self):
        """ Setup unittest values and classes for testing and print log """
        self.coach1 = Coach('coach1', 'coach1@gmail.com', 6044468180, '01/01/2000', 9000, 'Coach')
        self.logPoint()

    def tearDown(self):
        """ Tear down values after use and print log """
        self.coach1 = None
        self.logPoint()

    def logPoint(self):
        """ Utility function used for module functions and class methods """
        current_test = self.id().split('.')[-1]
        calling_function = inspect.stack()[1][3]
        print('in %s - %s()' % (current_test, calling_function))

    def test_coach(self):
        """ Parameter validation for Coach Class """
        self.assertRaises(ValueError, Coach, 9, 'coach1@gmail.com', '6044468180', '01/01/2000', 9000, 'Coach')
        self.assertRaises(ValueError, Coach, 'coach1', 9, 6044468180, '01/01/2000', '9000', 'Coach')
        self.assertRaises(ValueError, Coach, 'coach1', 'coach1@gmail.com', 9, '01/01/2000', 9000, 'Coach')
        self.assertRaises(ValueError, Coach, 'coach1', '', 6044468180, '01/01/2000', '', 'Coach')
        self.assertRaises(ValueError, Coach, 'coach1', 'coach1@gmail.com', 6044468180, '01/01/2000', 9000, 0)

    def test_to_dict(self):
        """ Tests to dict method"""
        self.assertEqual(self.coach1.to_dict(), {
            "name": "coach1",
            "email": 'coach1@gmail.com',
            "phone number": 6044468180,
            "date of birth": '01/01/2000',
            "id": None,
            "salary": 9000,
            "position": 'Coach',
            "type": "Coach"
        })

    def test_copy(self):
        """ Tests Copy method """
        self.coach2 = Coach('coach2', 'coach2@gmail.com', 6044468180, '02/02/2000', 8000, 'Coach')
        self.coach2.copy(self.coach1)
        self.assertEqual(self.coach2.to_dict(), {
            "name": 'coach1',
            "email": 'coach1@gmail.com',
            "phone number": 6044468180,
            "date of birth": '01/01/2000',
            "id": None,
            "salary": 9000,
            "position": 'Coach',
            "type": "Coach"
        })


if __name__ == "__main__":
    unittest.main()
