## Windows SAPI Text-to-Speech / Phoneme-to-Speech Audio File Generator
using Win SpVoice Interface (SAPI) with python to generate audio files


## Configuration

edit config.ini to change to a different Voice Bank, or change other TTS parameters

## Generating Audio
create a CSV file with the unique ID as the first parameter and the transcript to run as the second.
it also supports phoneme-based text-to-speech by adding the phonemes in the 3rd column ([link for supported phonemes](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/ms717239(v=vs.85)))
if phonemes are provided, it will ignore the transcript parameter


to generate the audio files, run this command

```bash
$ python generator.py
```

generated audio files will be in the output folder
