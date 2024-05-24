"""The process of crawling Semitisches Tonarchiv webpage"""
from typing import Dict
from selenium import webdriver
from selenium.webdriver.remote.errorhandler import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import time
import json
import argparse
from pathlib import Path


def crawl_page(page: str, sleep_time: int = 10) -> Dict[str, str]:
    """
    Function crawls a website page and collects links to audio files
    :param page: page url
    :param sleep_time: time between requests in seconds
    :return: dictionary of filenames and corresponding links
    """
    driver = webdriver.Chrome()
    driver.get(page)
    time.sleep(sleep_time)

    data = {}
    while True:
        objs = driver.find_elements(By.CLASS_NAME, "ep-type-objekte")
        for obj in objs:
            data.update(process_object(obj))

        try:
            driver.find_element(By.XPATH, "//button[@data-function='ep-pages-forw']").click()
            time.sleep(sleep_time)
        except NoSuchElementException:
            driver.close()
            break
    return data


def process_object(obj: WebElement, sleep_time: int = 8) -> Dict[str, str]:
    """
    Function processes a web page object that includes a filename and a link
    :param obj: web page object
    :param sleep_time: time between requests in seconds
    :return: dictionary of a filename and a link
    """
    name = obj.find_element(By.CLASS_NAME, "ez-format-comma").text
    if not name.startswith('Maʿlūla'):
        return {}
    details_button = obj.find_element(By.CLASS_NAME, "ep-detail-switch")
    details_button.click()
    time.sleep(sleep_time)
    try:
        audio = obj.find_element(By.CSS_SELECTOR, "audio")
    except NoSuchElementException:
        time.sleep(sleep_time)
        audio = obj.find_element(By.CSS_SELECTOR, "audio")
    link = audio.find_element(By.CSS_SELECTOR, "source").get_attribute('src')
    details_button.click()
    return {name: link}


def main(page_url: str,
         out_file: Path):
    links_dict = crawl_page(page_url)
    json.dump(links_dict,
              out_file.open(mode='w', encoding='utf-8'),
              ensure_ascii=False,
              indent='\t')


if __name__ == '__main__':
    parser = argparse.ArgumentParser('Audio Links Crawler')
    parser.add_argument('-u', '--url', help='URL link to audio page')
    parser.add_argument('-o', '--out', help='Path to the directory to write target json file')

    arguments = parser.parse_args()
    page_url = arguments.url
    out_file = Path(arguments.out).joinpath('audio_links.json')
    main(page_url, out_file)

"""
-u
"https://semarch.ub.uni-heidelberg.de/#filter:2:[%22Aram%C3%A4isch%22,%22Neuwestaram%C3%A4isch%22]"
-o
"."
"""