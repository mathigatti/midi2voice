python2 generateSong/voice/musicXML.py
OUTPUT=$(curl -X POST -F 'SPKR_LANG=english' -F 'SPKR=4' -F 'SYNALPHA=0.55' -F 'VIBPOWER=1' -F 'F0SHIFT=0' -F  'SYNSRC=@generateSong/voice/musicXMLs/voice.xml' http://sinsy.sp.nitech.ac.jp/index.php | grep "lf0")
python2 generateSong/voice/sinsy.py $OUTPUT
python2 generateSong/voice/voiceTag.py


