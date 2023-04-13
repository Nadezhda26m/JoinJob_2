from editor.core.dataformat.format_note import *


class FormatJSON(FormatNote):

    def convert_note_to_format(self, note: Note):
        result = {}
        result["note_id"] = note.NOTE_ID
        result["title"] = note.title
        result["text"] = note.text
        result["date_time"] = note.date_time.strftime("%d.%m.%Y %H:%M:%S")
        result["short_text"] = note.short_text
        return result

    def convert_notepad_to_format(self, notepad: Notepad):
        my_notepad = []
        for note in notepad.read_all():
            my_notepad.append(self.convert_note_to_format(note))
        return my_notepad

    def convert_note_from_format(self, note) -> Note:
        return Note(note["title"],
                    note["text"],
                    datetime.strptime(note["date_time"], "%d.%m.%Y %H:%M:%S"),
                    note["note_id"],
                    note["short_text"])

    def convert_notepad_from_format(self, notepad) -> Notepad:
        list_notes = Notepad()
        for note in notepad:
            list_notes.add_note_to_end(self.convert_note_from_format(note))
        return list_notes
