import toga
from toga.style.pack import COLUMN, ROW
from toga.style import Pack
import sqlite3
# сделать приложение "заметки"


class Application(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow()
        self.main_box = toga.Box(style=Pack(direction=COLUMN))
        self.login_box = toga.Box()
        self.login_box.style.update(direction=ROW)
        self.pass_box = toga.Box()
        self.pass_box.style.update(direction=ROW)
        self.btn_box = toga.Box()
        self.btn_box.style.update(direction=COLUMN)

        self.button = toga.Button("Вход в систему", on_press=self.button_handler, style=Pack(padding=5, flex=1))
        self.login_label = toga.Label("Логин", style=Pack(padding=5, flex=1, font_family='Helvetica', font_size=16))
        self.pass_label = toga.Label("Пароль", style=Pack(padding=5, flex=1, font_family='Helvetica', font_size=16))
        self.login_entry = toga.TextInput(style=Pack(padding=5, flex=1))
        self.pass_entry = toga.TextInput(style=Pack(padding=5, flex=1))
        self.error_label = toga.Label("Ошибки:", style=Pack(padding=5, flex=1, font_family='Helvetica', font_size=16))
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


        self.cursor.execute("SELECT password FROM users WHERE login=?",(user_login,))
        self.cnx.commit()
        ans = self.cursor.fetchall()
        print(ans)
        if ans:
            tmp = ans[0]
            pass_tmp = tmp[0]
            print(pass_tmp)
            if pass_tmp == user_password:
                print("ok")
            else:
                print("не ok")
        #сделать проверку пароля


app = Application("myApp","myApp")
app.main_loop()


#https://ctxt.io/2/AAB4Kx_ZEQ
