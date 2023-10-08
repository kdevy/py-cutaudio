# py-cutaudio
Simple audio file cutting command.

## Installation
```
pip install -r requirements.txt
```
Please install ffmpeg and put it in PATH.

https://github.com/BtbN/FFmpeg-Builds/releases

## Example
If there is no option, it will be cut to the end every 10 seconds.

The file will be output to ./cutaudio_[YYYYMMDDHHMMSS]/ in the current directory.
```
python .\cutaudio.py .\sample.wav
```
When cutting audio files every 20 seconds (total of 30 files):
```
python .\cutaudio.py .\sample.wav -m 30 -i 20
```
You can specify the output format with the -e option.
```
python .\cutaudio.py .\sample.wav -m 30 -i 20 -e mp3
```