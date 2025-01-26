class SentimentMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Sentiment(metaclass=SentimentMeta):

    # TODO: Implement sentiment analysis
    # noinspection PyMethodMayBeStatic
    def get_sentiment(self, entry_text: str):
        if entry_text:
            return 0.5
