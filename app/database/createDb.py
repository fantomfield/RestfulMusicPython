import sqlite3

def createTrackTable(dbName):
    conn = sqlite3.connect(dbName)
    crusor = conn.cursor()
    crusor.execute("CREATE TABLE tracks (track_id int PRIMARY KEY, name text NOT NULL, artist text, file_name text NOT NULL, length real)")
    conn.commit()
    conn.close()

def createQueueTable(dbName):
    conn = sqlite3.connect(dbName)
    crusor = conn.cursor()
    crusor.execute("CREATE TABLE queues (queue_id int PRIMARY_KEY, queue_name text NOT NULL, track_ids text NOT NULL)")
    conn.commit()
    conn.close()

def populateQueueTable(dbName):
    conn = sqlite3.connect(dbName)
    crusor = conn.cursor()
    crusor.execute("INSERT INTO queues VALUES (1, 'Default', '1,2,3')")
    conn.commit()
    conn.close()

def insertRecords(dbName):
    conn = sqlite3.connect(dbName)
    crusor = conn.cursor()
    crusor.execute("INSERT INTO tracks VALUES (1, 'Chase The Sun','Planet Funk','Planet_Funk-Chase_the_Sun', 0.0)")
    crusor.execute("INSERT INTO tracks VALUES (2, 'Tuk Spot','Clyde Carson','Clyde_Carson-Tuk_Spot', 0.0)")
    crusor.execute("INSERT INTO tracks VALUES (3, 'Cant get u outta my mind','Mall Grab','mall_grab_-_can_39_t_get_u_outta_my_mind', 0.0)")
    conn.commit()
    conn.close()

def createDB():
    db = 'databaseV2.db'
    createTrackTable(db)
    insertRecords(db)
    createQueueTable(db)
    populateQueueTable(db)


if __name__ == '__main__':
    createDB()
    # insertRecords('databaseV1.db')
