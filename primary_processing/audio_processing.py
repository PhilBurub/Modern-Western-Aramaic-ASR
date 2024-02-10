"""A set of functions that help preprocess initial audio files"""

from moviepy.editor import VideoFileClip
import warnings
from typing import Union
from path import Path
import librosa
import soundfile as sf


def get_new_audiofile_path(current_path: Path) -> Path:
    """
    Returns unique path for .wav file
    :param current_path: initial path
    :return: unique path based on the initial one
    """
    output_path = current_path
    idx = 0
    while (output_path + '.wav').exists():
        warnings.warn(f"File {output_path + '.wav'} already exists")
        output_path = current_path + '_' + str(idx)
        idx += 1
    output_path += '.wav'
    return output_path


def video2audio(video_path: Path,
                audio_path: Union[Path, None] = None) -> Path:
    """
    Rewrites video file as audio
    :param video_path: path to video file
    :param audio_path: directory where new audiofile will be saved
    :return: path where new audiofile is saved
    """
    file_path, _ = video_path.splitext()
    file_path_splitted = file_path.splitall()
    designed_path = audio_path.joinpath(file_path_splitted[-1]) if \
        audio_path is not None else file_path
    output_path = get_new_audiofile_path(designed_path)

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
    file_path, _ = input_path.splitext()
    file_path_splitted = file_path.splitall()
    designed_path = destination_path.joinpath(file_path_splitted[-1]) if \
        destination_path is not None else file_path
    output_path = get_new_audiofile_path(designed_path)
    audio, sr = librosa.load(input_path, sr=None)
    sf.write(output_path, audio, sr)
    return output_path
