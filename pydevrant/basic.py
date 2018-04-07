# Written by Sergio La Rosa (sergio.larosa89@gmail.com)
# and John Leonardo (hey@jdleo.me)
# Part of "pydevrant" package
# https://github.com/SergioLaRosa/pydevrant

import requests
import json
import time  # for timestamps in auth-related requests


class RantParser:

    def __init__(self):
        self._main_url = "https://www.devrant.io/api/"

    def get_user_id(self, user):
        '''
        Get user ID from username.
        '''
        self._url = self._main_url + "get-user-id?app=3&username=" + str(user)
        self._res = requests.get(self._url)
        return json.loads(self._res.text)

    def get_user_info(self, user_id):
        # Fetches detailed information about a user (profile, rants, favorites,
        # upvoted)
        self._url = self._main_url + "users/" + str(user_id) + "?app=3"
        self._res = requests.get(self._url)
        return json.loads(self._res.text)

    def get_rants(self, **kparams):
        '''
        Fetches a list of rants.
        Optional params:
        - sort [algo, top, recent]: sort the rants according to the parameter
        - limit: number of rants to fetch
        - skip: Skip the first N rants and fetch from there
        '''
        self._url = self._main_url + "devrant/rants?app=3"
        if "sort" in kparams:
            self._sort = kparams['sort']
            self._url += "&sort=" + str(self._sort)
        if "limit" in kparams:
            self._limit = kparams['limit']
            self._url += "&limit=" + str(self._limit)
        if "skip" in kparams:
            self._skip = kparams['skip']
            self._url += "&skip=" + str(self._skip)
        self._res = requests.get(self._url)
        return json.loads(self._res.text)

    def get_single_rant(self, rant_id):
        '''
        Fetches a single rant with comments
        '''
        self._url = self._main_url + "devrant/rants/" + str(rant_id) + "?app=3"
        self._res = requests.get(self._url)
        return json.loads(self._res.text)

    def search_rants(self, term):
        '''
        Fetches rants matching the search term
        '''
        self._url = self._main_url + "devrant/search?app=3&term=" + str(term)
        self._res = requests.get(self._url)
        return json.loads(self._res.text)

# Credits: auth class made by John Leonardo (thank you, John!)


class Auth:

    def login(self, email, password):
        '''
        Auths user and gets important user attributes
        '''
        self._url = "https://www.devrant.io/api/users/auth-token"
        data = {
            "app": 3,
            "username": email,
            "password": password,
            "plat": 3,
            "sid": time.time(),
            "seid": 6
        }
        self._res = requests.post(self._url, data=data)
        if json.loads(self._res.text)['success'] == False:
            return False
        self.uid = json.loads(self._res.text)['auth_token']['user_id']
        self.token_id = json.loads(self._res.text)['auth_token']['id']
        self.token_key = json.loads(self._res.text)['auth_token']['key']
        return True

    def vote(self, type, rant_id, value):
        '''
        Vote on a post or comment
        '''
        if type == "rant":
            self.voteUrl = "https://devrant.com/api/devrant/rants/" + \
                str(rant_id) + "/vote"
        elif type == "comment":
            self.voteUrl = "https://devrant.com/api/comments/" + \
                str(rant_id) + "/vote"
        data = {
            "app": 3,
            "token_id": self.token_id,
            "token_key": self.token_key,
            "user_id": self.uid,
            "plat": 3,
            "sid": time.time(),
            "seid": 155,
            "vote": value
        }
        if value == -1:
            # if user is downvoting, reason needs to be provided
            data["reason"] = 0
        self._res = requests.post(self.voteUrl, data=data)
        return json.loads(self._res.text)

    def post(self, body, tags, type):
        '''
        Make a post from user's account
        '''
        self.postUrl = "https://devrant.com/api/devrant/rants"
        data = {
            "app": 3,
            "rant": body,
            "tags": tags,
            "token_id": self.token_id,
            "token_key": self.token_key,
            "user_id": self.uid,
            "type": type
        }
        self._res = requests.post(self.postUrl, data=data)
        return json.loads(self._res.text)
