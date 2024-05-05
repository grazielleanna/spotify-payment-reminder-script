from typing import Literal

class SpotifyPerson():
    """
    Class representing a person participating in spotify

    Args:
    name (str): The name person
    type (Literal): Whether the person is the payer of the month or the payer of the next month

    Attributes:
    name (str): The name person
    type (Literal): Whether the person is the payer of the month or the payer of the next month
    """
    def __init__(self, name: str, type: Literal['paying_user', 'next_paying_user']) -> None:
        """
        Initialize a spotify person instance

        Args:
        name (str): The name person
        type (Literal): Whether the person is the payer of the month or the payer of the next month.
        """
        self.name = name
        self.type = type