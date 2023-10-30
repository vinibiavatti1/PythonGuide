"""
Observer design pattern

* Book: GOF
* Observer is a behavioral design pattern that lets you define a subscription
  mechanism to notify multiple objects about any events that happen to the
  object they're observing.
* The object that has some interesting state is often called subject, but since
  it's also going to notify other objects about the changes to its state, we'll
  call it publisher. All other objects that want to track changes to the
  publisher's state are called subscribers.
"""
from abc import ABC, abstractmethod


# Subject ABC class
class Subject(ABC):
    @abstractmethod
    def subscribe(self, observer):
        pass

    @abstractmethod
    def unsubscribe(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


# Observer ABC class
class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass


# Mailer class (Subject)
class MailerSubject(Subject):
    def __init__(self, name):
        self._observers = []
        self.name = name

    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def send_mail(self):
        print('Email sent!')
        self.notify()


# Notification observer
class NotificationObserver(Observer):
    def update(self, subject):
        print(f"[Notification] Email sent from: {subject.name}")


# Algorithm
mailer1 = MailerSubject('Mailer 1')
mailer2 = MailerSubject('Mailer 2')

notification = NotificationObserver()

mailer1.subscribe(notification)
mailer2.subscribe(notification)

mailer1.send_mail()
# Email sent!
# [Notification] Email sent from: Mailer 1

mailer2.send_mail()
# Email sent!
# [Notification] Email sent from: Mailer 2
