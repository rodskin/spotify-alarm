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