# pydevrant
Unofficial Python wrapper for the public [devRant](https://www.devrant.io) API.

Based on the unofficial wrapper made by "danillouz" ([here](https://github.com/danillouz/devrant)) and API docs from "abhn" ([here](https://github.com/abhn/devRant-Unofficial-API-Doc)). 

__From the official site__: _devRant is a fun community for developers to share and bond over their successes and frustrations with code, tech, and life as a programmer. devRant is built by just one developer (devRant: [@dfox](https://www.devrant.io/users/dfox) Twitter: [@dfoxinator](https://twitter.com/DFoxinator)) and one designer (devRant: [@trogus](https://www.devrant.io/users/trogus) Twitter: [@tim_rogus](https://twitter.com/tim_rogus)) working on this project nights and weekends._

## Installation
Install using [pip](https://pip.pypa.io/en/stable/quickstart/)

`pip install pydevrant`

## List of features
Currently, you can:

- Get user ID
- Get rants
- Get a rant with comments
- Search rants
- Get user profile
- Login with username/password
- Post a rant
- Vote a rant
- Vote a comment

(Note: search results are JSON-formatted data)

## Example
**Post a rant**

```
from pydevrant import *

client = Auth()
user = client.login("USERNAME", "PASSWORD")

#first argument is body (string)
#second argument is tags (string, make sure comma seperated)
#third argument is type (int, 1 for rant, 5 for collab)

client.post("this is my rant, do you like it?", "swift, react, js", 1)
```
**Vote a rant/comment**

```
#first argument is type (rant/comment)
#second argument is RANT_ID
#third argument is value. (+1 for upvote, -1 for downvote)
#(can only be +1 or -1. server rejects requests if any other data)

client.vote("rant", 1292812, +1)    #for voting on a rant
client.vote("comment", 1372121, +1)    #for voting on a comment
```
**Find the top rants but limit the results to just one**

```Python
from pydevrant import *
from pprint import pprint #just for nice output on terminal

elem = RantParser()
result = elem.get_rants(sort="top",limit=1)

pprint(result)
```

The output will be something like this (some parts removed for brevity):
```
{'news': {'action': 'grouprant',
          'body': 'Bad data loss story?',
          'footer': "Add tag 'wk98' to your rant",
          'headline': 'Weekly Group Rant',
          'height': 100,
          'id': 132,
          'type': 'intlink'},
 'rants': [{'attached_image': '',
            'created_time': 1474486614,
            'edited': True,
            'id': 194632,
            'num_comments': 155,
            'rc': 1,
            'rt': 1,
            'score': 2672,
            'tags': [],
            'text': 'It appears his main client had gone nuts with him because '
                    'they wanted him to make an internet toolbar (think '
                    "Ask.com) and he politely informed them toolbars doesn't "
                    "really exist anymore and it wouldn't work on things like "
                    'modern browsers or mobile devices.\n'
                    ....
                    ',
            'user_avatar': {'b': 'f99a66',
                            'i': 'v-18_c-3_b-3_g-m_9-1_1-2_16-13_3-5_8-2_7-2_5-2_12-2_6-11_10-9_2-42_15-11_11-4_4-2.jpg'},
            'user_avatar_lg': {'b': 'f99a66',
                               'i': 'v-18_c-1_b-3_g-m_9-1_1-2_16-13_3-5_8-2_7-2_5-2_12-2_6-11_10-9_2-42_15-11_11-4_4-2.png'},
            'user_id': 103918,
            'user_score': 4909,
            'user_username': 'peaam',
            'vote_state': 0}],
 'set': '5ac3b0a97b094',
 'settings': [],
 'success': True,
 'wrw': 98}
```

