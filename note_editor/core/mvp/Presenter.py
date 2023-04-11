from datetime import datetime
from JoinJob2NoteEditor.note_editor.core.infrastructure.Notepad import Notepad
from JoinJob2NoteEditor.note_editor.core.models.Note import Note
from JoinJob2NoteEditor.note_editor.core.mvp.Model import Model
from JoinJob2NoteEditor.note_editor.core.mvp.View import View


class Presenter:

    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
        self.notepad: Notepad = model.read_file()
        self.index: int = self.notepad.get_max_note_id() + 1
        self.parameters = ["Изменить заголовок", "Изменить текст заметки",
                           "Изменить заголовок и текст заметки"]

    def __str__(self):
        return f"{self.notepad}"

    def add_new_note(self):
        new_note = Note(self.view.get_note_title(),
                        self.view.get_note_text(),
                        datetime.now(), self.index)
        self.notepad.add_note(new_note)
        self.index += 1
        self.view.print_str(f"Заметка #{new_note.NOTE_ID:04} "
                            f"<{new_note.title}> успешно создана")
        self.model.add_to_file(self.notepad)

    def change_note(self):
        if self.show_notepad():
            index_note = self.view.get_index_note(self.notepad.size())
            select_note = self.notepad.read_all()[index_note]
            parameter = self.view.get_parameter_to_change(self.parameters)
            match parameter:
                case 1:
                    self.view.show_old_title(select_note.title)
                    self.notepad.change_note_title(index_note, self.view.get_note_title())
                case 2:
                    self.view.show_old_text(select_note.text)
                    self.notepad.change_note_text(index_note, self.view.get_note_text())
                case 3:
                    self.view.show_old_title(select_note.title)
                    new_title = self.view.get_note_title()
                    self.view.show_old_text(select_note.text)
                    new_text = self.view.get_note_text()
                    self.notepad.change_note(index_note, new_title, new_text)
            self.view.print_str("Изменения сохранены")
            self.model.add_to_file(self.notepad)

    def del_note(self):
        if self.show_notepad():
            index_note = self.view.get_index_note(self.notepad.size())
            self.notepad.del_note(index_note)
            self.model.add_to_file(self.notepad)

    def del_all(self):
        self.notepad.del_all()
        self.model.add_to_file(self.notepad)

    def show_note(self):
        if self.show_notepad():
            index_note = self.view.get_index_note(self.notepad.size())
            self.view.print_str(self.notepad.read_all()[index_note].__str__())

    def show_notepad(self):
        notes = self.notepad.read_all()
        if len(notes) > 0:
            i = 1
            for note in self.notepad.read_all():
                self.view.show_notepad(note.__repr__(), i)
                i += 1
            return True
        self.view.print_str("Записей еще нет")
        return False

    def filter_date(self):
        date = self.view.get_date()
        fit_notes = []
        for note in self.notepad.read_all():
            d = note.date_time
            if d.day == date.day and d.month == date.month and d.year == date.year:
                fit_notes.append(note)
        if len(fit_notes) > 0:
            i = 1
            for note in fit_notes:
                self.view.show_notepad(note.__repr__(), i)
                i += 1
        else:
            self.view.print_str("Подходящие записи не найдены")
