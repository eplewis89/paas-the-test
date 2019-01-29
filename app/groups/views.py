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
    contents = []

    for line in file_object:
        line = line.strip()
        fields = line.split(":")
        
        group = {
            "name" : fields[0],
            "gid" : fields[2],
            "members" : fields[3].split(',')
        }

        contents.append(group)

    file_object.close()

    return response('success', contents, 200)

# Return a single group by group id from /etc/groups
@groups.route('/groups/<gid>', methods=['GET'])
def getgroup(gid):
    found = False
    group = {}

    file_object = open(file, 'r')

    for line in file_object:
        line = line.strip()
        fields = line.split(":")
        group_id = int(fields[2])

        if group_id == int(gid):
            found = True
            group = {
                "name" : fields[0],
                "gid" : fields[2],
                "members" : fields[3].split(',')
            }
            
            break

    file_object.close()

    if (found):
        return response('group found', group, 200)
        
    return response('group not found', gid, 404)

@groups.route('/groups/query', methods=['GET'])
def querygroups():
    """
    Query all the groups in /etc/groups for some specific info
    :return:
    """

    req = request.args.to_dict()

    return response('success', req, 200)