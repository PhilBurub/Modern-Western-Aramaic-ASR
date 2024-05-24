from transformers import pipeline
import warnings
from pathlib import Path
import librosa
import argparse
from time import time
import torch


def getargs():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-i', '--input_path'
    )

    parser.add_argument(
        '-o', '--output_path', required=False
    )

    parser.add_argument(
        '-c', '--chunk_length', type=int, default=25
    )

    parser.add_argument(
        '-s', '--stride_length', nargs=2, type=int, default=(5, 5)
    )

    return parser.parse_args()


def main():
    print('Configuring the model...')
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore')
        pipe = pipeline("automatic-speech-recognition", model="pburub/wav2vec2-xls-r-300m-mwa-maaloula")

    args = getargs()

    print('Reading the file...')
    audio, sr = librosa.load(args.input_path, sr=None)
    if sr != 16_000:
        audio = librosa.resample(audio, orig_sr=sr, target_sr=16_000)

    print('Processing the file...')
    start = time()
    text = pipe(audio, chunk_length_s=args.chunk_length, stride_length_s=args.stride_length)['text']
    total_time = time() - start

    name = Path(args.input_path).stem + '.txt'
    out_path = Path(args.output_path) / name if args.output_path else Path(args.input_path).with_suffix('.txt')
    out_path.write_text(text, encoding='utf-8')
    print(f'Done! Your file was processed in {round(total_time)}s')


if __name__ == '__main__':
    main()
