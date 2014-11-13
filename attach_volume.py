import os
import sys
import time
import boto.ec2
import urllib

instanceid = urllib.urlopen('http://169.254.169.254/latest/meta-data/instance-id').read()
azone = urllib.urlopen('http://169.254.169.254/latest/meta-data/placement/availability-zone').read()

conn=boto.ec2.connect_to_region("us-east-1")

if azone=='us-east-1c':
	volume = 'vol-6dc6cd74'
elif azone=='us-east-1d':
	volume = 'vol-4d630405'
else:
	print "where the hell am I? I'm outta here"

try:
 conn.attach_volume(volume, instanceid, '/dev/sdb')
except:
 print "Could not mount PermaLearn volume:", sys.exc_info()[0]
 exit()

i=0
while i<10 and not os.path.exists('/dev/sdb'):
 print 'waiting for drive to mount'
 time.sleep(3)
 i+=1