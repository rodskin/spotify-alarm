#!/bin/bash
# @TODO : add day time for cron
# @TODO : add file conf for playlists
volume=1
sleep_volume_delay=5
CURRENT_DIR=`pwd`
echo $CURRENT_DIR

source lib/functions.sh

DATE=`date +"%H:%M"`
#echo $DATE
# get the time
LANG='fr'
python lib/google_tts.py $DATE $LANG
exit
TEXT=$( rawurlencode "Il est $DATE" )
echo $TEXT

API="http://translate.google.com/translate_tts?ie=UTF-8&tl=$LANG&q=$TEXT"
UA="Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36"
wget -o /dev/null --user-agent="$UA" -O "/tmp/time.mp3" "$API"
#aplay "/tmp/$hash.mp3"
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

# get the time
TEXT=$( rawurlencode "Il est 9h15" )
API="http://translate.google.com/translate_tts?ie=UTF-8&tl=$LANG&q=$TEXT"







