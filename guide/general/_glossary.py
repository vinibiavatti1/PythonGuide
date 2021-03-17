"""
Python's Glossary

* Reference:
  * https://docs.python.org/3/glossary.html#term-method-resolution-order

###############################################################################
Word                Description
###############################################################################

>>>:                The default Python prompt of the interactive shell. Often
                    seen for code examples which can be executed interactively
                    in the interpreter

ABC:                (Abstract Base Class) complement duck-typing by providing a
                    way to define interfaces when other techniques like
                    hasattr() would be clumsy or subtly wrong (for example with
                    magic methods). ABCs introduce virtual subclasses, which
                    are classes that don’t inherit from a class but are still
                    recognized by isinstance() and issubclass(); see the abc
                    module documentation. Python comes with many built-in ABCs
                    for data structures (in the collections.abc module),
                    numbers (in the numbers module), streams (in the io
                    module), import finders and loaders (in the importlib.abc
                    module). You can create your own ABCs with the abc module

Annotation:         A label associated with a variable, a class attribute or a
                    function parameter or return value, used by convention as a
                    type hint. like: def(a: int, b: str) -> int: ...

Argument:           A value passed to a function (or method) when calling the
                    function. There are two kinds of argument: Positional
                    argument and keyword argument

BDFL:               Benevolent Dictator For Life, a.k.a. Guido van Rossum,
                    Python's creator.

Callback:           A subroutine function which is passed as an argument to be
                    executed at some point in the future.

Class variable:     A variable defined in a class and intended to be modified
                    only at class level (i.e., not in an instance of the class)

Coercion:           The implicit conversion of an instance of one type to
                    another during an operation which involves two arguments of
                    the same type. For example, int(3.15) converts the floating
                    point number to the integer 3, but in 3+4.5, each argument
                    is of a different type (one int, one float), and both must
                    be converted to the same type before they can be added or
                    it will raise a TypeError. Without coercion, all arguments
                    of even compatible types would have to be normalized to the
                    same value by the programmer, e.g., float(3)+4.5 rather
                    than just 3+4.5

Complex number:     An extension of the familiar real number system in which
                    all numbers are expressed as a sum of a real part and an
                    imaginary part. Imaginary numbers are real multiples of the
                    imaginary unit (the square root of -1), often written i in
                    mathematics or j in engineering

Context manager:    An object which controls the environment seen in a with
                    statement by defining __enter__() and __exit__() methods.
                    See PEP 343

Coroutine:          Coroutines are a more generalized form of subroutines.
                    Subroutines are entered at one point and exited at another
                    point. Coroutines can be entered, exited, and resumed at
                    many different points. They can be implemented with the
                    async def statement. See also PEP 492

CPython:            The canonical implementation of the Python programming
                    language, as distributed on python.org. The term "CPython"
                    is used when necessary to distinguish this implementation
                    from others such as Jython or IronPython

Decorator:          A function returning another function, usually applied as a
                    function transformation using the @wrapper syntax. Common
                    examples for decorators are classmethod() and
                    staticmethod()

Descriptor:         Any object which defines the methods __get__(), __set__(),
                    or __delete__(). When a class attribute is a descriptor,
                    its special binding behavior is triggered upon attribute
                    lookup. Normally, using a.b to get, set or delete an
                    attribute looks up the object named b in the class
                    dictionary for a, but if b is a descriptor, the respective
                    descriptor method gets called. Understanding descriptors is
                    a key to a deep understanding of Python because they are
                    the basis for many features including functions, methods,
                    properties, class methods, static methods, and reference to
                    super classes

Dictionary:         An associative array, where arbitrary keys are mapped to
                    values. dct = {'name': 'John'}

Dictionary view:    The objects returned from dict.keys(), dict.values(), and
                    dict.items() are called dictionary views. They provide a
                    dynamic view on the dictionary’s entries, which means that
                    when the dictionary changes, the view reflects these
                    changes. To force the dictionary view to become a full list
                    use list(dictview). See Dictionary view objects

Docstring:          A string literal which appears as the first expression in a
                    class, function or module. While ignored when the suite is
                    executed, it is recognized by the compiler and put into the
                    __doc__ attribute of the enclosing class, function or
                    module

Extension module:   A module written in C or C++, using Python’s C API to
                    interact with the core and with user code.

f-string:           String literals prefixed with 'f' or 'F' are commonly
                    called "f-strings" which is short for formatted string
                    literals

Floor division:     Mathematical division that rounds down to nearest integer.
                    The floor division operator is //

__future__:         A pseudo-module which programmers can use to enable new
                    language features which are not compatible with the current
                    interpreter. Check _future.py

Garbage collection: The process of freeing memory when it is not used anymore.
                    Python performs garbage collection via reference counting
                    and a cyclic garbage collector that is able to detect and
                    break reference cycles. The garbage collector can be
                    controlled using the gc module

Generator:          A function which returns a generator iterator. It looks
                    like a normal function except that it contains yield
                    expressions for producing a series of values usable in a
                    for-loop or that can be retrieved one at a time with the
                    next() function

GIL:                (Global Interpreter Lock) The mechanism used by the CPython
                    interpreter to assure that only one thread executes Python
                    bytecode at a time. This simplifies the CPython
                    implementation by making the object model (including
                    critical built-in types such as dict) implicitly safe
                    against concurrent access

Hashable:           An object is hashable if it has a hash value which never
                    changes during its lifetime (it needs a __hash__() method),
                    and can be compared to other objects (it needs an __eq__()
                    method). Hashable objects which compare equal must have the
                    same hash value

IDLE:               An Integrated Development Environment for Python. IDLE is a
                    basic editor and interpreter environment which ships with
                    the standard distribution of Python

Iterator:           An object representing a stream of data. Repeated calls to
                    the iterator's __next__() method (or passing it to the
                    built-in function next()) return successive items in the
                    stream

keyword argument:   An argument preceded by an identifier (e.g. name=) in a
                    function call or passed as a value in a dictionary preceded
                    by **

Lambda:             An anonymous inline function consisting of a single
                    expression which is evaluated when the function is called
                    Check _lambda.py

Comprehension:      A compact way to process all or part of the elements in a
                    sequence and return a list with the results

Magic method:       A method that is called implicitly by Python to execute a
                    certain operation on a type, such as addition. Such methods
                    have names starting and ending with double underscores

Metaclass:          The class of a class. Class definitions create a class
                    name, a class dictionary, and a list of base classes. The
                    metaclass is responsible for taking those three arguments
                    and creating the class. Most object oriented programming
                    languages provide a default implementation. What makes
                    Python special is that it is possible to create custom
                    metaclasses. Most users never need this tool, but when the
                    need arises, metaclasses can provide powerful, elegant
                    solutions. They have been used for logging attribute
                    access, adding thread-safety, tracking object creation,
                    implementing singletons, and many other tasks.
                    Check _class_metaclass.py

MRO:                Method Resolution Order is the order in which base classes
                    are searched for a member during lookup. Check _super.py

Named tuple:        The term "named tuple" applies to any type or class that
                    inherits from tuple and whose indexable elements are also
                    accessible using named attributes. The type or class may
                    have other features as well

Package:            A Python module which can contain submodules or
                    recursively, subpackages. Technically, a package is a
                    Python module with an __path__ attribute

PDB:                (Python Debugger) The module pdb defines an interactive
                    source code debugger for Python programs. It supports
                    setting (conditional) breakpoints and single stepping at
                    the source line level, inspection of stack frames, source
                    code listing, and evaluation of arbitrary Python code in
                    the context of any stack frame. It also supports
                    post-mortem debugging and can be called under program
                    control

PEP:                Python Enhancement Proposal. A PEP is a design document
                    providing information to the Python community, or
                    describing a new feature for Python or its processes or
                    environment. PEPs should provide a concise technical
                    specification and a rationale for proposed features

Pythonic:           An idea or piece of code which closely follows the most
                    common idioms of the Python language, rather than
                    implementing code using concepts common to other languages

__slots__:          A declaration inside a class that saves memory by
                    pre-declaring space for instance attributes and eliminating
                    instance dictionaries. Though popular, the technique is
                    somewhat tricky to get right and is best reserved for rare
                    cases where there are large numbers of instances in a
                    memory-critical application

Sequence:           An iterable which supports efficient element access using
                    integer indices via the __getitem__() special method and
                    defines a __len__() method that returns the length of the
                    sequence. Some built-in sequence types are list, str,
                    tuple, and bytes. Note that dict also supports
                    __getitem__() and __len__(), but is considered a mapping
                    rather than a sequence because the lookups use arbitrary
                    immutable keys rather than integers

Type:               The type of a Python object determines what kind of object
                    it is; every object has a type. An object's type is
                    accessible as its __class__ attribute or can be retrieved
                    with type(obj)

Venv:               (Virtual Environment) A cooperatively isolated runtime
                    environment that allows Python users and applications to
                    install and upgrade Python distribution packages without
                    interfering with the behaviour of other Python applications
                    running on the same system

Zen of Python:      Listing of Python design principles and philosophies that
                    are helpful in understanding and using the language. The
                    listing can be found by typing "import this" at the
                    interactive prompt

###############################################################################
"""
