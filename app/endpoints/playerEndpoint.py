from flask import abort, request, jsonify, make_response
from .. import player
from .. import app

@app.route('/v1/player/play', methods=['GET'])
def play():
    player.play()
    return "playing"

@app.route('/v1/player/play', methods=['POST'])
def playTrack():
    if not request.json or not player.validTrack(request.json):
        abort(400)
    else:
        player.play(request.json)
        return "playing"

@app.route('/v1/player/next', methods=['GET'])
def playNext():
    return jsonify(player.playNext());

@app.route('/v1/player/previous', methods=['GET'])
def playPrevious():
    return jsonify(player.playPrevious());

@app.route('/v1/player/pause', methods=['GET'])
def pause():
    player.pause()
    return "paused"

@app.route('/v1/player/stop', methods=['GET'])
def stop():
    player.stop()
    return "stopped"

@app.route('/v1/player/playing', methods=['GET'])
def playing():
    return jsonify({'playing': player.playing(), 'currentSong': player.queue[player.currentSong]})

@app.route('/v1/player/queue', methods=['GET'])
def getQueue():
    return jsonify({'currentSong':player.currentSong ,'queue' : player.queue})

@app.route('/v1/player/queue', methods=['POST'])
def loadQueue():
    return jsonify(player.loadQueue(request.json))
