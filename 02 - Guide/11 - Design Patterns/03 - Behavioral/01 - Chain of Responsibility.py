"""
Chain of Responsibility

* The Chain of Responsibility pattern is a behavioral design pattern that
  allows an object to pass a request along a chain of potential handlers until
  one of them handles the request.
* This pattern decouples the sender and receiver of a request, allowing
  multiple objects to handle the request without the sender needing to know
  which object will handle it.
"""


###############################################################################
# Chain of Responsibility
###############################################################################


# Importing modules
# * We will import some resources to be used in the example below.
from abc import ABC, abstractmethod


# Base Order Handler
# * Abstract class for handling order statuses
class BaseOrderHandler(ABC):
    @abstractmethod
    def handle(self, status: str) -> None:
        pass


# Order Handler
# * Concrete handler for processing orders.
# * This handler serves as the initial point of contact for order processing.
class OrderHandler(BaseOrderHandler):
    def __init__(self) -> None:
        self.next = CompleteOrderHandler()

    def handle(self, status: str) -> None:
        self.next.handle(status)


# Complete Order Handler
# * Concrete handler to process complete orders.
# * If the order is not complete, it passes the request to the next handler.
class CompleteOrderHandler(BaseOrderHandler):
    def __init__(self) -> None:
        self.next = WaitingOrderHandler()

    def handle(self, status: str) -> None:
        if status == 'complete':
            print(f"Processing {status} order...")
        else:
            self.next.handle(status)


# Waiting Order Handler
# * Concrete handler to process waiting orders.
# * If the order is not waiting, it passes the request to the next handler.
class WaitingOrderHandler(BaseOrderHandler):
    def __init__(self) -> None:
        self.next = FailedOrderHandler()

    def handle(self, status: str) -> None:
        if status == 'waiting':
            print(f"Processing {status} order...")
        else:
            self.next.handle(status)


# Failed Order Handler
# * Concrete handler to process failed orders.
# * If the order is not failed, it stops the processing.
class FailedOrderHandler(BaseOrderHandler):
    def handle(self, status: str) -> None:
        if status == 'failed':
            print(f"Processing {status} order...")
        else:
            print(f"Unknown order status: {status}")


# Testing
# * Now, we will process an order using the chain of responsibility.
# * Note that we call the entry point of the chain with the order status, and
#   the request is passed along the chain until it is handled.
order_handler = OrderHandler()
order_handler.handle('waiting')
# Processing waiting order...
