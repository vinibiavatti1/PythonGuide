"""
Mediator

* Mediator is a behavioral design pattern that allows objects to communicate
  with each other without knowing about each other.
* It defines an object that encapsulates how a set of objects interact.
* This pattern is useful when you want to reduce the complexity of
  communication between multiple objects.
"""


###############################################################################
# Mediator
###############################################################################


# Form
# * The class below represents a form with submit and reset functionality.
# * It acts as the mediator between the buttons and the form.
class Form:
    def notify(self, event: str) -> None:
        if event == 'submit':
            print('Form submitted')
        elif event == 'reset':
            print('Form reset')


# Submit Button
# * The class below represents a submit button in the form.
class SubmitButton:
    def __init__(self, form: Form) -> None:
        self.form = form

    def click(self) -> None:
        self.form.notify('submit')


# Reset Button
# * The class below represents a reset button in the form.
class ResetButton:
    def __init__(self, form: Form) -> None:
        self.form = form

    def click(self) -> None:
        self.form.notify('reset')


# Testing
# * Now, note that the form acts as a mediator between the buttons. When a
#   button is clicked, the form is notified.
form = Form()
submit_button = SubmitButton(form)
reset_button = ResetButton(form)
submit_button.click()
reset_button.click()
# Form submitted
# Form reset
