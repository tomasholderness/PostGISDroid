# PostGISDroid - upload android location to PostGIS database
'''
PostGISDroid - script to upload android location to PostGIS database.

Copyright Tom Holderness & Newcastle University 2011.

Released under modified BSD license. See LICENSE.txt

version 1.1
'''

__version__ = "1.1"
__author__ = "Tom Holderness"

import android, time
import droidpg8000.dbapi as dbapi # The pg8000 module
 
droid = android.Android()
# Start a partial wakelock so script is active when screen is off.
droid.wakeLockAcquirePartial()
 
# Start location acquisition and give GPS 10s to acquire lock.
droid.startLocating()
print "Starting location acquisition (wait 10s)"
time.sleep(10)
 
# Start an infinite loop to acquire and transmit location.
while 1:
   loc = droid.readlocation()

   #Connect to the database and create a connection cursor.
   pwd = droid.dialogGetPassword("","Database password.")
   conn = dbapi.connect(host="0.0.0.0", user="user", password="pwd",
         database="dbname")
   cursor = conn.cursor()
   print "Connection database succesful."
	
      # Test for gps based location only (avoiding 'network' based location).
      if 'gps' in loc[1]:
 
      # Create an SQL INSERT statement, using well known text for geometry.
         datastr = "INSERT INTO droidtrack (id, provider, accuracy, altitude, \
speed, the_geom) VALUES (%s, %s, %s, %s, %s, ST_GeomFromText('POINT(%s %s)',4326));" % \
(str(loc[0]),"'"+str(loc[1]['gps']['provider'])+"'",str(loc[1]['gps']['accuracy']),\
str(loc[1]['gps']['altitude']),str(loc[1]['gps']['speed']),\
str(loc[1]['gps']['longitude']),str(loc[1]['gps']['latitude']))

      # Execute, commit and print data.
         cursor.execute(datastr)  
         conn.commit()
         print datastr

# Log location at 60s intervals
time.sleep(60)

# If loop exits, close connection and release wakelock.
cursor.close()
conn.close()
droid.wakeLockRelease()
