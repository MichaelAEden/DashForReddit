from flask import Flask, Blueprint, request, render_template, send_from_directory

from clients.reddit import RedditClient

subreddit_blueprint = Blueprint("subreddit", __name__)


@subreddit_blueprint.route('/<subreddit_id>', methods=['GET'])
def subreddit(subreddit_id):
    if request.method == 'GET':
        reddit_client = RedditClient()
        subreddit = reddit_client.get_subreddit_by_id(subreddit_id)
        return subreddit
