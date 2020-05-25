#!/usr/bin/env python3

from os.path import dirname, realpath
import csv
import tts.sapi


def _read_transcript_lines():
    req_file_path = '%s/transcripts.csv' % dirname(realpath(__file__))
    return open(req_file_path, 'r')



voice = tts.sapi.Sapi()
voice.set_voice('Zira')
voice.set_rate(-5)

reader = csv.reader(_read_transcript_lines())
for row in reader:
    voice.create_recording('output/' + row[0] + '.wav', row[1])