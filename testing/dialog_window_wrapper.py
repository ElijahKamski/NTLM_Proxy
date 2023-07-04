#! /usr/bin/python

import requests
from PySide6.QtWidgets import QMainWindow

from testing import dialog_window


def send_get_request_through_http_localhost_proxy(url: str, port=5865):
    response = requests.get(url, proxies={"http": f"http://127.0.0.1:{port}"})
    return response


class DialogWindow(QMainWindow, dialog_window.Ui_Dialog):
    def __init__(self, port=5865, is_bypass=True):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.setup_config)
        self.conf = {}
        self.port = port
        self.is_bypass = is_bypass

    def setup_config(self):
        url = self.lineEdit.text()
        try:
            if self.is_bypass:
                response = requests.get(url)
            else:
                response = send_get_request_through_http_localhost_proxy(url, self.port)
            self.textBrowser.setText(response.text)
        except Exception as e:
            self.textBrowser.setText(str(e))
