import pytest

from src.protocols.notification import AbsNotification


class MockNotification(AbsNotification):
    def __init__(self):
        super().__init__()

    def notify_stdout(self, message: str):
        return super().notify_stdout(message)


class TestAbsNotification:
    def setup_method(self, function):
        """Setup before each function"""
        print('\n\n[+] Test: "{}"'.format(function.__name__))
        print("    " + function.__doc__)

    def test_instatiation_of_concrete_class_without_nofitfy_stdout_method_implemented(
        self, capsys
    ):
        """
        assert if AbsNotification interface raises NotImplementedError
        when notify_stdout method is not implemented
        """
        with pytest.raises(NotImplementedError):
            mock_notification = MockNotification()
            mock_message = "fake-message"
            mock_notification.notify_stdout(mock_message)
