from flask import Blueprint, make_response, jsonify, request
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

@groups.route('/groups/<gid>', methods=['GET'])
def getgroup(gid):
    """
    Return a single group by group id from /etc/groups
    :return:
    """

    if (int(gid) > 0):
        return response('group found', gid, 200)
    return response('group not found', gid, 404)

@groups.route('/groups/query', methods=['GET'])
def querygroups():
    """
    Query all the groups in /etc/groups for some specific info
    :return:
    """

    req = request.args.to_dict()

    return response('success', req, 200)