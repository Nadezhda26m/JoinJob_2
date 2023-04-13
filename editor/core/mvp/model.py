from abc import ABC, abstractmethod
from editor.core.dataformat.format_note import FormatNote
from editor.core.infrastructure.notepad import Notepad
from os.path import isfile
from pathlib import Path


class Model(ABC):

    @abstractmethod
    def __init__(self, path, file_name, extension, data_format: FormatNote):
        self._file = path + file_name + extension
        self._data_format = data_format
        if not isfile(self._file):
            Path(self._file).touch()

    @abstractmethod
    def add_to_file(self, notepad: Notepad): pass

    @abstractmethod
    def read_file(self) -> Notepad: pass
