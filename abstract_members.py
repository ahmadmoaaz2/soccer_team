#! /usr/bin/env python3
import re
import datetime
from sqlalchemy import Column, Integer, String
from base import Base


class AbstractMember(Base):
    """ Abstract class for members of a soccer """
    __tablename__ = 'sports_team'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    phone_number = Column(Integer, nullable=False)
    type = Column(String(10), nullable=False)
    position = Column(String(30), nullable=False)
    date_of_birth = Column(String(30), nullable=False)

    def __init__(self, name, email, phone_number, date_of_birth, member_type, position):
        """ Not Implemented constructor that is meant to be polymorphed in child classes """
        self.__validate_string('coach name', name)
        self.__validate_string('email', email)
        self.__validate_phone_number(phone_number)
        self.__validate_string('date of birth', date_of_birth)
        self.__validate_string('type', member_type)
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.type = member_type
        self.position = position
        self.id = None

    def copy(self, new_member):
        """ Copy method Unimplemented """
        raise NotImplementedError()

    def to_dict(self):
        """ Converter of class object to dictionary object (unimplemented)"""
        raise NotImplementedError()

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
                raise ValueError("date of birth should be in format %d/%m/%Y")

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
    def __validate_coach_position(value):
        """ Validation for coach position input """
        if value.lower() != "coach" and value.lower() != "assistant coach" and value.lower() != 'head coach':
            raise ValueError("Position parameter for coach should be either 'coach', 'assistant coach' or 'head coach'")

    @staticmethod
    def __validate_player_position(value):
        """ Validation method for player position input """
        if value.lower() != "goalkeeper" and value.lower() != "defender" and value.lower() != "midfield" and value.lower() != "wing" and value.lower() != "forward":
            raise ValueError("Player position must be one of the following:\n 'goalkeeper'\n'defender'\n'midfield'\n'wing'\n'forward'")
