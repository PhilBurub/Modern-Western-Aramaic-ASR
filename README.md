# Deep Learning Model for Speech Recognition of Modern Werstern Aramaic Language
This repository contains files of project *Deep Learning Model for Speech Recognition of Modern Werstern Aramaic Language*. 
Here, we store all the stages of obtaining the data, processing and training a model.

# Files Navigation
├─ [_**app**_](app) contains CLI app to run the model<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ [`main.py`](app/main.py) command line interface to access the model locally<br>
├─ _**corpus_crawling**_ contains files for crawling audio files of the corpus<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `crawling.py` represents [Semitisches Tonarchiv webpage](https://semarch.ub.uni-heidelberg.de/#archive) crawling process<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `audio_links.json` is a result of the latter code<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `load_match.py` loads audio files and sorts them in two groups, whether they have a corresponding text or not<br>
├─ _**primary_processing**_ contains files of the first processing that goes before model learning preprocessing<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `audio_processing.py` rewrites audio in .wav format<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `text_processing.py` unifies text format<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `text_replace_pairs.json` contains character correspondences between the source and target formats<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `data_count.py` analyzes the amount of data<br>
├─ _**data_load**_ contains files that access files from the cloud<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `api_access.py` finds files on Google Drive and downloads them<br>
├─ _**notebooks**_ contains notebooks with further processing and tuning<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `Confusion matrix.ipynb` generates phonemic confusion matrix<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `copt_thesis.ipynb` pre-training process<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `cut_aligned.ipynb` cuts audios based on WEB MAUS output<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `Delete_Non_Speech_Parts.ipynb` cuts audios leaving only fragments containing speech<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `evaluate.ipynb` evaluates the model<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `finetune.ipynb` model fine-tuning<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ `transcribe.ipynb` synthetic data generation<br>

# Model
[**HuggingFace**](https://huggingface.co/pburub/wav2vec2-xls-r-300m-mwa-maaloula)<br>
**WER:** 0.3<br>
**CER:** 0.1

# Thesis
[Text]()

# About me
My name is Philipp Burlakov, in 2024 I graduate from HSE University Moscow Campus, Computational Linguistics BA.<br>
[My CV](https://drive.google.com/file/d/1ArmG8yozeX9hSdYGy-bUbW0L4vygBi_t/view?usp=sharing)
