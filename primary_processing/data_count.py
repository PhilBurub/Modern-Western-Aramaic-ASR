"""A set of functions that help calculate the amount of data"""
import librosa
from tqdm import tqdm
from pathlib import Path
import argparse


def count_seconds(audio_dir: Path) -> int:
    """
    The function calculates total duration of audio files in path
    :param audio_dir: path to the directory
    :return: duration in seconds
    """
    total = 0
    for audiofile in tqdm(audio_dir.iterdir()):
        audio, sr = librosa.load(audiofile, sr=None)
        total += audio.shape[0] // sr
    return total


def count_words(text_dir: Path) -> int:
    """
    The function calculates total number of tokens of text files in path
    :param text_dir: path to the directory
    :return: amount of tokens
    """
    file_lens = [len(text_file.read_text(encoding='utf-8').split()) for text_file in text_dir.iterdir()]
    return sum(file_lens)


def main(audio_dir: Path,
         text_dir: Path):
    """
    The function calculates total amount of data in path
    :param audio_dir: path to the directory with audio files
    :param text_dir: path to the directory with texts
    """
    print(f'Total audio length: {round(count_seconds(audio_dir)/3600, 2)} hours\n'
          f'Total texts length: {round(count_words(text_dir)/1000, 2)}k tokens')

if __name__=='__main__':
    parser = argparse.ArgumentParser('Data Counter')
    parser.add_argument('-a', '--audio', help='Audio files directory')
    parser.add_argument('-t', '--texts', help='Texts directory')

    arguments = parser.parse_args()
    audio_dir = Path(arguments.audio)
    text_dir = Path(arguments.texts)
    main(audio_dir, text_dir)
