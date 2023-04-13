from note_editor.core.infrastructure.Note import *


class Notepad:

    def __init__(self):
        self._list_notes = []

    def __str__(self):
        return f"{self._list_notes}"

    def add_note(self, note: Note):
        self._list_notes.insert(0, note)

    def add_note_to_end(self, note: Note):
        self._list_notes.append(note)

    def read_note(self, index: int):
        if index < len(self._list_notes):
            return self._list_notes[index]  # Note
        else:
            return False

    def read_all(self):
        return self._list_notes

    def change_note_title(self, index: int, new_value: str, parameter="title"):
        note = self._list_notes.pop(index)
        note.__setattr__(parameter, new_value)
        note.date_time = datetime.now()
        self.add_note(note)

    def change_note_text(self, index: int, new_value: str):
        self.change_note_title(index, new_value, "text")

    def change_note(self, index: int, new_title: str, new_text: str):
        self.change_note_title(index, new_title)
        self.change_note_text(0, new_text)

    def del_note(self, index: int):
        self._list_notes.pop(index)

    def del_all(self):
        self._list_notes.clear()

    def size(self):
        return len(self._list_notes)

    def get_max_note_id(self):
        if len(self._list_notes) > 0:
            return max(self._list_notes, key=lambda k: k.NOTE_ID).NOTE_ID
        else:
            return 0

    def get_len_short_text(self) -> int:
        if self.size() > 0 and 0 < self._list_notes[0].short_text < 16:
            return self._list_notes[0].short_text
        return 10
