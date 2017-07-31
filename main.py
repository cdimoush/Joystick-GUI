import os
import htmlPy
# Import back-end functionalities
from back_end_codes.back_end import ClassName
# from PyQt5 import QtGui


# Initial confiurations
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# GUI initializations
app = htmlPy.AppGUI(title=u"Application", maximized=True, plugins=True)


# GUI configurations
app.static_path = os.path.join(BASE_DIR, "static/")
app.template_path = os.path.join(BASE_DIR, "templates/")

app.web_app.setMinimumWidth(1024)
app.web_app.setMinimumHeight(768)
# app.window.setWindowIcon(QtGui.QIcon(BASE_DIR + "/static/img/icon.png"))

# Binding of back-end functionalities with GUI
# Register back-end functionalities
app.bind(ClassName(app))

app.template = ("index.html", {})


# Instructions for running application
if __name__ == "__main__":
    # The driver file will have to be imported everywhere in back-end.
    # So, always keep app.start() in if __name__ == "__main__" conditional
    app.start()
