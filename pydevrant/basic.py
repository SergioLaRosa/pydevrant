import requests
import json


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
