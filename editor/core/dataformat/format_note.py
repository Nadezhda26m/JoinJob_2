from abc import ABC, abstractmethod
from editor.core.infrastructure.notepad import Notepad
from editor.core.infrastructure.note import *


class FormatNote(ABC):

    @abstractmethod
    def convert_note_to_format(self, note: Note): pass

    @abstractmethod
    def convert_notepad_to_format(self, notepad: Notepad): pass

    @abstractmethod
    def convert_note_from_format(self, note) -> Note: pass

    @abstractmethod
    def convert_notepad_from_format(self, notepad) -> Notepad: pass
