# Audiofile aufnehmen
sudo sox -d recording.wav

# Audiofile transformieren stereo nach mono
sox recording.wav recording.l.wav remix 1
sox recording.wav recording.r.wav remix 2

# Audiofile abspielen
play [filename]                 # Teil von SoX
afplay recording.r.wav          # Mac Bordmitel

# transform into single channel 16k wav file which works for Speech API
sox new.wav -b 16 recording_curbed.wav channels 1 rate 16k

