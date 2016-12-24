import json
from app import database
from pygame import mixer
from time import sleep

currentSong = 0

options = {
 'loop':True,
 'trackPath':'/Users/henri/Projects/GIT/RestfulMusicPython/app/tracks/',
 'audioExtension':'.wav'
}

queue = None

# When player startes up default queue from config is loaded and also wheter to repeat
# if there is no queue then just play all songs from database
def initilzation():
    global queue
    queue = database.defaultQueue()
    mixer.init()
    trackLocation = getTrackLocation(queue[currentSong])
    mixer.music.load(trackLocation)
    mixer.music.play()
    mixer.music.pause()

def getTrackLocation(track):
    return options['trackPath'] + track['file_name'] + options['audioExtension']

def playing():
    time = mixer.music.get_pos()
    sleep(0.01)
    if(time == mixer.music.get_pos()):
        return False
    else :
        return True

def stop():
    mixer.music.stop()

def play(track=None):

    if track is not None:
        trackLocation = getTrackLocation(track)
        mixer.music.load(trackLocation)
        mixer.music.play()
    elif(not playing()):
        trackLocation = getTrackLocation(queue[0])
        mixer.music.load(trackLocation)
        mixer.music.play()
        trackLocation = getTrackLocation(queue[1])
        mixer.music.queue(trackLocation)
        # mixer.music.play()
        # mixer.music.unpause()

def pause():
    mixer.music.pause()

def validTrack(track):
    if((type(track) is dict)):
        if('track_id' in track and 'file_name' in track):
            if((type(track['track_id']) is int) & (type(track['file_name']) is str)):
                return True
    return False

def loadQueue(trackArray):
    global currentSong, queue
    if(type(trackArray) is list):
        if(len(trackArray) > 0):
            for track in trackArray:
                if(validTrack(track) == True):
                    currentSong = 0
                    queue = trackArray
                    return True
        else:
            return False
    else:
        return False

def playNext():
    global currentSong, queue
    currentSong = currentSong+1
    if(currentSong == len(queue)):
        currentSong = 0

    songToPlay=queue[currentSong]
    play(songToPlay)
    return songToPlay

def playPrevious():
    global currentSong, queue
    currentSong = currentSong- 1
    if(currentSong < 0 ):
        currentSong = len(queue) - 1

    songToPlay=queue[currentSong]
    play(songToPlay)
    return songToPlay

#
# def



# Queue()
#     return current song q json,
#             count:int
#             current_song:int
#             Repeat:boolean
#             Song_List
#
# AddQueue(Song)
#     Adds song to Queue
#     Returns json Queue
#
# removeQueue(Song)
#     removes song from queue
#     Returns new Queue / fail song not in queue / only song in queue stops playing
#
# SaveQueue(name)
#     Saves current queue to db with
#     returns 'Saved queue'/error
#
# Queue(queue)
#     Changes queue
#     Returns Queue
#
# Volume
#     returns Current Volume
#
# Volume(int)
#     sets Volume
#     Returns new volume/Error
#
# NextSong()
#     Plays nextSongInQueue
#
# PrevSong()
#     Plays previous Song
#
# RestartSong()
#     Plays Current song from begining
#     return true/false

if __name__ == '__main__':
    initilzation()
    print(getTrackLocation(defaultQueue[0]))
    print("valid track : ")
    print(validTrack(defaultQueue[0]))
    print("invalid string ")
    print(validTrack({"file_name":21, "track_id":2}))
    print("not json ")
    print(validTrack(True))
    play(defaultQueue[0])
    print(loadQueue(defaltQueue))
    print(queue)
    print(pause())
    while mixer.music.get_busy():
        sleep(5)
        if(playing()):
            pause()
        else:
            play()
        print(playing())
