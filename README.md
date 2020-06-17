# win-sapi-tts-audio-file-generator
using Win SpVoice Interface (SAPI) with python to generate audio files


# Set-up

```bash
$ pip install git+https://github.com/jetfontanilla/tts
```
# Configuration

edit config.ini to change to a different Voice Bank, or change other TTS parameters

# Running
create a CSV file with the unique ID as the first parameter and the transcript to run as the second.
it also supports phoneme-based text-to-speech by adding the phonemes in the 3rd column ([link for phonemes](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/ms717239(v=vs.85)))


the run this command

```bash
$ pip python generator.py
```

generated audiom files will be in the output folder