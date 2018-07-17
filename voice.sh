lyrics=$1
midi=$2
tempo=$3

musescore $midi -o inputs/musicXMLs/voice.musicxml
python2 voiceConverter.py $lyrics inputs/musicXMLs/voice.musicxml $tempo

OUTPUT=$(curl -X POST -F 'SPKR_LANG=english' -F 'SPKR=4' -F 'SYNALPHA=0.55' -F 'VIBPOWER=1' -F 'F0SHIFT=0' -F  'SYNSRC=@inputs/musicXMLs/voice.xml' http://sinsy.sp.nitech.ac.jp/index.php | grep "lf0")
python2 sinsy.py $OUTPUT
python2 voiceTag.py


