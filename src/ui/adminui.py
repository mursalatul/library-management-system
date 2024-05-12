from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import sys
from data.window_instance import windows
class AdminUI(QtWidgets.QMainWindow):
    """load admin ui
    it will be called from login page, when
    a admin will login
    """
    def __init__(self) -> None:
        super(AdminUI, self).__init__()
        # load the admin page ui
        loadUi("ui\\admin.ui", self)
        # storing the window instance
        windows["adminui"] = self
        self.show()
        
        # load the field
        self._loadTheWidgets()
    
    def _loadTheWidgets(self):
        self.widget_main_options = self.findChild(
            QtWidgets.QWidget, "widget_main_options"
        )
