# PostGISDroid - upload android location to PostGIS database
'''
PostGISDroid - script to upload android location to PostGIS database.

Released under BSD license

Copyright Tom Holderness 2011.

version 1.0
'''

import android, time, dbapi
droid = android.Android()

conn = dbapi.connect(host="192.168.0.8", user="postgres", password="Apollo11", database="android")
cursor = conn.cursor()
cursor.execute("SELECT id, provider, accuracy, altitude, speed FROM droidtrack")
data = cursor.fetchall()
cursor.close()
conn.close()

print data

exit(0)

