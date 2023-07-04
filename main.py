#! /usr/bin/python

import sys
import threading
import signal

from PySide6.QtWidgets import QMainWindow, QApplication

from lib import config, config_affairs, server

import __init__
from testing import main_window
from testing import dialog_window_wrapper


class MainWindowNTLM(QMainWindow, main_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.pop_up = None
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.ConnectButton.clicked.connect(self.setup_config)
        self.conf = {}

    def parse_config(self):
        conf = {}
        *proxy, port = self.ProxyPortField.text().split(':')
        conf['url'] = ':'.join(proxy)
        conf['port'] = port
        conf['domain'] = self.DomainField.text()
        conf['login'] = self.LoginField.text()
        conf['password'] = self.PasswordField.text()
        return conf

    def setup_config(self):
        parsed_config = self.parse_config()
        self.conf = config.server_config
        self.conf['GENERAL']['PARENT_PROXY'] = parsed_config['url']
        self.conf['GENERAL']['PARENT_PROXY_PORT'] = parsed_config['port']
        self.conf['NTLM_AUTH']['NT_DOMAIN'] = parsed_config['domain']
        self.conf['NTLM_AUTH']['USER'] = parsed_config['login']
        self.conf['NTLM_AUTH']['PASSWORD'] = parsed_config['password']
        self.conf['GENERAL']['VERSION'] = '0.9.9.0.1'
        if (self.conf['GENERAL']['PARENT_PROXY'].strip()):
            config_result = config_affairs.arrange(self.conf)

            # --------------------------------------------------------------
            # let's run it

            serv = server.AuthProxyServer(config_result)

            signal.signal(signal.SIGINT, serv.sigHandler)

            threading.Thread(target=serv.run).start()
            self.pop_up = dialog_window_wrapper.DialogWindow(self.conf['GENERAL']['LISTEN_PORT'])
        else:
            self.conf['GENERAL']['PARENT_PROXY'] = '0.0.0.0'
            self.conf['GENERAL']['PARENT_PROXY_PORT'] = 80
            self.pop_up = dialog_window_wrapper.DialogWindow(self.conf['GENERAL']['LISTEN_PORT'])

        self.pop_up.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindowNTLM()
    window.show()

    sys.exit(app.exec())
