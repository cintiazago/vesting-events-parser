from src.protocols.notification import AbsNotification

"""
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Context.
"""


class AdminNotification(AbsNotification):
    def __init__(self):
        super().__init__()

    def notify_stdout(self, message: str):
        print(message)
