"""
State

* The State pattern allows an object to change its behavior when its internal
  state changes.
* This pattern is useful when you want to avoid using large conditional
  statements to manage state transitions.
* It allows you to encapsulate state-specific behavior in separate classes,
  making the code more maintainable and easier to understand.
"""


###############################################################################
# State
###############################################################################


# Importing modules
# * We will import some resources to be used in the example below.
from abc import ABC, abstractmethod


# State
# * The State interface defines the methods that will be implemented by the
#   concrete states.
# * In this case, it is the Edit, Publish, and Unpublish methods that will be
#   called when the post changes state.
class PostState(ABC):
    @abstractmethod
    def edit(self, content: str) -> None:
        pass

    @abstractmethod
    def publish(self) -> None:
        pass

    @abstractmethod
    def unpublish(self) -> None:
        pass


# Post
# * The Post class is the context that will change its state based on the
#   current state.
# * It contains a reference to the current state and the content of the post.
class Post:
    def __init__(self) -> None:
        self.content = ''
        self.state = DraftState(self)

    def edit(self, content: str) -> None:
        self.state.edit(content)

    def publish(self) -> None:
        self.state.publish()

    def unpublish(self) -> None:
        self.state.unpublish()


# Draft State
# * The DraftState represents the state of a post that is being edited.
class DraftState(PostState):
    def __init__(self, post: Post) -> None:
        self.post = post

    def edit(self, content: str) -> None:
        self.post.content = content
        print('Post edited')

    def publish(self) -> None:
        self.post.state = PublishedState(self.post)
        print('Post published')

    def unpublish(self) -> None:
        print('Cannot unpublish a draft post')


# Published State
# * The PublishedState represents the state of a post that has been published.
class PublishedState(PostState):
    def __init__(self, post: Post) -> None:
        self.post = post

    def edit(self, content: str) -> None:
        print('Cannot edit a published post')

    def publish(self) -> None:
        print('Post is already published')

    def unpublish(self) -> None:
        self.post.state = DraftState(self.post)
        print('Post unpublished')


# Testing
# * Now, look that the post performs state transitions based on the current
#   state.
post = Post()                  # Output:
post.edit('Hello, World!')     # Post edited
post.publish()                 # Post published
post.edit('Hello, Universe!')  # Cannot edit a published post
post.unpublish()               # Post unpublished
post.edit('Hello, Galaxy!')    # Post edited
post.publish()                 # Post published
post.publish()                 # Post is already published
