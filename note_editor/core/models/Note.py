from datetime import datetime

class Note:
    def __init__(self, id: int, title, text, date_time: datetime):
        self.id = id
        self.title = title
        self.text = text
        self.date_time = date_time

    def get_note_info(self):
        return f'id_{self.id} title:{self.title}, date:{self.date_time.date()} ' \
               f'{self.date_time.time().hour}:{self.date_time.time().minute}\ntext:{self.text}'


new_note = Note(1, 'Note 1', 'Text 1', datetime.now())
print(new_note.get_note_info())
