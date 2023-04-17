from faker.providers import BaseProvider


class ToxicMessageProvider(BaseProvider):
    def toxic_message(self):
        return "This is a toxic message"
