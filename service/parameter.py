import configparser


class Parameter():

    @staticmethod
    def get_parameter(key):
        parser = configparser.ConfigParser()
        parser.read('./config/settings.ini')

        return parser["app"].get(key)
