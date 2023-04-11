from abc import ABC, abstractmethod
from JoinJob2NoteEditor.note_editor.core.dataformat.FormatNote import FormatNote
from JoinJob2NoteEditor.note_editor.core.infrastructure.Notepad import Notepad
from os.path import isfile
from pathlib import Path


class Model(ABC):

    @abstractmethod
    def __init__(self, path, file_name, extension, data_format: FormatNote):
        self.file = path + file_name + extension
        self.data_format = data_format
        if not isfile(self.file):
            Path(self.file).touch()

    @abstractmethod
    def add_to_file(self, notepad: Notepad): pass

    @abstractmethod
    def read_file(self) -> Notepad: pass
