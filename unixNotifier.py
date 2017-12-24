# -*- coding: utf-8 -*-"

import notify2
import os


class UnixNotifier:
    """Class to push-notify on Unix-systems"""

    def __init__(self, title_text, timeout=1000):
        """Method-constructor for unix-notifier

        Args:
            title_text: common text for all messages of current instance.
            timeout: timeout of notifications.
        """
        self.ICON_PATH = os.getcwd() + "/batman.png"
        self.title_text = title_text

        # Инициализируем d-bus соединение
        notify2.init("Unix-system notifier")
        self.urgency = notify2.URGENCY_NORMAL
        self.timeout = timeout

    def notify(self, notify_text):
        """Method to show notification.

        Args:
            notify_text: notification's text.
        """
        text = self.title_text + "\n\n" + str(notify_text)

        notifier = notify2.Notification(text, icon=self.ICON_PATH)
        notifier.set_urgency(self.urgency)
        notifier.set_timeout(self.timeout)
        notifier.show()


UnixNotifier("There is new apartment in Minsk:").notify("Skr-skr")

