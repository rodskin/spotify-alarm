#!/usr/bin/env python
# encoding: utf-8
import sys
import gtts

datetime = "Il est " + sys.argv[1]
lang = sys.argv[2]
tts = gtts.gTTS(text=datetime, lang=lang)
tts.save("tmp/time.mp3")