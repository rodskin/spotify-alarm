#!/bin/bash
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

playdate() {
   DATE=`date +"%H:%M"`
   #echo $DATE
   # get the time
   LANG='fr'
   python lib/google_tts.py $DATE $LANG
   mpg123 tmp/time.mp3
}