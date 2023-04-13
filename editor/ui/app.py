from editor.core.mvp.presenter import Presenter
from path_db import PATH_DB
from editor.core.mvp.model_json import ModelJSON
from editor.ui.view_console import ViewConsole


def app_note_editor():
    p = Presenter(ModelJSON(PATH_DB, "my_note"), ViewConsole())
    commands = ["add", "change", "open", "showall", "del", "delall", "searchdate",
                "lenpreview",  "exit"]
    flag = True
    p.view.print_str("Добро пожаловать в редактор заметок")
    p.view.print_str(f"Доступное количество заметок: {p.notepad.size()}")
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
            case 7: p.change_len_preview_text()
            case 8: flag = False
    p.view.print_str("\nЗавершение работы")
