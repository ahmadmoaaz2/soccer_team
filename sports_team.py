#! /usr/bin/env python3
from coach import Coach
from players import Player
from abstract_members import AbstractMember
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
import os
import json


class SportsTeam:
    """ Class to hold a sports team """
    def __init__(self, team_name, db_filename):
        """ Constructor for the team """
        self._validate_string("Database Filename", db_filename)
        self._db_filename = db_filename
        sql_engine = create_engine("sqlite:///" + db_filename, connect_args={'check_same_thread': False})
        Base.metadata.bind = sql_engine
        self._db = sessionmaker(bind=sql_engine)
        self._validate_string('Team Name', team_name)
        self._name = team_name

    def add(self, new_member):
        """ Assigns an id to each object and adds it to the database """
        self._validate_member_object("object in add()", new_member)
        session = self._db()
        session.add(new_member)
        session.commit()
        new_id = new_member.id
        session.close()
        return new_id

    def get(self, object_id):
        """ Returns an object based on id """
        self._validate_int("member id in get()", object_id)
        session = self._db()
        db_members = [
            session.query(Coach).filter(Coach.type == Coach.TYPE).filter(Coach.id == object_id).first(),
            session.query(Player).filter(Player.type == Player.TYPE).filter(Player.id == object_id).first()
        ]
        if db_members[0] is None and db_members[1] is None:
            raise ValueError("No course with that id")
        for member in db_members:
            if member is None:
                continue
            db_member = member
        session.close()
        return db_member

    def get_all(self):
        """ Returns all objects """
        session = self._db()
        members = [
            session.query(Coach).filter(Coach.type == Coach.TYPE).all(),
            session.query(Player).filter(Player.type == Player.TYPE).all()
        ]
        returned = []
        for member in members:
            for i in member:
                returned.append(i)
        session.close()
        return returned

    def get_all_by_type(self, member_type):
        """ Return all objects that match the given type """
        session = self._db()
        members = [
            session.query(Coach).filter(Coach.type == Coach.TYPE).all(),
            session.query(Player).filter(Player.type == Player.TYPE).all()
        ]
        returned = []
        for member in members:
            for i in member:
                if i.type == member_type:
                    returned.append(i)
        session.close()
        return returned

    def update(self, given_member):
        """ Updates and object with a new object based on ID """
        self._validate_member_object("object in update()", given_member)
        session = self._db()
        db_members = [
            session.query(Coach).filter(Coach.type == Coach.TYPE).filter(Coach.id == given_member.id).first(),
            session.query(Player).filter(Player.type == Player.TYPE).filter(Player.id == given_member.id).first()
        ]
        if db_members[0] is None and db_members[1] is None:
            raise ValueError("No existing course")
        for member in db_members:
            if member is None:
                continue
            db_member = member
        if given_member.type != db_member.type:
            session.close()
            self.delete(db_member.id)
            self.add(given_member)
            return
        db_member.copy(given_member)
        session.commit()
        session.close()

    def delete(self, object_id):
        """ Deletes member object based on id """
        self._validate_int("member id in delete()", object_id)
        session = self._db()
        db_member = session.query(AbstractMember).filter(AbstractMember.id == object_id).first()
        if db_member is None:
            raise ValueError("No existing course")
        session.delete(db_member)
        session.commit()
        session.close()

    def get_team_name(self):
        """ Getter for the team name """
        return self._name

    def set_team_name(self, name):
        """ Setter method for team name """
        self._validate_string("Team name", name)
        self._name = name

    @staticmethod
    def _validate_string(name, value):
        """ Validation for string inputs """
        if not isinstance(value, str):
            raise ValueError(name + ' must be a string')
        if value == '':
            raise ValueError(name + ' cannot be an empty string')

    @staticmethod
    def _validate_int(name, value):
        """ Validation for Integer """
        if not isinstance(value, int):
            raise ValueError(name + ' must be an integer')

    @staticmethod
    def _validate_member_object(name, value):
        """ Validation for member objects """
        if not isinstance(value, AbstractMember):
            raise ValueError(name + ' is not a member object')