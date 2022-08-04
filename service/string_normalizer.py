import unicodedata


class StringNormalizer():
    @staticmethod
    def normalize(value):
        return ''.join(c for c in unicodedata.normalize('NFD', value) if unicodedata.category(c) != 'Mn')
