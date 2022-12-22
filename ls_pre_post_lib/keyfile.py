from qd.cae.dyna import KeyFile
from qd.cae.dyna import Element
from qd.cae.dyna import Node
from qd.cae.dyna import QD_Part
from .cards.card import ICard
import os

#добавление основы после геометрии
class ModelKeyfile(KeyFile):
    """

    """

    def __init__(self, keyfile_name: str, keyfile_path: str) -> None:
        super().__init__()
        self.keyfile = KeyFile(filepath=os.sep.join([keyfile_path, keyfile_name]),
                               load_includes=True,
                               parse_mesh=True)

    @staticmethod
    def _create_keyfile_line(*args) -> str:
        """

        """
        line = ''
        for arg in args:
            line = line + " " * (10 - len(str(arg))) + str(arg)
        return line

    def add_card(self, card: ICard, pos: int = -1) -> None:
        """
        add ICard object to the keyfile (.k)
        """
        card_name = card.get_card_name()
        card_rows = card.get_rows_lengths()
        card_values = card.get_data_list()
        self.keyfile.remove_keyword("*END")
        card_section = self.keyfile.add_keyword("*"+card_name, position=pos)

        i = 0
        for cells_number in card_rows:
            card_section.append_line(self._create_keyfile_line(*card_values[i:i + cells_number]))
            i += cells_number
        self.keyfile.add_keyword("*END")

    def save(self, keyfile_path: str, keyfile_name: str) -> None:
        """

        """
        self.keyfile.save(f'{os.sep.join([keyfile_path, keyfile_name])}')

    def remove_keyword(self, name: str) -> None:
        self.keyfile.remove_keyword(name)

    def get_parts(self):
        return self.keyfile.get_parts()

    def get_partByID(self, i: int) -> QD_Part:
        return self.keyfile.get_partByID(i)
