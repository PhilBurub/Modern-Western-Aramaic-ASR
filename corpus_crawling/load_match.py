"""Process of downloading audio files and matching them with the texts"""
import re
from pathlib import Path
from typing import List
import argparse
import warnings
import wget
from tqdm import tqdm
import json
from primary_processing.text_processing import preprocess_corpus


def rewrite_texts(texts_path: Path, out_path: Path) -> set:
    """
    Function preprocesses texts, moves them to a different folder and returns the set of their names
    :param texts_path: initial path with text files
    :param out_path: target folder
    :return: set of file names
    """
    texts_set = set()
    for text_file in texts_path.iterdir():
        name = re.search(r'(?<=[A-ZḤČḲʕṢŠḲṬŽḎ][A-ZḤČḲʕṢŠḲṬŽḎ] )[\w\-, ]+\Z', text_file.stem)

        if name is not None:
            new_name = name.group()
            text = text_file.read_text(encoding='utf-8')
            out_path.joinpath(new_name + '.txt').write_text(preprocess_corpus(text))
            texts_set.update([name.group()])
        else:
            warnings.warn(f'We did not find an appropriate name for file {text_file.name}')
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


def main(corpus_path: Path,
         audio_links_json: Path,
         text_out_path: Path,
         matched_audio_path: Path,
         unmatched_audio_path: Path):
    """
    Function converts files from the corpus to the uniform format, downloads audio files and sorts them into matched
    und unmatched ones
    :param corpus_path: path to the corpus of texts
    :param audio_links_json: path to the json file containing links to audio files
    :param text_out_path: path to the target text directory
    :param matched_audio_path: path to the target directory for audio files that have corresponding texts
    :param unmatched_audio_path: path to the target directory for audio files that do not have corresponding texts
    """
    if not text_out_path.exists():
        text_out_path.mkdir()
    if not matched_audio_path.exists():
        matched_audio_path.mkdir()
    if not unmatched_audio_path.exists():
        unmatched_audio_path.mkdir()

    texts_set = rewrite_texts(corpus_path, text_out_path)
    match_and_download(audio_links_json, texts_set, matched_audio_path, unmatched_audio_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Aramaic Corpora Files Match')
    parser.add_argument('-c', '--corpus', help='Path to the corpus texts')
    parser.add_argument('-a', '--audio', help='Path to the json file with links to audio files')
    parser.add_argument('-t', '--texts', help='Target path to processed texts', required=False)
    parser.add_argument('-m', '--matched', help='Target path to matched audio files', required=False)
    parser.add_argument('-u', '--unmatched', help='Target path to unmatched audio files', required=False)

    arguments = parser.parse_args()
    corpus_path = Path(arguments.corpus)
    audio_links_json = Path(arguments.audio)
    text_out_path = Path(arguments.texts) if arguments.texts else corpus_path.parent.joinpath('preprocessed_texts')
    matched_audio_path = Path(arguments.matched) if arguments.matched else \
        audio_links_json.parent.joinpath('matched_audio')
    unmatched_audio_path = Path(arguments.unmatched) if arguments.unmatched else \
        audio_links_json.parent.joinpath('unmatched_audio')

    main(corpus_path, audio_links_json, text_out_path, matched_audio_path, unmatched_audio_path)
