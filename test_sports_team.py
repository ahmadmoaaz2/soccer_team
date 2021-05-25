#! /usr/bin/env python3
from sports_team import SportsTeam
from coach import Coach
from players import Player
import unittest
import inspect
from unittest import TestCase
import os
from sqlalchemy import create_engine
from base import Base


class TestSportsTeam(TestCase):
    """ Class for Test Sports Team """
    def setUp(self):
        """ Setup unittest values and classes for testing and print log """
        engine = create_engine('sqlite:///test_sports_teams.sqlite')

        Base.metadata.create_all(engine)
        Base.metadata.bind = engine

        self.team = SportsTeam('teamname1', 'test_sports_teams.sqlite')
        self.player1 = Player('player1', 'player1@gmail.com', 6044468180, '01/02/2000', 1, 'forward')
        self.player2 = Player('player2', 'player2@gmail.com', 6044468180, '01/02/2000', 1, 'forward')
        self.logPoint()

    def tearDown(self):
        """ Tear down values after use and print log """
        self.team = None
        self.player1 = None
        self.player2 = None
        os.remove('test_sports_teams.sqlite')
        self.logPoint()

    def logPoint(self):
        """ Utility function used for module functions and class methods """
        current_test = self.id().split('.')[-1]
        calling_function = inspect.stack()[1][3]
        print('in %s - %s()' % (current_test, calling_function))

    def test_sports_team(self):
        """ Parameter validation for the SportsTeam class """
        self.assertRaises(ValueError, SportsTeam, 3, 'file.txt')
        self.assertRaises(ValueError, SportsTeam, 'teamname1', 1)
        self.assertRaises(ValueError, SportsTeam, 'teamname1', None)

    def test_add(self):
        """ Test for add function """
        self.team.add(self.player1)
        all_player = self.team.get_all()
        self.assertEqual(len(all_player), 1)

    def test_get(self):
        """ Test for get method """
        playerid = self.team.add(self.player1)
        retrievedplayer = self.team.get(playerid)
        self.assertEqual(retrievedplayer.name, "player1")
        self.assertEqual(retrievedplayer.email, "player1@gmail.com")

    def test_get_all(self):
        """ Test for get_all() """
        self.team.add(self.player2)
        self.team.add(self.player1)
        allplayers = self.team.get_all()
        self.assertEqual(len(allplayers), 2)

    def test_get_all_by_type(self):
        """ Tests the Get all by type method """
        self.player1 = Player('player1', 'player1@gmail.com', 6044468180, '01/02/2000', 1, 'forward')
        self.player2 = Player('player2', 'player2@gmail.com', 6044468180, '02/02/2000', 1, 'Wing')

        playerid = self.team.add(self.player2)
        playerid2 = self.team.add(self.player1)

        allplayers = self.team.get_all_by_type("Player")
        self.assertEqual(len(allplayers), 2)

    def test_update(self):
        """ Tests the Update method """
        self.player2 = Player('player1', 'player1@gmail.com', 6044468180, '01/02/2000', 1, 'forward')
        playerid = self.team.add(self.player2)

        retrievedplayer = self.team.get(playerid)
        self.assertEqual(retrievedplayer.name, "player1")

        retrievedplayer.name = "player12"
        self.team.update(retrievedplayer)

        retrievenew = self.team.get(playerid)
        self.assertEqual(retrievenew.name, "player12")

    def test_delete(self):
        """ Tests the delete method """
        self.team.add(self.player1)
        memberid = self.team.add(self.player2)
        self.team.delete(memberid)
        self.assertEqual(len(self.team.get_all()), 1)

    def test_get_team_name(self):
        """ Tests the Get Team Name method """
        self.assertEqual(self.team.get_team_name(), 'teamname1')

    def test_set_team_name(self):
        """ Tests the Set Team Name method """
        self.assertRaises(ValueError, self.team.set_team_name, 88)
        self.team.set_team_name('GG')
        self.assertEqual(self.team.get_team_name(), 'GG')


if __name__ == "__main__":
    unittest.main()
