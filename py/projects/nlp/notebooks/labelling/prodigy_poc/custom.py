import copy
import random
from typing import Iterable, List

import prodigy
from prodigy.components.loaders import JSONL
from prodigy.components.sorters import prefer_uncertain
from prodigy.util import split_string


class DummyModel:
    def __init__(self, hint_for_uncertain: str):
        # hint_for_uncertain is used for testing prodiy uncertainity feature.
        # Whenever we see that text in the sentence we will return 0.5.
        self.hint_for_uncertain = hint_for_uncertain

        # In real world scenarion we will just load our model here.

    def predict(self, text: str):
        if self.hint_for_uncertain in text:
            return 0.5

        # Return random for other sentences
        # In real world scneario we will run model.predict() here and return the score from it.
        return random.random()


class ModelFlow(object):
    # This is a model flow that we can run multiple classifiers and predict for each.

    def __init__(self):
        self.toxic_model = DummyModel("222")
        self.insult_model = DummyModel("111")

    def __call__(self, stream: Iterable[dict]):
        for eg in stream:
            predictions = {
                "toxic": self.toxic_model.predict(eg["text"]),
                "insult": self.insult_model.predict(eg["text"]),
            }
            # Create prediction for each label.
            for label, score in predictions.items():
                # Score the example with respect to the current weights and
                # assign a label
                item = copy.deepcopy(eg)
                item["label"] = label
                yield (score, item)

    def update(self, answers: List[dict]):
        accepted = [eg for eg in answers if eg["answer"] == "accept"]
        rejected = [eg for eg in answers if eg["answer"] == "reject"]

        # Re-train models here.
        # To have remaining progressbar, we can return loss. If we don't return anything the progressbar swill show infinity.
        return 1 / len(accepted)
        # return loss


# Recipe decorator with argument annotations: (description, argument type,
# shortcut, type / converter function called on value before it's passed to
# the function). Descriptions are also shown when typing --help.
@prodigy.recipe(
    "textcat.custom-model",
    dataset=("The dataset to use", "positional", None, str),
    source=("The source data as a JSONL file", "positional", None, str),
)
def textcat_custom_model(dataset: str, source: str):
    """
    Use active learning-powered text classification with a custom model. To
    demonstrate how it works, this demo recipe uses a simple dummy model that
    "precits" random scores. But you can swap it out for any model of your
    choice, for example a text classification model implementation using
    PyTorch, TensorFlow or scikit-learn.
    """
    # Load the stream from a JSONL file and return a generator that yields a
    # dictionary for each example in the data.
    stream = JSONL(source)

    # Load the dummy model
    model = ModelFlow()

    # Use the prefer_uncertain sorter to focus on suggestions that the model
    # is most uncertain about (i.e. with a score closest to 0.5). The model
    # yields (score, example) tuples and the sorter yields just the example
    stream = prefer_uncertain(model(stream))

    # The update method is called every time Prodigy receives new answers from
    # the web app. It can be used to update the model in the loop.
    update = model.update

    return {
        "view_id": "classification",  # Annotation interface to use
        "dataset": dataset,  # Name of dataset to save annotations
        "stream": stream,  # Incoming stream of examples
        "update": update,  # Update callback, called with batch of answers
    }
