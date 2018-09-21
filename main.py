import boto3
import base64


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
        "contentType": spoken_text["ContentType"],
        "audioContent": base64.b64encode(spoken_text["AudioStream"].read())
    }
