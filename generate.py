#!/usr/bin/env python3

from os.path import dirname, realpath
import csv
import configparser
from tts import sapi

def _load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['default']

def _read_transcript_lines():
    req_file_path = '%s/transcripts.csv' % dirname(realpath(__file__))
    return open(req_file_path, 'r')

def _generate_phoneme_xml(phonemes, phoneme_set='sapi'):
    if phoneme_set == 'sapi':
        valid_phonemes = {'&', '-', '!', '?', ',', '.', '_', 'aa', 'ae', 'ah', 'ao', 'aw', 'ax', 'ay', 'b', 'ch', 'd', 'dh', 'eh', 'er', 'ey', 'f', 'g', 'h', 'ih', 'iy', 'jh', 'k', 'l', 'm', 'n', 'ng', 'ow', 'oy', 'p', 'r', 's', 'sh', 't', 'th', 'uh', 'uw', 'v', 'w', 'y', 'z', 'zh'}
        current_phonemes = set(map(lambda x:x.lower(), phonemes.split()))
        invalid_phonemes = current_phonemes.difference(valid_phonemes)

        if len(invalid_phonemes) > 0:
            print(invalid_phonemes)
            return ''

    word_phonemes = phonemes.split('&')
    ssml = ''
    for word_phoneme in word_phonemes:
        ssml += '<phoneme alphabet="sapi" ph="{phonemes}"></phoneme>'.format(phonemes=word_phoneme.strip().lower())

    return '<speak version="1.0" xmlns="https://www.w3.org/2001/10/synthesis" xml:lang="en-US">{ssml}</speak>'.format(ssml=ssml)



config = _load_config()
voice = sapi.Sapi()

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
    if sapi_input != '':
        voice.create_recording('output/' + row[0] + '.wav', sapi_input, sapi_flags)