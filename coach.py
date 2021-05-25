#! /usr/bin/env python3
from abstract_members import AbstractMember
import datetime
import re
from sqlalchemy import Column, Integer, String


class Coach(AbstractMember):
    """ Class for Coaches """
    TYPE = "Coach"

    salary = Column(Integer)

    def __init__(self, name, email, phone_number, date_of_birth, salary, position="Coach"):
        """ Constructor for the Coach class """
        self.__validate_coach_position(position)
        super().__init__(name, email, phone_number, date_of_birth, Coach.TYPE, position)
        self.__validate_integer('salary', salary)
        self.salary = salary

    def copy(self, new_member):
        """ Copy Attributes Method """
        self.id = new_member.id
        self.name = new_member.name
        self.email = new_member.email
        self.phone_number = new_member.phone_number
        self.date_of_birth = new_member.date_of_birth
        self.type = new_member.type
        self.position = new_member.position
        self.salary = new_member.salary

    def to_dict(self):
        """ Converter of class object to dictionary object in json dumps string form """
        return {
            "name": self.name,
            "email": self.email,
            "phone number": self.phone_number,
            "date of birth": self.date_of_birth,
            "id": self.id,
            "salary": self.salary,
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
    def __validate_coach_position(value):
        """ Validation for coach position input """
        if not isinstance(value, str):
            raise ValueError("Position of coach must be a string")
        if value.lower() != "coach" and value.lower() != "assistant coach" and value.lower() != 'head coach':
            raise ValueError("Position parameter for coach should be either 'coach', 'assistant coach' or 'head coach'")
