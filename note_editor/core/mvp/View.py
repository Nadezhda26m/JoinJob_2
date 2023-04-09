from abc import ABC, abstractmethod


class View(ABC):

    @abstractmethod
    def get_note_title(self) -> str: pass

    @abstractmethod
    def get_note_text(self) -> str: pass

    @abstractmethod
    def get_len_preview_text(self) -> int: pass

    @abstractmethod
    def show_full_note(self, full_note: str): pass

    @abstractmethod
    def show_short_note(self, short_note: str): pass

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
