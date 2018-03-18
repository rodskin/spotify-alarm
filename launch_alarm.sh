#!/bin/bash
# @TODO : add day time for cron
# @TODO : add file conf for playlists
volume=1
sleep_volume_delay=5
CURRENT_DIR=`pwd`
echo $CURRENT_DIR

source lib/functions.sh

playdate
exit

exit

mpc clear
mpc random 1
mpc volume ${volume}
mpc add spotify:user:icelandairwaves:playlist:3dNCFy3Q9d6LtGZLWT0c2O
mpc play

sleep ${sleep_volume_delay}
for volume in {1..40}
do
   mpc volume ${volume}
   sleep ${sleep_volume_delay}
done