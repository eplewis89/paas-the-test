from flask import Blueprint, make_response, jsonify, request
from app import app
from app.helpers import response

users = Blueprint('users', __name__)

# Declare the file location
user_file = "/etc/passwd"
group_file = "/etc/group"

# Return all the users from /etc/passwd
@users.route('/users/', methods=['GET'])
def getusers():
    file_object = open(user_file, 'r')
    user_contents = []

    for line in file_object:
        line = line.strip()
        fields = line.split(":")
        
        user = {
            "name" : fields[0],
            "uid" : fields[2],
            "gid" : fields[3],
            "comment" : fields[4],
            "home" : fields[5],
            "shell" : fields[6]
        }

        user_contents.append(user)

    file_object.close()

    if (len(user_contents) > 0):
        return jsonify(user_contents)
        
    return response('no users found', '', 404)

# Return a single user by user id from /etc/passwd
@users.route('/users/<uid>', methods=['GET'])
def getuser(uid):
    found = False
    user = {}

    file_object = open(user_file, 'r')

    for line in file_object:
        line = line.strip()
        fields = line.split(":")
        user_id = int(fields[2])

        if user_id == int(uid):
            found = True
            user = {
                "name" : fields[0],
                "uid" : fields[2],
                "gid" : fields[3],
                "comment" : fields[4],
                "home" : fields[5],
                "shell" : fields[6]
            }
            
            break

    file_object.close()

    if (found):
        return jsonify(user)
        
    return response('user not found', uid, 404)

@users.route('/users/<uid>/groups', methods=['GET'])
def getusergroups(uid):
    """
    Return a single user's groups by user id from /etc/users
    :return:
    """
    user_found = False
    groups = []

    file_object = open(user_file, 'r')

    for line in file_object:
        line = line.strip()
        fields = line.split(":")
        user_id = int(fields[2])

        if user_id == int(uid):
            groups = fields[3]
            user_found = True
            break

    file_object.close()

    if not user_found:
        return response('user not found', uid, 404)

    if len(groups) == 0:
        return response('no user groups found', uid, 404)
    
    found = False

    group_data = []

    file_object = open(group_file, 'r')

    for line in file_object:
        line = line.strip()
        fields = line.split(":")
        group_id = int(fields[2])

        if str(group_id) in groups:
            group = {
                "name" : fields[0],
                "gid" : fields[2],
                "members" : fields[3].split(',')
            }
            
            group_data.append(group)

    file_object.close()

    if len(group_data) > 0:
        return jsonify(group_data)

    return response('no user groups found', uid, 404)

@users.route('/users/query', methods=['GET'])
def queryusers():
    """
    Query all the users in /etc/users for some specific info
    :return:
    """
    req = request.args.to_dict()

    user_contents = []

    file_object = open(user_file, 'r')

    for line in file_object:
        line = line.strip()
        fields = line.split(":")
        user_id = int(fields[2])

        user = {
            "name" : fields[0],
            "uid" : fields[2],
            "gid" : fields[3],
            "comment" : fields[4],
            "home" : fields[5],
            "shell" : fields[6]
        }

        add = True
            
        for x in req:
            if user[x] != req[x]:
                add = False
        
        if add:
            user_contents.append(user)

    file_object.close()

    if (len(user_contents) > 0):
        return jsonify(user_contents)
        
    return response('no users found', req, 404)