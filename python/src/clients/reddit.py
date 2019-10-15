import os

import praw

class RedditClient():

    _CLIENT_ID = os.environ['CLIENT_ID']
    _CLIENT_SECRET = os.environ['CLIENT_SECRET']
    # TODO: declare app version constant.
    _USER_AGENT = 'web:DashForReddit:1.0 (by /u/CanadaUDev)'

    # TODO: should this be a singleton?
    # TODO: are there any network requests made upon initializing the client?
    def __init__(self):
        self._reddit = praw.Reddit(
            client_id=RedditClient._CLIENT_ID,
            client_secret=RedditClient._CLIENT_SECRET,
            user_agent=RedditClient._USER_AGENT
        )

    def get_subreddit_by_id(self, subreddit_id):
        # TODO: define subreddit model, based on Praw's subreddit model.
        # TODO: error handling.
        subreddit = self._reddit.subreddit(subreddit_id)

        return {
            'subreddit_id': subreddit_id,
            'description': subreddit.description
        }
