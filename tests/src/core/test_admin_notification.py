from src.core.admin_notification import AdminNotification


class TestNotifications:
    def setup_method(self, function):
        """Setup before each function"""
        print('\n\n[+] Test: "{}"'.format(function.__name__))
        print("    " + function.__doc__)

    def test_send_notification_with_valid_message(self, capsys):
        """assert 'Test message' was printed to console"""
        admin_notification = AdminNotification()
        message_mock = "Test message"
        admin_notification.notify_stdout(message_mock)

        out, _ = capsys.readouterr()
        assert message_mock in out
