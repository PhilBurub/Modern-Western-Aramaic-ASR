"""A set of functions that preprocess initial texts extracted from different sources"""
import re
from typing import List, Callable
import json
from pathlib import Path

REPLACES = json.load(Path('text_replace_pairs.json').open(encoding='utf-8'))


def validate_charset(preprocess: Callable[[str], str]) -> Callable[[str], str]:
    """
    Decorator: raises a warning if text contains characters that are not in the character set
    :param preprocess: preprocessing function
    """

    def validate(*args, **kwargs) -> str:
        """
        Function validates whether the text corresponds to the charset
        :return: output text
        """
        output_text = preprocess(*args, **kwargs)
        character_set = set(' aābcčdḏḍḏ̣eēəfgġhḥiīklmnoōprsšṣtṯṭuūwxyzžẓʕʔ')
        if set(output_text).difference(character_set) != set():
            raise Warning('After preprocessing, the text still contains characters that are not present in the set')
        return output_text

    return validate


def make_replaces(text: str, replaces: List[List[str, str]]) -> str:
    """
    Function runs a chain of replacements for a string
    :param text: string input
    :param replaces: list of tuples containing arguments for the replace method
    :return: texts with replaced characters
    """
    output_text = text
    for replace_pair in replaces:
        output_text = output_text.replace(*replace_pair)
    return output_text


def preprocess_base(text: str) -> str:
    """
    Deletes non-letter characters and space-like symbols besides space
    :param text: input text
    :return: output text
    """
    words_only = ' '.join(re.findall('\w+', text.lower()))
    new_text = re.sub('[\d_]+', ' ', words_only)
    new_text = re.sub('\s+', ' ', new_text)
    return re.sub(r'(\A | \Z)', '', new_text)


@validate_charset
def preprocess_corpus(text: str) -> str:
    """
    Preprocessing of texts obtained from the corpus
    :param text: input text
    :return: output text
    """
    consonants = 'nymgsbtfḏdpšzʔṣḍʕrčṭwhẓṯḥxḳžḷǧġlkc'
    vowels = 'úūīeəaāēáoōuíi'
    output_text = preprocess_base(text)
    output_text = re.sub(fr'(?P<const>[{consonants}])(?=\1[^{vowels}])', '', output_text)
    output_text = re.sub(fr'(?P<const>[{consonants}])(?=\1$)', '', output_text)
    output_text = make_replaces(output_text, REPLACES['corpus'])
    return re.sub(r'(?<!\w)w(?!\w)', 'u', output_text)


@validate_charset
def preprocess_church_militant(text: str) -> str:
    """
    Preprocessing of text from the article 'Church Militant'
    :param text: input text
    :return: output text
    """
    output_text = preprocess_base(text)
    output_text = make_replaces(output_text, REPLACES['church molitant'])
    return re.sub(r'(?<!\w)w(?!\w)', 'u', output_text)


@validate_charset
def preprocess_lullaby(text: str) -> str:
    """
    Preprocessing of text from the article 'Lullaby'
    :param text: input text
    :return: output text
    """
    output_text = preprocess_base(text)
    return make_replaces(output_text, REPLACES['lullaby'])


@validate_charset
def preprocess_war_account(text: str) -> str:
    """
    Preprocessing of text from the article 'War Account'
    :param text: input text
    :return: output text
    """
    output_text = preprocess_base(text)
    return make_replaces(output_text, REPLACES['war account'])


@validate_charset
def preprocess_war_description(text: str) -> str:
    """
    Preprocessing of text from the draft 'War Description'
    :param text: input text
    :return: output text
    """
    output_text = preprocess_base(text)
    return make_replaces(output_text, REPLACES['war description'])


@validate_charset
def preprocess_maaloulians_in_palestine(text: str) -> str:
    """
    Preprocessing of text from the draft 'Maaloulians in Palestine'
    :param text: input text
    :return: output text
    """
    output_text = preprocess_base(text)
    output_text = make_replaces(output_text, REPLACES['maaloulians in palestine'])
    return re.sub(r'(?<!\w)w(?!\w)', 'u', output_text)


@validate_charset
def preprocess_old_words(text: str) -> str:
    """
    Preprocessing of text from the draft 'Old Words'
    :param text: input text
    :return: output text
    """
    output_text = preprocess_base(text)
    return make_replaces(output_text, REPLACES['old words'])
