from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.discovery import build, Resource
import io
from collections import defaultdict
import pandas as pd
from typing import Tuple, List
from path import Path

GOOGLEAPI_SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
CREDENTIALS = service_account.Credentials.from_service_account_file(
    'thesis.json', scopes=GOOGLEAPI_SCOPES)
SERVICE = build('drive', 'v3', credentials=CREDENTIALS)


def getfiles(service: Resource) -> pd.DataFrame:
    """
    Function returns a pandas dataframe that shows ids of corresponding text and audio files
    :param service: initialized Google Drive API service
    :return: dataframe with file ids
    """
    files = service.files().list(pageSize=1000).execute()['files']
    matched = collect_matches(files)
    return pd.DataFrame(matched).T


def collect_matches(files: List[dict]) -> dict:
    """
    Function collects matching audio and text files
    :param files: files list received from Google Drive API
    :return: dictionary with matching audio and text files
    """
    corr = defaultdict(lambda: {})
    for file in files:
        if file['mimeType'] == 'text/plain':
            corr[file['name'][:-4]]['txt'] = file['id']
        elif file['mimeType'] == 'audio/wav':
            corr[file['name'][:-4]]['wav'] = file['id']
    return dict(corr)


def download_row(row: Tuple[str, pd.Series],
                 service: Resource,
                 get_wav: bool = True,
                 get_txt: bool = True,
                 out_path: Path = Path('./')) -> dict:
    """
    Function downloads files listed in a row
    :param row: pandas dataframe row (index, pd.Series)
    :param service: initialized Google Drive API service
    :param get_wav: indicates whether the audio file should be loaded
    :param get_txt: indicates whether the text file should be loaded
    :param out_path: download path
    :return: dictionary with filepaths
    """
    if not out_path.exists():
        out_path.mkdir()

    to_path = {}

    filename, text_wav = row
    wav_file_id, txt_file_id = text_wav.wav, text_wav.txt

    if get_wav and pd.notnull(wav_file_id):
        to_path['wav'] = out_path.joinpath(filename + '.wav')
        download_file(wav_file_id, service, to_path['wav'])

    if get_txt and pd.notnull(txt_file_id):
        to_path['txt'] = out_path.joinpath(filename + '.txt')
        download_file(wav_file_id, service, to_path['txt'])
    return to_path


def download_file(file_id: str, service: Resource, path: Path) -> None:
    """
    Function downloads the file to the given directory
    :param file_id: Google Drive API file id
    :param service: initialized Google Drive API service
    :param path: target path
    """
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(path, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        _, done = downloader.next_chunk()
