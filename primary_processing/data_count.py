"""A set of functions that help calculate the amount of data"""
import librosa
from tqdm import tqdm
from path import Path


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
    total = 0
    for textfile in tqdm(text_dir.iterdir()):
        with open(textfile, 'r', encoding='utf-8') as f:
            total += len(f.read().split())
    return total
