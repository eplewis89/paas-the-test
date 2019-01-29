from flask import Blueprint, make_response, jsonify, request
from app import app
from app.helpers import response

groups = Blueprint('groups', __name__)

# Declare the file location
file = "/etc/group"

# Return all the groups from /etc/groups
@groups.route('/groups/', methods=['GET'])
def getgroups():
    file_object = open(file, 'r')
    contents = {}

    for line in file_object:
        line = line.strip()
        fields = line.split(":")
        contents["name"] = fields[0]
        contents["gid"] = fields[2]
        contents["members"] = fields[3].split(',')
    
    file_object.close()

    return response('success', contents, 200)

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