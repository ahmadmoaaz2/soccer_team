#! /usr/bin/env python3
from abstract_members import AbstractMember
import re
import datetime
from sqlalchemy import Column, Integer, String


class Player(AbstractMember):
    """ Class for Player """
    TYPE = "Player"

    jersey_number = Column(Integer)

    def __init__(self, name, email, phone_number, date_of_birth, jersey_number, position):
        """ Constructor for the Player Class"""
        self.__validate_player_position(position)
        super().__init__(name, email, phone_number, date_of_birth, Player.TYPE, position)
        self.__validate_integer('Jersey number', jersey_number)
        self.jersey_number = jersey_number

    def copy(self, new_member):
        """ Copy Attributes Method """
        self.id = new_member.id
        self.name = new_member.name
        self.email = new_member.email
        self.phone_number = new_member.phone_number
        self.date_of_birth = new_member.date_of_birth
        self.type = new_member.type
        self.position = new_member.position
        self.jersey_number = new_member.jersey_number

    def to_dict(self):
        """ Converter of class object to dictionary object in json dumps string form"""
        return {
            "name": self.name,
            "email": self.email,
            "phone number": self.phone_number,
            "date of birth": self.date_of_birth,
            "id": self.id,
            "jersey number": self.jersey_number,
            "position": self.position,
            "type": self.TYPE
        }

    @staticmethod
    def __validate_string(name, value):
        """ Validation for string inputs """
        if not isinstance(value, str):
            raise ValueError(name + ' must be a string')
        if value == '':
            raise ValueError(name + ' cannot be an empty string')
        if name == 'email' and len(re.findall(r'[\w]+[@][\w]+\.[\w]+', value)) < 1:
            raise ValueError("Email must be a valid email")
        if name == 'date of birth':
            try:
                datetime.datetime.strptime(value, '%d/%m/%Y')
            except ValueError:
                raise ValueError("date of birth should be in format ##/##/####")

    @staticmethod
    def __validate_integer(name, value):
        if not isinstance(value, int):
            raise ValueError(name + ' must be an integer')
        if name == 'Jersey number' and value not in range(1, 20):
            raise ValueError("Jersey number must be in the range 1-20")

    @staticmethod
    def __validate_phone_number(value):
        if not isinstance(value, int) or len(str(value)) != 10:
            raise ValueError("phone number must be a 10 digit integer")

    @staticmethod
    def __validate_player_position(value):
        """ Validation method for player position input """
        if not isinstance(value, str):
            raise ValueError("Position of player must be a string")
        if value.lower() != "goalkeeper" and value.lower() != "defender" and value.lower() != "midfield" and value.lower() != "wing" and value.lower() != "forward" :
            raise ValueError("Player position must be one of the following:\n 'goalkeeper'\n'defender'\n'midfield'\n'wing'\n'forward'")
