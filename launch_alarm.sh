#!/bin/bash
volume=1
sleep_volume_delay=5

rawurlencode() {
   local string="${1}"
   local strlen=${#string}
   local encoded=""

   for (( pos=0 ; pos<strlen ; pos++ )); do
      c=${string:$pos:1}
      case "$c" in
         [-_.~a-zA-Z0-9] ) o="${c}" ;;
         * ) printf -v o '%%%02x' "'$c"
      esac
     encoded+="${o}"
   done
   echo "${encoded}"
}

# get the time
LANG='fr'
TEXT=$( rawurlencode "Il est 9h15" )
echo $TEXT
hash="$(echo -n "$TEXT" | md5sum )"
API="http://translate.google.com/translate_tts?ie=UTF-8&tl=$LANG&q=$TEXT"
UA="Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36"
wget -o /dev/null --user-agent="$UA" -O "~/spotify-alarm/tmp/$hash.mp3" "$API"
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







