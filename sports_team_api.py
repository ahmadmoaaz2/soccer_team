#! /usr/bin/env python3
from flask import Flask, request
from sports_team import SportsTeam
from players import Player
from coach import Coach
import json

app = Flask(__name__)
sports_team = SportsTeam("Soccer Team", 'teams.sqlite')


@app.route('/sports_team/member', methods=['POST'])
def add_member():
    """ Adds a member to the team """
    content = request.json
    try:
        if not("name" in content and "email" in content and "phone number" in content and "date of birth" in content and("salary" in content or "jersey number" in content) and "position" in content and "type" in content and isinstance(content, dict)):
            raise ValueError("Invalid Object (not a dictionary object or missing required keys)")
        if content["type"].lower() == "coach":
            member = Coach(
                content["name"],
                content["email"],
                content["phone number"],
                content["date of birth"],
                content["salary"],
                content["position"]
            )
        if content["type"].lower() == "player":
            member = Player(
                content["name"],
                content["email"],
                content["phone number"],
                content["date of birth"],
                content["jersey number"],
                content["position"]
            )
        returned = sports_team.add(member)
        response = app.response_class(
            status=200,
            response=str(returned),
            mimetype='application/json'
        )
    except ValueError as e:
        response = app.response_class(
            status=400,
            response=str(e)
        )
    except KeyError as e:
        response = app.response_class(
            status=400,
            response="Key Error: Wrong Attribute for type, missing" + str(e)
        )
    return response


@app.route('/sports_team/member/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    """ Updates a member on the team based on the id provided """
    content = request.json
    try:
        if sports_team.get(member_id) is None:
            response = app.response_class(
                status=404,
                response="Error 404 ID NOT FOUND"
            )
            return response
        if not ("name" in content and "email" in content and "phone number" in content and "date of birth" in content and ("salary" in content or "jersey number" in content) and "position" in content and "type" in content and isinstance(content, dict)):
            raise ValueError("Invalid Object (not a dictionary object or missing required keys)")
        if content["type"].lower() == "coach":
            member = Coach(
                content["name"],
                content["email"],
                content["phone number"],
                content["date of birth"],
                content["salary"],
                content["position"]
            )
        if content["type"].lower() == "player":
            member = Player(
                content["name"],
                content["email"],
                content["phone number"],
                content["date of birth"],
                content["jersey number"],
                content["position"]
            )
        member.id = member_id
        sports_team.update(member)
        response = app.response_class(
            status=200
        )
    except ValueError as e:
        response = app.response_class(
            status=400,
            response=str(e)
        )
    return response


@app.route('/sports_team/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    """ Deletes a member from the team """
    try:
        if sports_team.get(member_id) is None:
            response = app.response_class(
                status=404,
                response="Error 404 ID NOT FOUND"
            )
            return response
        sports_team.delete(member_id)
        response = app.response_class(
            status=200
        )
    except ValueError as e:
        response = app.response_class(
            status=400,
            response=str(e)
        )
    return response


@app.route('/sports_team/member/<int:member_id>', methods=['GET'])
def get_member_id(member_id):
    """ Gets a member from team based on member id """
    try:
        if sports_team.get(member_id) is None:
            response = app.response_class(
                status=404,
                response="Error 404 ID NOT FOUND"
            )
            return response
        response_body = sports_team.get(member_id).to_dict()
        response = app.response_class(
            status=200,
            response=json.dumps(response_body),
            mimetype='application/json'
        )
    except ValueError as e:
        response = app.response_class(
            status=400,
            response=str(e)
        )
    return response


@app.route('/sports_team/member/all', methods=['GET'])
def get_member_all():
    """ Gets all the members from the team """
    try:
        response_list = [k.to_dict() for k in sports_team.get_all()]
        response = app.response_class(
            status=200,
            response=json.dumps(response_list),
            mimetype='application/json'
        )
    except ValueError as e:
        response = app.response_class(
            status=400,
            response=str(e)
        )
    return response


@app.route('/sports_team/member/all/<member_type>', methods=['GET'])
def get_member_type(member_type):
    """ Gets all the members that match a certain type from the team """
    try:
        if member_type.lower() != 'coach' and member_type.lower() != 'player':
            raise ValueError('Type is invalid')
        response_list = [k.to_dict() for k in sports_team.get_all() if k.type.lower() == member_type.lower()]
        if len(response_list) == 0:
            raise ValueError('No matching entities found for type')
        response = app.response_class(
            status=200,
            response=json.dumps(response_list),
            mimetype='application/json'
        )
    except ValueError as e:
        response = app.response_class(
            status=400,
            response=str(e)
        )
    return response


if __name__ == '__main__':
    app.run()
