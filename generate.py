#!/usr/bin/env python3

from os.path import dirname, realpath
import csv
import configparser
import tts.sapi

def _load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['default']

def _read_transcript_lines():
    req_file_path = '%s/transcripts.csv' % dirname(realpath(__file__))
    return open(req_file_path, 'r')


config = _load_config()
voice = tts.sapi.Sapi()

voice.set_voice(config['voice'])
voice.set_rate(int(config['rate']))

reader = csv.reader(_read_transcript_lines())
for row in reader:
    voice.create_recording('output/' + row[0] + '.wav', row[1])