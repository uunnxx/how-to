import flask
from flask import request


app = flask.Flask(__name__)


# Example comment data
comments = [
    {
        'id': 1,
        'video_id': 1,
        'comment': 'Comment 1 for video 1',
        'username': 'user1'
    },
    {
        'id': 2,
        'video_id': 2,
        'comment': 'Comment 2 for video 2',
        'username': 'user2'
    }
]


# Get all comments for a specific video
@app.route('/comments', methods=['GET'])
def get_comments():
    video_id = request.args.get('video_id')
    video_comments = [
        comment for comment in comments
        if comment['video_id'] == int(video_id)
    ]

    return {'comments': video_comments}


# Add a new comment
@app.route('/comments', methods=['POST'])
def add_comment():
    comment = request.get_json()
    comments.append(comment)

    return {'message': 'Comment added successfully'}


if __name__ == '__main__':
    app.run()



