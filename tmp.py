import toga
from toga.style.pack import Pack


class MyApp(toga.App):
    def startup(self):
        # Главное окно приложения
        self.main_window = toga.MainWindow(title="Пример InfoDialog")

        # Основной контейнер
        self.main_box = toga.Box(style=Pack(padding=10))

        # Кнопка для открытия InfoDialog
        self.info_button = toga.Button("Показать информацию", on_press=self.show_info_dialog, style=Pack(padding=5))

        # Добавляем кнопку в основной контейнер
        self.main_box.add(self.info_button)

        # Устанавливаем контент окна
        self.main_window.content = self.main_box
        self.main_window.show()

    def show_info_dialog(self, widget):
        # Создаем и показываем диалог с информацией
        info_dialog = toga.InfoDialog(
            title="Информация",
            message="Это пример использования InfoDialog в Toga.",
        )



if __name__ == "__main__":
    app = MyApp("InfoDialog Example", "org.beeware.toga.infodialog")
    app.main_loop()
