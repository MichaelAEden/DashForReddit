import os

import praw

class RedditClient():

    # TODO: declare app version constant.
    USER_AGENT = 'web:DashForReddit:1.0 (by /u/CanadaUDev)'

    # TODO: should this be a singleton?
    # TODO: are there any network requests made upon initializing the client?
    def __init__(self):
        # TODO: fail on app start-up if creds are missing.
        client_id = os.environ['CLIENT_ID']
        client_secret = os.environ['CLIENT_SECRET']

        self._reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=RedditClient.USER_AGENT
        )

    def get_subreddit_by_id(self, subreddit_id):
        # TODO: define subreddit model, based on Praw's subreddit model.
        # TODO: error handling.
        subreddit = self._reddit.subreddit(subreddit_id)

        return {
            'subreddit_id': subreddit_id,
            'description': subreddit.description
        }
