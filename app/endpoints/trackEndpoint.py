from flask import abort, request, jsonify, make_response
from .. import app
from .. import database

@app.route('/v1/track/all', methods=['GET'])
def getAllTracks():
    return jsonify(database.getAllTracks())

@app.route('/v1/track/id/<int:track_id>', methods=['GET'])
def getTrackById(track_id):
    return jsonify(database.getTrackById(track_id))

@app.route('/v1/queue/all', methods=['GET'])
def getAllQueues():
    return jsonify(database.getAllQueues())

@app.route('/v1/queue/id/<int:queue_id>', methods=['GET'])
def getQueueById(queue_id):
    return jsonify(database.getQueueByIdWithTracks(queue_id))
