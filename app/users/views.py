from flask import Blueprint, make_response, jsonify, request
from app import app
from app.helpers import response

users = Blueprint('users', __name__)

# Declare the file location
file = "/etc/passwd"

# Return all the users from /etc/passwd
@users.route('/users/', methods=['GET'])
def getusers():
    file_object = open(file, 'r')
    contents = []

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

        contents.append(user)

    file_object.close()

    return response('success', contents, 200)

# Return a single user by user id from /etc/passwd
@users.route('/users/<uid>', methods=['GET'])
def getuser(uid):
    found = False
    user = {}

    file_object = open(file, 'r')

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
        return response('user found', user, 200)
        
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