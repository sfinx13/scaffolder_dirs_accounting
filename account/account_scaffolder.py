from service.string_normalizer import StringNormalizer
from service.parameter import Parameter
from account.account_directory import AccountDirectory

import calendar
import locale
import os


class AccountScaffolder():

    def __init__(self):
        self.year = 2021
        self.month_number = -1
        self.month_name = ''
        locale.setlocale(locale.LC_ALL, Parameter.get_parameter('locale'))

    def _ask_month(self):
        while True:
            try:
                while self.month_number < 0 or self.month_number > 12:
                    self.month_number = int(input('Merci de saisir le numéro du mois entre 1 et 12 : '))
                    if self.month_number < 0 or self.month_number > 12:
                        print('Le mois doit être saisi entre 1 et 12')
            except ValueError:
                print(f'{self.month_number} n\'est pas un mois valide')
            else:
                self.month_name = StringNormalizer.normalize(calendar.month_name[self.month_number])
                return self.month_name

    def _ask_year(self):
        while True:
            try:
                while self.year < 2022:
                    self.year = int(input('Merci de saisir une année : '))
                    if self.year < 2022:
                        print('L\'année doit être supérieur à 2022')
            except ValueError:
                print(f'{self.year} n\'est pas une année valide')
            else:
                return self.year

    def setup(self):
        self._ask_year()
        self._ask_month()

    def build(self):
        month_number_formated = f'{self.month_number:02d}'
        path = os.path.join(
            Parameter.get_parameter('path'), str(self.year), f'{month_number_formated}-{self.month_name}'
        )

        try:
            for dir in (AccountDirectory):
                dir_path = os.path.join(path, dir.value)
                try:
                    os.makedirs(dir_path)
                    print(f'[OK] {dir_path} crée')
                except FileExistsError:
                    print(f'[KO] {dir_path} Repertoire déja crée')
        except FileNotFoundError:
            print('Le chemin n\'existe pas')
