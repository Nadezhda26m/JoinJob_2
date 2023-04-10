from abc import ABC, abstractmethod
from JoinJob2NoteEditor.note_editor.core.infrastructure.Notepad import Notepad


class Model(ABC):

    @abstractmethod
    def __init__(self, path, file_name, extension):
        self.file = path + file_name + extension

    @abstractmethod
    def add_to_file(self, notepad: Notepad): pass

    @abstractmethod
    def read_file(self): pass
