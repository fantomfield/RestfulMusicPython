import json, sqlite3
#
# AddQueueLists,
# just id's of songs

config = {
    'databaseLocation' : '/Users/henri/Projects/GIT/RestfulMusicPython/app/database/',
    'databaseName' : 'databaseV2.db'
}

cursor = None
conn = None

def connectTodb():
    global cursor, conn
    dbFile = config['databaseLocation'] + config['databaseName']
    print(dbFile)
    conn = sqlite3.connect(dbFile, check_same_thread=False)
    cursor = conn.cursor()

    # cursor.execute("PRAGMA table_info(tracks)")

# def jsonResponse(item):
#     return json.dumps(item,separators=(',',':'))

def formatTrack(track):
    return {
        'track_id': track[0],
        'name': track[1],
        'artist': track[2],
        'file_name': track[3],
        'length':track[4]
    }

def formatQueue(queue):
    return {
        'queue_id': queue[0],
        'queue_name': queue[1],
        'track_ids': queue[2].split(',')
    }

def addTrackInfoToQueue(queue):

    queueWithTrackInfo = queue

    trackIds = queue['queue']['track_ids']

    trackList = []

    for trackId in trackIds :
        track = getTrackById(trackId)
        trackList.append(track['track'])

    queueWithTrackInfo['queue']['tracks'] = trackList
    return queueWithTrackInfo

def getTrackById(id):
    global conn, cursor
    if(conn is None or cursor is None):
        connectTodb()

    track_id = (id,)
    cursor.execute('SELECT * FROM tracks WHERE track_id=?', track_id)

    track = cursor.fetchone()

    return { 'track':formatTrack(track) }

def getAllTracks():
    global conn, cursor
    if(conn is None or cursor is None):
        connectTodb()

    return {'tracks': [formatTrack(track) for track in cursor.execute('SELECT * FROM tracks')]}

def defaultQueue():
    return getAllTracks()['tracks']

def getAllQueues():
    global conn, cursor
    if(conn is None or cursor is None):
        connectTodb()

    cursor.execute('SELECT * FROM queues')
    return {'queues': [formatQueue(queue) for queue in cursor.execute('SELECT * FROM queues')]}

def getQueueById(id):
    global conn, cursor
    if(conn is None or cursor is None):
        connectTodb()

    queue_id = (id,)
    cursor.execute('SELECT * FROM queues WHERE queue_id=?', queue_id)
    queue = cursor.fetchone()

    return { 'queue': formatQueue(queue)}

def getQueueByIdWithTracks(id):
    return addTrackInfoToQueue(getQueueById(id))

if __name__ == '__main__':
    #print(getTrackById(1))
    # task = [1,2,3,{'4': 5, '6': 7}]
    # print (jsonResponse(task))
    # print (jsonResponse(getAllTracks()))
    # print (jsonResponse(getTrackById(1)))
    # print (jsonResponse(getTrackById(0)))
    # track = getTrackById(1)
    # print (track['valid_id'])

    print(getAllQueues())
    # print(getTrackById(3))
    # Queue = getQueueById(1)
    # print(Queue)
    # print(addTrackInfoToQueue(Queue))
    # print()
