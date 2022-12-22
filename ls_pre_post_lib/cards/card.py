from abc import ABC
from typing import List, Any

#интерфейс для карточек в модулях он определяет методы для того чтоб затем карточкуможно было перевести в к файл , наследуется от абстрактного класса
class ICard(ABC):
    name: str = ""
    rows_lengths: List[int] = []

    def get_data_list(self) -> List[Any]:
        """

        """
        list_card = list(self.__dict__.values())[2:]  # first two values - name and rows_length
        new_list_card = []
        for element in list_card:
            if isinstance(element, list):
                for dictionary in element:
                    new_list_card += list(dictionary.values())
            else:
                new_list_card.append(element)
        return new_list_card

    def get_card_name(self) -> str:
        """

        """
        return self.name

    def get_rows_lengths(self) -> List[int]:
        """

        """
        return self.rows_lengths
