import os

import torch
from fairseq import hub_utils
from fairseq.models.roberta import RobertaModel, RobertaHubInterface
from torch import LongTensor

from utils.environment import Environment


class SentimentMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Sentiment(metaclass=SentimentMeta):
    roberta_labels_mapping = {
        "__label__meta_minus_m": "negative_sentiment",
        "__label__meta_plus_m": "positive_sentiment",
        "__label__meta_zero": "neutral_sentiment",
        "__label__meta_amb": "neutral_sentiment"
    }

    labels_number_mapping = {
        "negative_sentiment": -1,
        "neutral_sentiment": 0,
        "positive_sentiment": 1,
    }

    sentiment_labels = [
        "__label__meta_minus_m",
        "__label__meta_plus_m",
        "__label__meta_zero",
        "__label__meta_amb"
    ]

    def initialize(self):
        model_path = Environment.resource_path("static/roberta")
        loaded = hub_utils.from_pretrained(
            model_name_or_path=model_path,
            data_name_or_path=Environment.resource_path('static/data_processed'),
            checkpoint_file='checkpoint_best.pt',
            bpe="sentencepiece",
            sentencepiece_vocab=os.path.join(model_path, "sentencepiece.bpe.model"),
            load_checkpoint_heads=True,
            archive_map=RobertaModel.hub_models(),
            cpu=False,
        )
        self.roberta = RobertaHubInterface(loaded['args'], loaded['task'], loaded['models'][0])
        self.roberta.eval()

    def devide_and_get_mean(self, sentence: str) -> str:
        sentences = []
        chunk = ''
        for word in sentence.strip().split():
            # 510, not 512, because of the special tokens <s> and </s>
            if len(self.roberta.encode(chunk + word + ' ')) <= 510:
                chunk += ' ' + word
            else:
                sentences.append(chunk.strip())
                chunk = word
        if chunk:
            sentences.append(chunk.strip())
        sentiment = 0
        for sentence in sentences:
            input_tokens = self.roberta.encode(sentence)
            label = self.predict_sentiment4small_sentence(input_tokens)
            sentiment += self.labels_number_mapping.get(label, 0)
        sentiment /= len(sentences)
        if sentiment < -0.20:
            return "negative_sentiment"
        elif sentiment > 0.20:
            return "positive_sentiment"
        return "neutral_sentiment"

    def predict_sentiment4small_sentence(self, input_tokens: LongTensor) -> str:
        with torch.no_grad():
            logits = self.roberta.predict("sentence_classification_head", input_tokens)
            predicted_class = torch.argmax(logits, dim=-1).item()
        label = self.sentiment_labels[predicted_class]
        mapped_label = self.roberta_labels_mapping.get(label, None)
        return mapped_label

    def get_sentiment(self, entry_text: str):
        input_tokens = self.roberta.encode(str(entry_text))

        # 510, not 512, because of the special tokens <s> and </s>
        if len(input_tokens) <= 510:
            return self.predict_sentiment4small_sentence(input_tokens)
        else:
            return self.devide_and_get_mean(entry_text)
