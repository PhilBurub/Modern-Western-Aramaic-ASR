# Deep Learning Model for Speech Recognition of Modern Werstern Aramaic Language
This repository contains files of project *Deep Learning Model for Speech Recognition of Modern Werstern Aramaic Language*. 
Here, we store all the stages of obtaining the data, processing and training a model.

# Files Navigation
├─ [_**app**_](app) contains CLI app to run the model<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ [`main.py`](app/main.py) command line interface to access the model locally<br>
├─ [_**corpus_crawling**_](corpus_crawling) contains files for crawling audio files of the corpus<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ [`crawling.py`](corpus_crawling/crawling.py) represents [Semitisches Tonarchiv webpage](https://semarch.ub.uni-heidelberg.de/#archive) crawling process<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ [`audio_links.json`](corpus_crawling/audio_links.json) is a result of the latter code<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ [`load_match.py`](corpus_crawling/load_match.py) loads audio files and sorts them in two groups, whether they have a corresponding text or not<br>
├─ [_**primary_processing**_](primary_processing) contains files of the first processing that goes before model learning preprocessing<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ [`audio_processing.py`](primary_processing/audio_processing.py) rewrites audio in .wav format<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ [`text_processing.py`](primary_processing/text_processing.py) unifies text format<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ [`text_replace_pairs.json`](primary_processing/text_replace_pairs.py) contains character correspondences between the source and target formats<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ [`data_count.py`](primary_processing/data_count.py) analyzes the amount of data<br>
├─ [_**data_load**_](data_load) contains files that access files from the cloud<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ [`api_access.py`](data_load/api_access.py) finds files on Google Drive and downloads them<br>
├─ [_**notebooks**_](notebooks) contains notebooks with further processing and tuning<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ [`Confusion matrix.ipynb`](notebooks/Confusion matrix.ipynb) generates phonemic confusion matrix<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ [`copt_thesis.ipynb`](notebooks/copt_thesis.ipynb) pre-training process<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ [`cut_aligned.ipynb`](notebooks/cut_aligned.ipynb) cuts audios based on WEB MAUS output<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ [`Delete_Non_Speech_Parts.ipynb`](notebooks/Delete_Non_Speech_Parts.ipynb) cuts audios leaving only fragments containing speech<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ [`evaluate.ipynb`](notebooks/evaluate.ipynb) evaluates the model<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ [`finetune.ipynb`](notebooks/finetune.ipynb) model fine-tuning<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ [`transcribe.ipynb`](notebooks/transcribe.ipynb) synthetic data generation<br>
├─ [_**thesis_content**_](thesis_content) contains text and slides materials of a submitted work<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ [`Text.pdf`](thesis_content/Text.pdf) text of the thesis<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├─ [`Slides.pdf`](thesis_content/Slides.pdf) slides from the thesis presentation<br>

# Model
[**HuggingFace**](https://huggingface.co/pburub/wav2vec2-xls-r-300m-mwa-maaloula)<br>
**WER:** 0.3<br>
**CER:** 0.1

# Thesis
[Text](thesis_content/Text.pdf)<br>
[Slides](thesis_content/Slides.pdf)

# About me
My name is Philipp Burlakov, in 2024 I graduated from HSE University Moscow Campus, Computational Linguistics BA.<br>
[My CV](thesis_content/CV.pdf)
