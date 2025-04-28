import toga
from toga.style.pack import COLUMN, ROW
from toga.style import Pack
import sqlite3


# сделать приложение "заметки"

#https://github.com/leonid1123/pk32_toga_2025
class Application(toga.App):
    def startup(self):
        self.notes_list_window = None
        self.style = Pack(padding=5, flex=1, font_family='Helvetica', font_size=16)
        self.main_window = toga.MainWindow(size=(600,200))
        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        self.login_box = toga.Box()
        self.login_box.style.update(direction=ROW)
        self.pass_box = toga.Box()
        self.pass_box.style.update(direction=ROW)
        self.btn_box = toga.Box()
        self.btn_box.style.update(direction=COLUMN)

        self.button = toga.Button("Вход в систему", on_press=self.button_handler, style=self.style)
        self.login_label = toga.Label("Логин", style=self.style)
        self.pass_label = toga.Label("Пароль", style=self.style)
        self.login_entry = toga.TextInput(style=self.style)
        self.pass_entry = toga.TextInput(style=self.style)
        self.error_label = toga.Label("Ошибки:", style=self.style)
        self.login_box.add(self.login_label)
        self.login_box.add(self.login_entry)

        self.pass_box.add(self.pass_label)
        self.pass_box.add(self.pass_entry)

        self.btn_box.add(self.button)
        self.btn_box.add(self.error_label)

        self.main_box.add(self.login_box)
        self.main_box.add(self.pass_box)
        self.main_box.add(self.btn_box)
        self.main_window.content = self.main_box

        self.cnx = sqlite3.connect("users.db")
        self.cursor = self.cnx.cursor()

        self.main_window.show()

    def button_handler(self, widget):
        user_login = self.login_entry.value
        user_password = self.pass_entry.value
        create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        );
        """
        self.cursor.execute(create_table_query)
        self.cnx.commit()

        self.cursor.execute("SELECT password FROM users WHERE login=?", (user_login,))
        self.cnx.commit()
        ans = self.cursor.fetchall()
        print(ans)
        if ans:
            tmp = ans[0]
            pass_tmp = tmp[0]
            print(pass_tmp)
            if pass_tmp == user_password:
                print("ok")
                self.notes_window()
            else:
                print("не ok")
        #сделать проверку пароля

    def notes_window(self):
        if self.notes_list_window is None:
            self.notes_list_window = toga.Window(title="Заметки")
            notes_window_box = toga.Box()
            notes_window_box.style.update(direction=COLUMN)
            self.note1 = toga.Button("Заметка №1", style=self.style, on_press=self.note)
            self.note2 = toga.Button("Заметка №2", style=self.style)
            self.note3 = toga.Button("Заметка №3", style=self.style)
            self.note4 = toga.Button("Заметка №4", style=self.style)
            self.note5 = toga.Button("Заметка №5", style=self.style)
            notes_window_box.add(self.note1)
            notes_window_box.add(self.note2)
            notes_window_box.add(self.note3)
            notes_window_box.add(self.note4)
            notes_window_box.add(self.note5)

            self.notes_list_window.content = notes_window_box
            self.notes_list_window.show()

    def note(self, widget):
        #сделать проверку на открытие окна
        #сделать таблицу с заметками
        self.note_win = toga.Window(title="Заметка")
        note_box = toga.Box()
        note_box.style.update(direction=COLUMN)
        self.note_view = toga.MultilineTextInput(style=self.style)
        note_btn = toga.Button("OK", style=self.style, on_press=self.ok_note_button)
        note_box.add(self.note_view)
        note_box.add(note_btn)
        self.note_win.content = note_box
        self.note_win.show()

    def ok_note_button(self):
        txt = self.note_view.value
        sql = ""
        params = (self.id_user,txt) #нужно получит ID пользователя
        self.cursor.execute(sql,params)
        self.cnx.commit()
        self.note_win.close()




app = Application("myApp", "myApp")
app.main_loop()
