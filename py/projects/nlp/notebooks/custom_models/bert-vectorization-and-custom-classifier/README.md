# Datasets

For the dataset we use Jigsaw Multilingual Toxic Comment Classification Data here:
<https://www.kaggle.com/competitions/jigsaw-multilingual-toxic-comment-classification/data>

This dataset contains training data in English and evaluation data in French.
There is translated French versions of train data in the following links:
<https://www.kaggle.com/datasets/ludovick/jigsawtanslatedgoogle>
<https://www.kaggle.com/datasets/miklgr500/jigsaw-train-multilingual-coments-google-api>

## Downloading Datasets to S3

We used Kaggle CLI for downloading these and uploaded into S3 with the following commands:

## Download from Kaggle

```sh
kaggle datasets download -d ludovick/jigsawtanslatedgoogle
kaggle datasets download -d miklgr500/jigsaw-train-multilingual-coments-google-api
kaggle competitions download -c jigsaw-multilingual-toxic-comment-classification
```

## Upload to S3

```sh
aws s3 cp jigsaw-multilingual-toxic-comment-classification s3://safebear-train-data/jigsaw-multilingual-toxic-comment-classification --recursive --profile nuage-dev
aws s3 cp jigsaw-train-multilingual-coments-google-api s3://safebear-train-data/jigsaw-train-multilingual-coments-google-api --recursive --profile nuage-dev
aws s3 cp jigsawtanslatedgoogle s3://safebear-train-data/jigsawtanslatedgoogle --recursive --profile nuage-dev
```

## Model Architecture

We will utilize the distiluse-base-multilingual-cased model from [SentenceTransformers](https://www.sbert.net/examples/training/multilingual/README.html), which offers better text vectorization for sentence representation. This is a crucial advantage since our approach involves employing a fixed model for vectorization and a separate model for classification tasks.

There is two versions of this model, second version supports more languages but it performs weaker. So we will go with the first one:
<https://huggingface.co/sentence-transformers/distiluse-base-multilingual-cased-v1>

Descriptions of both models from SBERT Docs:

```text
distiluse-base-multilingual-cased-v1: Multilingual knowledge distilled version of multilingual Universal Sentence Encoder. Supports 15 languages: Arabic, Chinese, Dutch, English, French, German, Italian, Korean, Polish, Portuguese, Russian, Spanish, Turkish.

distiluse-base-multilingual-cased-v2: Multilingual knowledge distilled version of multilingual Universal Sentence Encoder. This version supports 50+ languages, but performs a bit weaker than the v1 model.
```

Consequently, we will generate enhanced text vectors, enabling our classifiers to more effectively distinguish the meaning. This model produces text vectors of length 512, which will serve as the input for our classifier model, while the output will consist of binary classification. We will develop a separate binary classifier for each label.

![Architecture](../../../docs/model_architecture.png)
