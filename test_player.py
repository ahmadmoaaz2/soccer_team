#! /usr/bin/env python3

from sports_team import SportsTeam
import unittest
from unittest import TestCase
from players import Player
import inspect


class TestPlayer(TestCase):
    """ Class for Test Player """

    def setUp(self):
        """ Setup unittest values and classes for testing and print log """
        self.player1 = Player('player1', 'player1@gmail.com', 6044468180, '01/02/2000', 1, 'forward')
        self.player2 = Player('player2', 'player2@gmail.com', 6044468181, '01/02/2001', 2, 'goalkeeper')
        self.player3 = Player('player3', 'player3@gmail.com', 6044468182, '01/02/2002', 3, 'defender')
        self.player4 = Player('player4', 'player4@gmail.com', 6044468183, '01/02/2003', 4, 'midfield')
        self.player5 = Player('player5', 'player5@gmail.com', 6044468184, '01/02/2004', 5, 'wing')
        self.logPoint()

    def tearDown(self):
        """ Tear down values after use and print log """
        self.player1 = None
        self.player2 = None
        self.player3 = None
        self.player4 = None
        self.player5 = None
        self.logPoint()

    def logPoint(self):
        """ Utility function used for module functions and class methods """
        current_test = self.id().split('.')[-1]
        calling_function = inspect.stack()[1][3]
        print('in %s - %s()' % (current_test, calling_function))

    def test_players(self):
        """ Tests the parameter validation for Players """
        self.assertRaises(ValueError, Player, 'player5', 'player5@gmail.com', '6044468184', '01/02/2004', 5, 'wing')
        self.assertRaises(ValueError, Player, 'player5', 'player5@gmail.com', '6044468184', '01/02/2004', '5', 'wing')
        self.assertRaises(ValueError, Player, '', 'player5@gmail.com', 6044468184, '01/02/2004', 5, 'wing')
        self.assertRaises(ValueError, Player, 'player5', '', '6044468184', '01/02/2004', 5, 'wing')
        self.assertRaises(ValueError, Player, 'player5', 'player5@gmail.com', 6044468184, '', 5, 'wing')
        self.assertRaises(ValueError, Player, 'player5', 'player5@gmail.com', 6044468184, '01/02/2004', 5, '')
        self.assertRaises(ValueError, Player, 'player5', 'player5@gmail.com', '', '01/02/2004', 5, 'wing')

    def test_to_dict(self):
        """ Tests to dict method"""
        self.assertEqual(self.player1.to_dict(), {
            "name": "player1",
            "email": 'player1@gmail.com',
            "phone number": 6044468180,
            "date of birth": '01/02/2000',
            "id": None,
            "jersey number": 1,
            "position": 'forward',
            "type": "Player"
        })

    def test_copy(self):
        """ Tests Copy method """
        self.player6 = Player('player1', 'player1@gmail.com', 6044468180, '01/02/2000', 1, 'forward')
        self.player1.copy(self.player6)
        self.assertEqual(self.player1.to_dict(), {
            "name": 'player1',
            "email": 'player1@gmail.com',
            "phone number": 6044468180,
            "date of birth": '01/02/2000',
            "id": None,
            "jersey number": 1,
            "position": 'forward',
            "type": "Player"
        })


if __name__ == "__main__":
    unittest.main()

