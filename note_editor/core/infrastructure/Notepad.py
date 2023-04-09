from JoinJob2NoteEditor.note_editor.core.models.Note import *


class Notepad:

    def __init__(self):
        self._list_notes = []

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

    # def sort_notes(self):  #
    #     pass


my_notes = Notepad()

a = 1
while True:
    if a % 3 == 0:
        note_t = input("new title 2> ")
        my_notes.change_note(1, note_t)
    else:
        note_t = input("title> ")
        note_txt = input("text> ")
        my_notes.add_note(Note(note_t, note_txt, datetime.now(), a))
    a += 1

    b = 1
    for i in my_notes.read_all():
        print(f'{b}. {i}')
        b += 1
    print()

    note_list = my_notes.read_all()
    size = len(note_list)
    for i in range(size):
        print(note_list[i].__repr__())
    print()
