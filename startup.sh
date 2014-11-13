wget -O /root/attach_volume.py http://pastebin.com/raw.php?i=2URnuebR
/usr/bin/python /root/attach_volume.py

mount /dev/sdb /mnt/permalearn

su ec2-user -c "/home/ec2-user/permalearn/depp.sh"

#comment