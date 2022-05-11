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
    group_contents = []

    for line in file_object:
        line = line.strip()
        fields = line.split(":")
        
        group = {
            "name" : fields[0],
            "gid" : fields[2],
            "members" : fields[3].split(',')
        }

        group_contents.append(group)

    file_object.close()

    return jsonify(group_contents)

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
        return jsonify(group)

    return response('group not found', gid, 404)

@groups.route('/groups/query', methods=['GET'])
def querygroups():
    """
    Query all the groups in /etc/groups for some specific info
    :return:
    """
    req = request.args.to_dict()

    print(req)

    file_object = open(file, 'r')
    group_contents = []

    for line in file_object:
        line = line.strip()
        fields = line.split(":")
        
        group = {
            "name" : fields[0],
            "gid" : fields[2],
            "members" : fields[3].split(',')
        }

        add = True

        for x in req:
            if req[x] is None:
                add = False
                continue

            if len(group[x]) > 0:
                members = req[x].split(',')

                for m in members:
                    if m not in group[x]:
                        add = False
            elif group[x] != req[x]:
                add = False

        if add:
            group_contents.append(group)

    file_object.close()

    return jsonify(group_contents)