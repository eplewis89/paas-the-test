from flask import Blueprint, make_response, jsonify
from app import app

groups = Blueprint('groups', __name__)

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

@groups.route('/groups/', methods=['GET'])
def getgroups():
    """
    Return all the groups in /etc/groups
    :return:
    """

    return response('success', '', 200)