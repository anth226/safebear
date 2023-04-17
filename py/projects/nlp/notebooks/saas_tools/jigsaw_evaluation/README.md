# 1. Test Data

We used test data from Jigsaw with following labels:

* Toxic
* Obscene
* Threat
* Insult
* Identity Attack


# 2. Results

## 2.1. MultiLabel

### OpenAI
```
                 precision    recall  f1-score   support

identity_attack       0.22      0.53      0.31       139
         insult       0.37      0.83      0.51       287
        obscene       0.22      0.03      0.05       128
         threat       0.60      0.06      0.11       100
          toxic       0.56      0.02      0.04       396

      micro avg       0.32      0.32      0.32      1050
      macro avg       0.39      0.30      0.21      1050
   weighted avg       0.43      0.32      0.21      1050
    samples avg       0.21      0.20      0.19      1050
```
### Hive
```
                 precision    recall  f1-score   support

identity_attack       0.77      0.48      0.59       139
         insult       0.24      0.07      0.10       287
        obscene       0.16      0.10      0.13       128
         threat       0.49      0.67      0.56       100
          toxic       0.89      0.27      0.42       396

      micro avg       0.54      0.26      0.35      1050
      macro avg       0.51      0.32      0.36      1050
   weighted avg       0.57      0.26      0.33      1050
    samples avg       0.19      0.16      0.16      1050
```
### Custom Model

```
                 precision    recall  f1-score   support

identity_attack       0.92      0.96      0.94       139
         insult       0.80      0.91      0.85       287
        obscene       0.90      0.89      0.89       128
         threat       0.99      0.91      0.95       100
          toxic       0.59      0.96      0.73       396

      micro avg       0.73      0.93      0.82      1050
      macro avg       0.84      0.93      0.87      1050
   weighted avg       0.77      0.93      0.83      1050
    samples avg       0.49      0.60      0.52      1050

```
## 2.2. Binary

### OpenAI
```
              precision    recall  f1-score   support

      Normal       0.55      0.54      0.54       350
       Toxic       0.75      0.76      0.76       650

    accuracy                           0.68      1000
   macro avg       0.65      0.65      0.65      1000
weighted avg       0.68      0.68      0.68      1000
```
### Hive
```
              precision    recall  f1-score   support

      Normal       0.48      0.93      0.64       350
       Toxic       0.93      0.46      0.61       650

    accuracy                           0.62      1000
   macro avg       0.70      0.70      0.62      1000
weighted avg       0.77      0.62      0.62      1000
```
### Custom Model
```
              precision    recall  f1-score   support

      Normal       0.92      0.86      0.89       350
       Toxic       0.93      0.96      0.94       650

    accuracy                           0.92      1000
   macro avg       0.92      0.91      0.92      1000
weighted avg       0.92      0.92      0.92      1000
```

# 3. Summary

We can use F1-score (macro avg) for overall comparision of different methods. We can see that custom model performs better than both OpenAI and the Hive.


|                | Multi Label | Binary   |
|----------------|-------------|----------|
| Hive           | 0.36        | 0.62     |
| OpenAI         | 0.21        | 0.65     |
| Custom Model   | 0.87        | 0.92     |