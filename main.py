#! /usr/bin/env python
import os
import sys

parent_dir = os.path.abspath(os.path.dirname(__file__))
vendor_dir = os.path.join(parent_dir, 'lib')

sys.path.append(vendor_dir)

from lib import boto3

def main(aws_access_key_id, aws_secret_access_key, region_name, text, lexicon_names=None, sample_rate=None, speech_mark_types=None, text_type=None, language_code=None, output_format='mp3', voice_id='Emma'):

    polly = boto3.client(
        'polly',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name
    )

    params = {
        "Text": text,
        "OutputFormat": output_format,
        "VoiceId": voice_id
    }

    if lexicon_names:
        params.update({
            "LexiconNames": lexicon_names
        })
    
    if sample_rate:
        params.update({
            "SampleRate": sample_rate
        })
    
    if speech_mark_types:
        params.update({
            "SpeechMarkTypes": speech_mark_types
        })
    
    if text_type:
        params.update({
            "TextType": text_type
        })
    
    if language_code:
        params.update({
            "LanguageCode": language_code
        })

    spoken_text = polly.synthesize_speech(
        **params
    )

    return {
        "content-type": spoken_text["ContentType"],
        "content": spoken_text["AudioStream"].read()
    }
