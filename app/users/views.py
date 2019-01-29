from flask import Blueprint, make_response, jsonify, request
from app import app
from app.helpers import response

users = Blueprint('users', __name__)

# Declare the file location
file = "/etc/passwd"

# Return all the users from /etc/users
@users.route('/users/', methods=['GET'])
def getusers():
    file_object = open(file, 'r')
    contents = {}

    for line in file_object:
        line = line.strip()
        fields = line.split(":")
        contents["name"] = fields[0]
        contents["uid"] = fields[2]
        contents["gid"] = fields[3]
        contents["comment"] = fields[4]
        contents["home"] = fields[5]
        contents["shell"] = fields[6]
    
    file_object.close()

    return response('success', contents, 200)

@users.route('/users/<uid>', methods=['GET'])
def getuser(uid):
    """
    Return a single user by user id from /etc/users
    :return:
    """
    
    if (int(uid) > 0):
        return response('user found', uid, 200)
    return response('user not found', uid, 404)

@users.route('/users/<uid>/groups', methods=['GET'])
def getusergroups(uid):
    """
    Return a single user's groups by user id from /etc/users
    :return:
    """

    if (int(uid) > 0):
        return response('user groups found', uid, 200)
    return response('user not found', uid, 404)

@users.route('/users/query', methods=['GET'])
def queryusers():
    """
    Query all the users in /etc/users for some specific info
    :return:
    """

    req = request.args.to_dict()

    return response('success', req, 200)