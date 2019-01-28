# paas-the-test
### PaaS - /etc/passwd and /etc/groups REST API

This service is written using python and is made for testing purposes only.

I hold no responsibility over how you use it. This software is licensed under the __[GNU General Public License (GPL)](https://www.gnu.org/licenses/gpl-3.0.en.html)__.

# API Methods
### GET /users

Return a list of all users on the system, as defined in the /etc/passwd file.

Example Response:

    [
        {
            "name": "root",
            "uid": 0,
            "gid": 0,
            "comment": "root",
            "home": "/root",
            "shell": "/bin/bash"
        },
        {
            "name": "dwoodlins",
            "uid": 1001,
            "gid": 1001,
            "comment": "",
            "home": "/home/dwoodlins",
            "shell": "/bin/false"
        }
    ]

### GET /users/query[?name=&lt;nq>][&uid=&lt;uq>][&gid=&lt;gq>][&comment=&lt;cq>][&home=&lt;hq>][&shell=&lt;sq>]

Return a list of users matching all of the specified query fields. The bracket notation indicates that any of the following query parameters may be supplied:

+ name
+ uid
+ gid
+ comment
+ home
+ shell

*Only exact matches are supported.*

Example Query: GET /users/query?shell=%2Fbin%2Ffalse

Example Response:

    [
        {
            "name": "dwoodlins",
            "uid": 1001,
            "gid": 1001,
            "comment": "",
            "home": "/home/dwoodlins",
            "shell": "/bin/false"
        }
    ]

### GET /users/&lt;uid>

Return a single user with &lt;uid>. Return 404 if &lt;uid> is not found.

Example Response:

    {
        "name": "dwoodlins",
        "uid": 1001,
        "gid": 1001,
        "comment": "",
        "home": "/home/dwoodlins",
        "shell": "/bin/false"
    }

### GET /users/&lt;uid>/groups

Return all the groups for a given user.

Example Response:

    [
        {
            "name": "docker",
            "gid": 1002,
            "members": [
                "dwoodlins"
            ]
        }
    ]

### GET /groups

Return a list of all groups on the system, a defined by /etc/group.

Example Response:

    [
        {
            "name": "_analyticsusers",
            "gid": 250,
            "members": [
                "_analyticsd’,"_networkd","_timed"
            ]
        },
        {
            "name": "docker", 
            "gid": 1002, 
            "members": []
        }
    ]

### GET /groups/query[?name=&lt;nq>][&gid=&lt;gq>][&member=&lt;mq1>[&member=&lt;mq2>][&...]]

Return a list of groups matching all of the specified query fields. The bracket notation indicates that any of the following query parameters may be supplied:

+ name
+ gid
+ member (repeated)

Any group containing all the specified members should be returned, i.e. when query members are a subset of group members.

Example Query: GET /groups/query?member=_analyticsd&member=_networkd

Example Response:

    [
        {
            "name": "_analyticsusers",
            "gid": 250,
            "members": [
                "_analyticsd’,
                "_networkd",
                "_timed"
            ]
        }
    ]

### GET /groups/&lt;gid>

Return a single group with &lt;gid>. Return 404 if &lt;gid> is not found.

Example Response:

    {
        "name": "docker",
        "gid": 1002,
        "members": [
            "dwoodlins"
        ]
    }