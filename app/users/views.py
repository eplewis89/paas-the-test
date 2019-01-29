from flask import Blueprint, make_response, jsonify, request
from app import app
from app.helpers import response

users = Blueprint('users', __name__)

@users.route('/users/', methods=['GET'])
def getusers():
    """
    Return all the users from /etc/users
    :return:
    """

    return response('success', '', 200)

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