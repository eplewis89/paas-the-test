from flask import Blueprint, make_response, jsonify
from app import app
from app.helpers import response

groups = Blueprint('groups', __name__)

@groups.route('/groups/', methods=['GET'])
def getgroups():
    """
    Return all the groups in /etc/groups
    :return:
    """

    return response('success', '', 200)