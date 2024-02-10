"""Process of downloading audio files and matching them with the texts"""

import os
import re
from path import Path
from typing import List, Union
import warnings
import wget
from tqdm import tqdm
import json
from primary_processing.text_processing import preprocess_corpus

CORPUS_PATH = Path('./corpus_maalula/')
TEXT_OUT_PATH = Path('./texts/')
AUDIO_LINKS_JSON = Path('./audio_links.json')
MATCHED_AUDIO_PATH = Path('./audio/')
UNMATCHED_AUDIO_PATH = Path('./unmathced audio/')


def rewrite_texts(texts_path: Path, out_path: Path) -> set:
    """
    Function preprocesses texts, moves them to a different folder and returns the set of their names
    :param texts_path: initial path with text files
    :param out_path: target folder
    :return: set of file names
    """
    texts_set = set()
    for file in texts_path.iterdir():
        file_path, file_extension = file.splitext()
        file_name = file_path.splitall()[-1]
        name = re.search(r'(?<=[A-ZḤČḲʕṢŠḲṬŽḎ][A-ZḤČḲʕṢŠḲṬŽḎ] )[\w\-, ]+\Z', file_name)

        if name is not None:
            new_name = name.group()
            text = file.open(encoding='utf-8').read()
            out_path.joinpath(new_name + '.txt').write_text(preprocess_corpus(text))
            texts_set.update([name.group()])
        else:
            warnings.warn(f'We did not find an appropriate name for file {file_name + "." + file_extension}')
    return texts_set


def match_and_download(audio_links_json: Path,
                       texts_set: set,
                       matched_audio_dir: Path,
                       unmatched_audio_dir: Path) -> List[Path]:
    """
    Function renames audio files, so they match text files and downloads them
    :param audio_links_json: path to json file with links to audio files
    :param texts_set: set of text filenames
    :param matched_audio_dir: path to folder with matching audio files
    :param unmatched_audio_dir: path to folder with not matching audio files
    :return: list of all downloaded files
    """
    audio_dct = json.load(audio_links_json.open(encoding='utf-8'))
    all_files = []
    for name, link in tqdm(audio_dct.items()):
        mapping = re.search(r'(?<=\d )[\w,\- ]+$', name)
        if mapping and mapping.group() in texts_set:
            new_name = mapping.group()
            audio_path = matched_audio_dir.joinpath(new_name + '.wav')
            texts_set.discard(new_name)
        else:
            audio_path = unmatched_audio_dir.joinpath(' '.join(re.findall(r'\w+', name)) + '.wav')

        if not audio_path.exists():
            wget.download(link, out=audio_path)
            all_files.append(audio_path)
        else:
            warnings.warn(f'File {audio_path} already exists')
    return all_files


if __name__ == '__main__':
    if not TEXT_OUT_PATH.exists():
        TEXT_OUT_PATH.mkdir()
    if not MATCHED_AUDIO_PATH.exists():
        MATCHED_AUDIO_PATH.mkdir()
    if not UNMATCHED_AUDIO_PATH.exists():
        UNMATCHED_AUDIO_PATH.mkdir()

    texts_set = rewrite_texts(CORPUS_PATH, TEXT_OUT_PATH)
    match_and_download(AUDIO_LINKS_JSON, texts_set, MATCHED_AUDIO_PATH, UNMATCHED_AUDIO_PATH)