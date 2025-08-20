"""
Visitor

* The Visitor pattern is a design pattern that lets you separate algorithms
  from the objects on which they operate.
* It allows you to add new operations to existing object structures without
  modifying the structures themselves.
"""


###############################################################################
# Visitor
###############################################################################


# Importing modules
# * We will import some resources to be used in the example below.
from abc import ABC, abstractmethod


# Visitor
# * The Concrete Visitor implements the Visitor interface and provides the
#   logic for processing each element type.
# * In this case, we have a visitor that exports the shapes to SVG format.
class ShapeVisitor(ABC):
    @abstractmethod
    def visit_dot(self, dot):
        pass

    @abstractmethod
    def visit_circle(self, circle):
        pass

    @abstractmethod
    def visit_rect(self, rect):
        pass


# SVG Export Visitor
# * The Concrete Visitor implements the Visitor interface and provides the
#   logic for processing each element type.
# * In this case, we have a visitor that exports the shapes to SVG format.
class SVGExportVisitor(ShapeVisitor):
    def visit_dot(self, dot):
        print("<dot/>")

    def visit_circle(self, circle):
        print("<circle/>")

    def visit_rect(self, rect):
        print("<rect/>")


# Shape
# * The interface below represents the element that can be visited by a
#   visitor.
# * The visitor will implement the logic for processing the element.
class Shape(ABC):
    @abstractmethod
    def accept(self, visitor: ShapeVisitor) -> None:
        pass


# Dot
# * The class below represents a concrete element that can be visited by a
#   visitor.
class Dot(Shape):
    def accept(self, visitor: ShapeVisitor) -> None:
        visitor.visit_dot(self)


# Circle
# * The class below represents a concrete element that can be visited by a
#   visitor.
class Circle(Shape):
    def accept(self, visitor: ShapeVisitor) -> None:
        visitor.visit_circle(self)


# Rect
# * The class below represents a concrete element that can be visited by a
#   visitor.
class Rect(Shape):
    def accept(self, visitor: ShapeVisitor) -> None:
        visitor.visit_rect(self)


# Testing
# * Now, we can see that each shape can be exported to SVG format without
#   modifying the shape classes.
dot = Dot()
circle = Circle()
rect = Rect()
exporter = SVGExportVisitor()
dot.accept(exporter)
circle.accept(exporter)
rect.accept(exporter)
# <dot/>
# <circle/>
# <rect/>
