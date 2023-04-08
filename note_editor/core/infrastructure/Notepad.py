from JoinJob2NoteEditor.note_editor.core.models.Note import *


class Notepad:

    def __init__(self):
        self.list_notes = []
        # self.index = index

    def _add_note(self, note: Note):
        self.list_notes.append(note)  # добавит в конец списка

    def _read_note(self, index: int):
        if index < len(self.list_notes):
            return self.list_notes[index]  # Note
        else:
            return False

    def _read_all(self):
        return self.list_notes

    # def _change_note(self, index: int, parametr):
    #     note = self.list_notes[index]

    def _del_note(self, index: int):
        self.list_notes.pop(index)

    def _del_all(self):
        self.list_notes.clear()