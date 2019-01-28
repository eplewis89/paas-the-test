from flask import Blueprint, make_response, jsonify
from app import app

users = Blueprint('users', __name__)

def response(status, message, code):
    """
    Helper method to make a http response
    :param status: Status message
    :param message: Response message
    :param code: Response status code
    :return: Http Response
    """
    return make_response(jsonify({
        'status': status,
        'message': message
    })), code

@users.route('/users/', methods=['GET'])
def getusers():
    """
    Return all the users in /etc/users
    :return:
    """

    return response('success', '', 200)