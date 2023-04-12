import datetime
from abc import ABC, abstractmethod


class View(ABC):

    @abstractmethod
    def get_note_title(self) -> str: pass

    @abstractmethod
    def get_note_text(self) -> str: pass

    @abstractmethod
    def get_len_preview_text(self) -> int: pass

    @abstractmethod
    def print_str(self, format_note: str): pass

    @abstractmethod
    def show_notepad(self, format_note: str, index: int): pass

    @abstractmethod
    def get_index_note(self, max_index: int) -> int: pass

    @abstractmethod
    def get_index_command(self, commands: list[str]) -> int: pass

    @abstractmethod
    def get_parameter_to_change(self, parameters: list[str]) -> int: pass

    @abstractmethod
    def show_commands(self, commands: list[str]): pass

    @abstractmethod
    def show_parameters(self, parameters: list[str]): pass

    @abstractmethod
    def show_old_title(self, old_value: str, name_value: str = ""): pass

    @abstractmethod
    def show_old_text(self, old_value: str, name_value: str = ""): pass

    @abstractmethod
    def get_date(self, format_date="%d.%m.%Y") -> datetime: pass

    @abstractmethod
    def confirm_action(self) -> bool: pass
