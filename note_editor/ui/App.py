from JoinJob2NoteEditor.note_editor.core.mvp.Presenter import Presenter
from JoinJob2NoteEditor.note_editor.path_db import PATH_DB
from JoinJob2NoteEditor.note_editor.core.mvp.ModelJSON import ModelJSON
from JoinJob2NoteEditor.note_editor.ui.ViewConsole import ViewConsole


def app_note_editor():
    p = Presenter(ModelJSON(PATH_DB, "my_note"), ViewConsole())
    commands = ["add", "change", "open", "showall", "del", "delall", "searchdate", "exit"]
    flag = True
    p.view.print_str("Добро пожаловать в редактор заметок")
    while flag:
        p.view.show_commands(commands)
        index = p.view.get_index_command(commands)
        match index:
            case 0: p.add_new_note()
            case 1: p.change_note()
            case 2: p.show_note()
            case 3: p.show_notepad()
            case 4: p.del_note()
            case 5: p.del_all()
            case 6: p.filter_date()
            case 7: flag = False
    p.view.print_str("Завершение работы")
