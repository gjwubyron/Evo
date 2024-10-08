## Setup

Install required packages:

```bash
git clone git@github.com:gjwubyron/Evo.git
cd Evo
pip install -r requirements.txt
```
## Download data


Download the data from [Abstract Meaning Representation (AMR) Annotation Release 2.0](https://catalog.ldc.upenn.edu/LDC2017T10) and [Abstract Meaning Representation 2.0 - Four Translations](https://catalog.ldc.upenn.edu/LDC2020T07).

The translations we collected will be released soon. Due to the origin of the translations, the data we use is to be licensed by the Linguistic Data Consortium. If you would like to use this dataset for your research, please contact the authors. The collection of the data continues.

## Reorganize data
After downloading the data, run the following command to reorganize the data:

```bash
python LDC/organize_data.py -d <path_of_the_translation_folders> -r <path_of_the_reference_files>
```

Reorganize the data in a format that the first column is the source sentence and the second column is the target sentence. The rest will be the translations from each date.

## sacreBLEU

Run the following command to get the BLEU and chrF score:

```bash
python sacrebleu.py -d <data_path> -o <output_path> -m <metric>
```

## Neural Metrics

Run the following command to get the score for all the neural metrics:

```bash
python neu_metric.py -d <data_path> -o <output_path> -m <metric>
```

## The visualization of the results will be avaliable in the view_of_RQ.ipynb




