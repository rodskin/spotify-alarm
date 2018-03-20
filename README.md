# Alarm clock with Spotify

## Installation

### Needs
- mpg123
- python gTTS
- Spotify Premium account
- mopidy
- mpc

### Mopidy

#### Install
```
wget -q -O - https://apt.mopidy.com/mopidy.gpg | sudo apt-key add -
sudo wget -q -O /etc/apt/sources.list.d/mopidy.list https://apt.mopidy.com/jessie.list
sudo apt-get update
sudo apt-get install mopidy
apt-cache search mopidy
sudo apt-get install mopidy-spotify
```

edit `/etc/mopidy/mopidy.conf` with the `sample/mopidy.conf`


#### get spotify IDs
https://www.mopidy.com/authenticate/#spotify

## CRON
In order to use a crontab for the script, you need to make it executable

`chmod -x launch_alarm.py`

and create a crontab `crontab -e`

`15 7 * * 1-5 /home/user/spotify-alarm/launch_alarm.py`

## @TODO
- check connexion and play classic mp3 instead of spotify playlist
- add weather API for temperature, weather, wind direction / speed (par coded in openweather.py)
- find how to use the led while the script is playing (sleep makes it "freeze")