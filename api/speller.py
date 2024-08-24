from pyaspeller import YandexSpeller


class Speller:

    speller = YandexSpeller()

    @classmethod
    def correct_text(cls, text: str) -> str:
        return cls.speller.spelled(text)
