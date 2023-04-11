from os.path import getsize
from JoinJob2NoteEditor.note_editor.core.dataformat.FormatJSON import FormatJSON
from JoinJob2NoteEditor.note_editor.core.mvp.Model import *
import json


class ModelJSON(Model):

    def __init__(self, path, file_name):
        super().__init__(path, file_name, ".json", FormatJSON())

    def add_to_file(self, notepad: Notepad):
        my_notepad = self.data_format.convert_notepad_to_format(notepad)
        with open(self.file, 'w', encoding='utf-8') as db:
            db.writelines(json.dumps(my_notepad, indent=2) + '\n')

    def read_file(self):
        if getsize(self.file) > 0:
            with open(self.file, 'r', encoding='utf-8') as db:
                file_str = json.load(db)
            return self.data_format.convert_notepad_from_format(file_str)
        else:
            return Notepad()
