# Deep Learning Model for Speech Recognition of Modern Werstern Aramaic Language
This repository contains files of project *Deep Learning Model for Speech Recognition of Modern Werstern Aramaic Language*. 
Here, we store all the stages of obtaining the data, processing and training a model.

# Files Navigation
- _corpus crawling_ contains files for crawling audio files of the corpus
  - **crawling.py** represents [Semitisches Tonarchiv webpage](https://semarch.ub.uni-heidelberg.de/#archive) crawling process
  - **audio_links.json** is a result of the latter code
  - **load_match.py** loads audio files and sorts them in two groups, whether they have a corresponding text or not
- _primary processing_ contains files of the first processing that goes before model learning preprocessing
  - **audio_processing.py** rewrites audio in .wav format
  - **text_processing.py** unifies text format
  - **text_replace_pairs.py** contains character correspondences between the source and target formats
  - **data_count.py** analyzes the amount of data
- _data_load_ contains files that access files from the cloud
  - **api_access.py** finds files on Google Drive and downloads them

# About me
My name is Philipp Burlakov, in 2024 I graduate from HSE University Moscow Campus, Computational Linguistics BA.<br>
[My CV](https://drive.google.com/file/d/1ArmG8yozeX9hSdYGy-bUbW0L4vygBi_t/view?usp=sharing)