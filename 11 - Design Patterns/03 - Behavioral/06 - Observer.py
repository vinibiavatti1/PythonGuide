"""
Observer

* The Observer pattern defines a one-to-many dependency between objects so that
  when one object changes state, all its dependents are notified and updated
  automatically.
* This pattern is useful when you want to maintain a consistent state across
  multiple objects without tightly coupling them.
"""


###############################################################################
# Observer
###############################################################################


# Importing modules
# * We will import some resources to be used in the example below.
from abc import ABC, abstractmethod


# Observer
# * The Observer interface defines the method that will be called when the
#   subject changes state.
class Observer(ABC):
    @abstractmethod
    def notify(self, message: str) -> None:
        pass


# Email Service
# * The class below represents the publisher in the Observer pattern.
# * The Publisher is the subject that maintains a list of subscribers and
#   notifies them when its state changes.
class EmailService:
    def __init__(self) -> None:
        self.observers: list[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        self.observers.append(observer)

    def send_email(self, to: str) -> None:
        print(f'Sending email to: {to}...')
        for observer in self.observers:
            observer.notify(f'Email sent to {to}')


# Metrics Service
# * The MetricsService class is an observer that tracks email sending metrics.
class MetricsService(Observer):
    def notify(self, message: str) -> None:
        print(f'MetricsService received notification: {message}')


# Logging Service
# * The LoggingService class is an observer that logs email sending events.
class LoggingService(Observer):
    def notify(self, message: str) -> None:
        print(f'LoggingService received notification: {message}')


# Testing
# * Now, we will create an email service and subscribe two observers to it.
# * Note that when an email is sent, both observers receive the notification.
email_service = EmailService()
metrics_service = MetricsService()
logging_service = LoggingService()
email_service.subscribe(metrics_service)
email_service.subscribe(logging_service)
email_service.send_email('user@example.com')
# Sending email to: user@example.com...
# MetricsService received notification: Email sent to user@example.com
# LoggingService received notification: Email sent to user@example.com
