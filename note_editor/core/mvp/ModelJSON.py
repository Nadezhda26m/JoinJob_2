from JoinJob2NoteEditor.note_editor.core.dataformat.FormatJSON import FormatJSON
from JoinJob2NoteEditor.note_editor.core.mvp.Model import *
import json


class ModelJSON(Model):

    def __init__(self, path, file_name):
        super().__init__(path, file_name, ".json")

    def add_to_file(self, notepad: Notepad):
        f = FormatJSON()
        my_notepad = f.convert_notepad_to_format(notepad)
        with open(self.file, 'w', encoding='utf-8') as db:
            db.writelines(json.dumps(my_notepad, indent=2) + '\n')

    def read_file(self):
        with open(self.file, 'r', encoding='utf-8') as db:
            file_str = json.load(db)
        return file_str
