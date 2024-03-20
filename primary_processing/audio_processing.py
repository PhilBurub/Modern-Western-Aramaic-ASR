"""A set of functions that help preprocess initial audio files"""
from moviepy.editor import VideoFileClip
import warnings
from typing import Union
from pathlib import Path
import librosa
import soundfile as sf


def get_new_path(current_path: Path) -> Path:
    """
    Returns unique path
    :param current_path: initial path
    :return: unique path based on the initial one
    """
    output_stem = current_path.stem
    idx = 0
    while current_path.with_stem(output_stem).exists():
        warnings.warn(f"File {current_path.with_stem(output_stem)} already exists")
        output_stem = current_path.stem + '_' + str(idx)
        idx += 1
    return current_path.with_stem(output_stem)


def video2audio(video_path: Path,
                audio_path: Union[Path, None] = None) -> Path:
    """
    Rewrites video file as audio
    :param video_path: path to video file
    :param audio_path: directory where new audiofile will be saved
    :return: path where new audiofile is saved
    """

    designed_path = audio_path.joinpath(video_path.stem + '.wav') if \
        audio_path is not None else video_path.with_suffix('.wav')
    output_path = get_new_path(designed_path)

    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(output_path)
    video.close()
    return output_path


def audio2wav(input_path: Path,
              destination_path: Union[Path, None] = None) -> Path:
    """
    Rewrites audio as .wav file
    :param input_path: path to audio file
    :param destination_path: directory where new audiofile will be saved
    :return: path where new audiofile is saved
    """
    designed_path = destination_path.joinpath(input_path.stem + '.wav') if \
        destination_path is not None else input_path.with_suffix('.wav')
    output_path = get_new_path(designed_path)
    audio, sr = librosa.load(input_path, sr=None)
    sf.write(output_path, audio, sr)
    return output_path
