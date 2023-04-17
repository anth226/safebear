# 1. Our Test Data

Contains 37 items in 7 different categories.

* Racisme
* Insulte (et Discrimination)
* Obscénité
* Sexualité explicite
* Menace
* Toxicité
* Sexisme


# 2. Hive

https://hivemoderation.com/text-moderation

https://docs.thehive.ai/docs/text-moderation-api

Hive supports the following labels in French:
* hate
* bullying
* sexual
* violence

PoC notebook https://github.com/nuage-studio/safebear/blob/master/py/notebooks/hive-poc.ipynb

## 2.1. Binary Evaluation

All of the labels in the dataset converted to "Toxic" as binary and when Hive predicted any of its 4 labels we assume the prediction is correct.

```
Correct Prediction / Total Item: 28 / 37
Accuracy: 75.68%
```
## 2.2. Multi-Label Evaluation

Our data labels are mapped with the following dictionary and during evaluation its checked if one of the predictions is the correct label:
```python
{
    "Racisme":"hate",
    "Insulte (et Discrimination)":"bullying",
    "Obscénité":"sexual",
    "Sexualité explicite":"sexual",
    "Menace":"violence",
    "Toxicité":"bullying",
    "Sexisme":"hate"
}
```

### Result:
```
Correct Prediction / Total Item: 18 / 37
Accuracy: 48.65%
```


# 3. OpenAI

As OpenAI is a general language model we can customize the labels in any way we want. By using its general understanding it will try to classify accordingly. 

There are 4 different models of OpenAI: (from simpler to complex one)

* Ada
* Babbage
* Curie
* Davinci

In all experiments, we see that models other than Davinci give very inaccurate results with many False Positives or False Negatives.

When we try to predict our original labels:

## 3.1. All Labels (Multi Class Prediction)

PoC notebook https://github.com/nuage-studio/safebear/blob/master/py/notebooks/openai-poc.ipynb

### Prompt:
```
The following is a list of text categories in French:

1. Racisme
2. Insulte (et Discrimination)
3. Obscénité
4. Sexualité explicite
5. Menace
6. Toxicité
7. Sexisme

Please classify the following text as one or multiple of the above categories:
"{input_text}"
```
## Result:
```
Correct Prediction / Total Item: 20 / 37
Accuracy: 54.05%
```

## 3.2. Merge Some Labels (Multi Class Prediction)

PoC notebook https://github.com/nuage-studio/safebear/blob/master/py/notebooks/openai-poc-merged-labels.ipynb

We merged some of the labels into single categories and reduced number of labels to 4

```
1. Insult or Discrimination (Racisme + Insulte (et Discrimination) + Sexisme)
2. Obscene or Sexual (Obscénité + Sexualité explicite)
3. Threats of Violence (Menace)
4. Cyberbullying or Toxic (Toxicité)
```

### Result:
```
Correct Prediction / Total Item: 28 / 37
Accuracy: 75.68%
```

## 3.3. All Labels  (Multi Label Prediction)

PoC notebook https://github.com/nuage-studio/safebear/blob/master/py/notebooks/openai-poc-multi-label.ipynb

We asked OpenAI to do a multi-label classification instead of limiting to one label.

### Prompt
```
The following is a list of text categories in French:

1. Racisme
2. Insulte (et Discrimination)
3. Obscénité
4. Sexualité explicite
5. Menace
6. Toxicité
7. Sexisme

Please classify the following text as one or multiple of the above categories:
```

### Results:
```
Correct Prediction / Total Item: 18 / 37
Accuracy: 48.65%
```

## 3.4. Binary Classification + Model Comparisions

PoC notebook https://github.com/nuage-studio/safebear/blob/master/py/notebooks/openai-poc-binary.ipynb

In binary classification, we also tested the simpler models as its the simplest task and compared different models of the OpenAI. 

### Prompt
```
Decide whether a text's class is toxic or normal. Write only the label, no explanation.
Text: "{input_text}"
Category:
```

### Results

|                  | Correct Prediction | Accuracy | Correct in Neutral |
|------------------|--------------------|----------|--------------------|
| text-davinci-003 | 29 / 37            | 78.38%   | 4 / 4  (100%)      |
| text-curie-001   | 37 / 37            | 100%     | 0 / 4  (0%)        |
| text-babbage-001 | 35 / 37            | 94.59%   | 2 / 4  (50%)       |
| text-ada-001     | 3 / 37             | 8.11%    | 4 / 4  (0%)        |

Models other than davinci performed poorly on this task. Although `text-curie-001` seems to have 100% accuracy on the toxic items its because it always predicts as Toxic (0% accuracy in the neutral items.), which means it gives many False Positives.

Models other than `text-davinci-003` perform badly on the test data, so we will do the final comparison with the `text-davinci-003`.


# 4. Comparision


Here are the results from the best performing variants of each system:

## 4.1. Hive

|                  | Binary Toxic       | Multi Label (4 Class) | Accuracy in Neutral |
|------------------|--------------------|-----------------------|---------------------|
| **Hive**         | 28 / 37 (75.68%)   | 18 / 37 (48.65%)      | 4 / 4  (100%)       |

## 4.2. OpenAI

|                                | Binary Toxic       | Multi Label (7 Class) | Multi Class (4 Class) | Accuracy in Neutral |
|--------------------------------|--------------------|-----------------------|-----------------------|---------------------|
| **OpenAI (text-davinci-003)**  | 29 / 37 (78.38%)   | 18 / 37 (48.65%)      | 28 / 37 (75.68%)      | 4 / 4  (100%)       |


--- 
**Binary**: OpenAI and Hive performed very closely with 75% and 78% accuracy respectively.

**Multi-Label**: Hive and OpenAI performed the same with 48.65% but Hive has 4 labels while we do the evaluation with 7 labels in the OpenAI

**Multi-Class**: There is no multi-class option in Hive but OpenAI performed the same as binary with 75.68%.


## 4.3 Comment

* If we will go with binary classification Hive and OpenAI works similar.

* For multi-class or multi-label prediction, OpenAI performs much more better. And also in Hive we are limited with the 4 labels (hate, bullying, sexual, violence) while we can add any label in the OpenAI.

* Although OpenAI performs much better than Hive, the good results are only from the most complex model `text-davinci-003` which costs `$0.0200` per 1k tokens that estimately 500 queries for 1$. So pricing can be another consideration when selecting one of them.