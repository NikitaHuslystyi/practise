import PyQt6
import PyQt6.QtCore as core
import PyQt6.QtWidgets as widgets

app = widgets.QApplication([])
window = widgets.QMainWindow()
window.setStyleSheet("background-color: purple")
screen = app.primaryScreen()
screen_size = screen.size()
screen_width = screen_size.width()
screen_height = screen_size.height()

window.setWindowTitle("practice")

window_width = 1080
window_height = 720

x = (screen_width//2) - (window_width//2)
y = (screen_height//2) - (window_height//2)


window.setGeometry(x, y, window_width, window_height)



window.show()
app.exec()