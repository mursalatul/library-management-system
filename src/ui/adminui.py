from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import sys

class AdminUI(QtWidgets.QMainWindow):
    """load admin ui
    it will be called from login page, when
    a admin will login
    """
    def __init__(self) -> None:
        super(AdminUI, self).__init__()
        # load the admin page ui
        loadUi("ui\\admin.ui", self)
        self.show()

class HandleAdminUI():
    def __init__(self) -> None:
        admin_ui_app = QtWidgets.QApplication(sys.argv)
        a = AdminUI()
        sys.exit(admin_ui_app.exec_())