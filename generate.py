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

def _generate_phoneme_xml(phonemes):
    return '<PRON SYM="{phonemes}"/>'.format(phonemes=phonemes.replace('&', '&amp;'))


config = _load_config()
voice = tts.sapi.Sapi()

voice.set_voice(config['voice'])
voice.set_rate(int(config['rate']))
voice.set_volume(int(config['volume']))

reader = csv.reader(_read_transcript_lines())

flag_xml = 8
flag_not_xml = 16

for row in reader:
    cols = len(row)
    sapi_input = _generate_phoneme_xml(row[2]) if cols > 2 else row[1]
    sapi_flags = flag_xml if cols > 2 else flag_not_xml
    voice.create_recording('output/' + row[0] + '.wav', sapi_input, sapi_flags)