from flask import Blueprint, make_response, jsonify
from app import app
from app.helpers import response

users = Blueprint('users', __name__)

@users.route('/users/', methods=['GET'])
def getusers():
    """
    Return all the users in /etc/users
    :return:
    """

    return response('success', '', 200)