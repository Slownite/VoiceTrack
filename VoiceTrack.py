from dotenv import load_dotenv
from pyannote.audio import Pipeline
from transformers import pipeline
import os
import pathlib
from argparse import ArgumentParser

def get_transcription(file: pathlib.Path):
    asr = pipeline("automatic-speech-recognition",
                   model="openai/whisper-small",
                   return_timestamps=True)
    result = asr(str(file))['chunks']
    return result

def get_speaker(key, file: pathlib.Path):
    pipeline = Pipeline.from_pretrained(
        "pyannote/speaker-diarization-3.1",
        use_auth_token=key)
    diarization = pipeline(str(file))
    return diarization

def get_match(transcription, diarization):
    final_output = []
    for chunk in transcription:
        text = chunk["text"]
        start = chunk["timestamp"][0]
        end = chunk["timestamp"][1]

        for turn in diarization.itertracks(yield_label=True):
            turn_start = turn[0].start
            turn_end = turn[0].end
            label = turn[2]
            if turn_start <= start <= turn_end or turn_start <= end <= turn_end:
                speaker = label
                break

        final_output.append(f"[{speaker}] {text}")
    return final_output

def main():
    load_dotenv()
    key = os.getenv("HUGGINGFACE")
    argument = ArgumentParser()
    argument.add_argument("file", type=pathlib.Path, help="input a wav file to transcript")
    argument.add_argument("--output","-o", help="output file for the transcript", required=False, type=pathlib.Path)
    args = argument.parse_args()
    transcription = get_transcription(args.file)
    speakers = get_speaker(key, args.file)
    output = get_match(transcription, speakers)
    if args.output:
        with open(args.output, 'w') as file:
            file.write("\n".join(output))
    else:
        for line in output:
            print(line)

if __name__ == '__main__':
    main()
