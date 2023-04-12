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
        self.len_preview = self.notepad.get_len_short_text()
        self.parameters = ["Изменить заголовок", "Изменить текст заметки",
                           "Изменить заголовок и текст заметки"]

    def __str__(self):
        return f"{self.notepad}"

    def add_new_note(self):
        new_note = Note(self.view.get_note_title(),
                        self.view.get_note_text(),
                        datetime.now(), self.index,
                        self.len_preview)
        self.notepad.add_note(new_note)
        self.index += 1
        self.view.print_str(f"Заметка {new_note.show_id_title()} успешно создана")
        self.model.add_to_file(self.notepad)

    def change_note(self):
        if self.is_not_empty():
            index_note = self.get_index_note("Доступна одна заметка. Выбрать ее?")
            if index_note >= 0:
                select_note = self.notepad.read_note(index_note)
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
        if self.is_not_empty():
            index_note = self.get_index_note("Доступна одна заметка. Удалить?", True)
            if index_note >= 0:
                self.notepad.del_note(index_note)
                self.model.add_to_file(self.notepad)
                self.view.print_str("Заметка удалена")

    def del_all(self):
        if self.is_not_empty():
            self.view.print_str(f"Удалить все заметки ({self.notepad.size()} шт.)?")
            if self.view.confirm_action():
                self.notepad.del_all()
                self.model.add_to_file(self.notepad)
                self.index = 1
                self.view.print_str("Все заметки удалены")

    def show_note(self):
        if self.is_not_empty():
            index_note = self.get_index_note("Доступна одна заметка. Открыть?")
            if index_note >= 0:
                self.view.print_str(self.notepad.read_note(index_note))

    def show_notepad(self):
        if self.is_not_empty():
            self.view.print_str("Список заметок")
            i = 1
            for note in self.notepad.read_all():
                self.view.show_notepad(note.__repr__(), i)
                i += 1

    def filter_date(self):
        if self.is_not_empty():
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

    def is_not_empty(self):
        if self.notepad.size() > 0:
            return True
        else:
            self.view.print_str("Записей еще нет")
            return False

    def get_index_note(self, msg: str, del_note=False) -> int:
        self.show_notepad()
        count = self.notepad.size()
        if count == 1:
            self.view.print_str(msg)
            if not self.view.confirm_action():
                return -1
            return 0
        else:
            index_note = self.view.get_index_note(count)
            if del_note:
                self.view.print_str(f"Удалить заметку "
                                    f"{self.notepad.read_note(index_note).show_id_title()}?")
                if not self.view.confirm_action():
                    return -1
            return index_note

    def change_len_preview_text(self):
        new_len = self.view.get_len_preview_text()
        if new_len != self.len_preview:
            self.len_preview = new_len
            for note in self.notepad.read_all():
                note.short_text = self.len_preview
            self.model.add_to_file(self.notepad)
            self.view.print_str("Настройки изменены")
        else:
            self.view.print_str("Оставлены текущие настройки")

