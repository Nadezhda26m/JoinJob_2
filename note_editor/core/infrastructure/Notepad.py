from JoinJob2NoteEditor.note_editor.core.models.Note import *


class Notepad:

    def __init__(self):
        self._list_notes = []

    def __str__(self):
        return f"{self._list_notes}"

    def add_note(self, note: Note):
        self._list_notes.insert(0, note)

    def read_note(self, index: int):
        if index < len(self._list_notes):
            return self._list_notes[index]  # Note
        else:
            return False

    def read_all(self):
        return self._list_notes

    def change_note(self, index: int, parametr):  # параметр
        note = self._list_notes.pop(index)
        note.title = parametr  #
        note.date_time = datetime.now()
        self.add_note(note)

    def del_note(self, index: int):
        self._list_notes.pop(index)

    def del_all(self):
        self._list_notes.clear()
