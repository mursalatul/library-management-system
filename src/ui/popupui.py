from PyQt5.QtWidgets import QMessageBox


class MessageBox:
    """
    show pop up window with spacific text. Make sure you use setMessage method
    to show spacific text
    """

    def showMessage(self, message: str):
        self.msg_box = QMessageBox()
        self.msg_box.setText(message)
        x = self.msg_box.exec_()
