import flask
from flask import request

app = flask.Flask(__name__)


# Example of video metadata
videos = [
    {
        'id': 1,
        'title': 'Video 1',
        'description': 'Description for video 1',
        'tags': ['tag1', 'tag2']
    },
    {
        'id': 2,
        'title': 'Video 2',
        'description': 'Description for video 2',
        'tags': ['tag3', 'tag4']
    }
]

# Get all videos
@app.route('/videos', methods=['GET'])
def get_videos():
    return {'videos': videos}


# Get specific video by id
@app.route('/videos/<int:id>', methods=['GET'])
def get_video(id):
    for video in videos:
        if video['id'] == id:
            return {'video': video}
    return {'error': 'Video not found'}, 404


# Add a new video
@app.route('/videos', methods=['POST'])
def add_video():
    video = request.get_json()
    videos.append(video)
    return {'message': 'Video added successfully'}


if __name__ == '__main__':
    app.run()
