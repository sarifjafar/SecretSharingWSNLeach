# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _genetic_algorithm
else:
    import _genetic_algorithm

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _genetic_algorithm.delete_SwigPyIterator

    def value(self):
        return _genetic_algorithm.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _genetic_algorithm.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _genetic_algorithm.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _genetic_algorithm.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _genetic_algorithm.SwigPyIterator_equal(self, x)

    def copy(self):
        return _genetic_algorithm.SwigPyIterator_copy(self)

    def next(self):
        return _genetic_algorithm.SwigPyIterator_next(self)

    def __next__(self):
        return _genetic_algorithm.SwigPyIterator___next__(self)

    def previous(self):
        return _genetic_algorithm.SwigPyIterator_previous(self)

    def advance(self, n):
        return _genetic_algorithm.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _genetic_algorithm.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _genetic_algorithm.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _genetic_algorithm.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _genetic_algorithm.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _genetic_algorithm.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _genetic_algorithm.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _genetic_algorithm:
_genetic_algorithm.SwigPyIterator_swigregister(SwigPyIterator)

class vector0(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _genetic_algorithm.vector0_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _genetic_algorithm.vector0___nonzero__(self)

    def __bool__(self):
        return _genetic_algorithm.vector0___bool__(self)

    def __len__(self):
        return _genetic_algorithm.vector0___len__(self)

    def __getslice__(self, i, j):
        return _genetic_algorithm.vector0___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _genetic_algorithm.vector0___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _genetic_algorithm.vector0___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _genetic_algorithm.vector0___delitem__(self, *args)

    def __getitem__(self, *args):
        return _genetic_algorithm.vector0___getitem__(self, *args)

    def __setitem__(self, *args):
        return _genetic_algorithm.vector0___setitem__(self, *args)

    def pop(self):
        return _genetic_algorithm.vector0_pop(self)

    def append(self, x):
        return _genetic_algorithm.vector0_append(self, x)

    def empty(self):
        return _genetic_algorithm.vector0_empty(self)

    def size(self):
        return _genetic_algorithm.vector0_size(self)

    def swap(self, v):
        return _genetic_algorithm.vector0_swap(self, v)

    def begin(self):
        return _genetic_algorithm.vector0_begin(self)

    def end(self):
        return _genetic_algorithm.vector0_end(self)

    def rbegin(self):
        return _genetic_algorithm.vector0_rbegin(self)

    def rend(self):
        return _genetic_algorithm.vector0_rend(self)

    def clear(self):
        return _genetic_algorithm.vector0_clear(self)

    def get_allocator(self):
        return _genetic_algorithm.vector0_get_allocator(self)

    def pop_back(self):
        return _genetic_algorithm.vector0_pop_back(self)

    def erase(self, *args):
        return _genetic_algorithm.vector0_erase(self, *args)

    def __init__(self, *args):
        _genetic_algorithm.vector0_swiginit(self, _genetic_algorithm.new_vector0(*args))

    def push_back(self, x):
        return _genetic_algorithm.vector0_push_back(self, x)

    def front(self):
        return _genetic_algorithm.vector0_front(self)

    def back(self):
        return _genetic_algorithm.vector0_back(self)

    def assign(self, n, x):
        return _genetic_algorithm.vector0_assign(self, n, x)

    def resize(self, *args):
        return _genetic_algorithm.vector0_resize(self, *args)

    def insert(self, *args):
        return _genetic_algorithm.vector0_insert(self, *args)

    def reserve(self, n):
        return _genetic_algorithm.vector0_reserve(self, n)

    def capacity(self):
        return _genetic_algorithm.vector0_capacity(self)
    __swig_destroy__ = _genetic_algorithm.delete_vector0

# Register vector0 in _genetic_algorithm:
_genetic_algorithm.vector0_swigregister(vector0)

class regions_t(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _genetic_algorithm.regions_t_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _genetic_algorithm.regions_t___nonzero__(self)

    def __bool__(self):
        return _genetic_algorithm.regions_t___bool__(self)

    def __len__(self):
        return _genetic_algorithm.regions_t___len__(self)

    def __getslice__(self, i, j):
        return _genetic_algorithm.regions_t___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _genetic_algorithm.regions_t___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _genetic_algorithm.regions_t___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _genetic_algorithm.regions_t___delitem__(self, *args)

    def __getitem__(self, *args):
        return _genetic_algorithm.regions_t___getitem__(self, *args)

    def __setitem__(self, *args):
        return _genetic_algorithm.regions_t___setitem__(self, *args)

    def pop(self):
        return _genetic_algorithm.regions_t_pop(self)

    def append(self, x):
        return _genetic_algorithm.regions_t_append(self, x)

    def empty(self):
        return _genetic_algorithm.regions_t_empty(self)

    def size(self):
        return _genetic_algorithm.regions_t_size(self)

    def swap(self, v):
        return _genetic_algorithm.regions_t_swap(self, v)

    def begin(self):
        return _genetic_algorithm.regions_t_begin(self)

    def end(self):
        return _genetic_algorithm.regions_t_end(self)

    def rbegin(self):
        return _genetic_algorithm.regions_t_rbegin(self)

    def rend(self):
        return _genetic_algorithm.regions_t_rend(self)

    def clear(self):
        return _genetic_algorithm.regions_t_clear(self)

    def get_allocator(self):
        return _genetic_algorithm.regions_t_get_allocator(self)

    def pop_back(self):
        return _genetic_algorithm.regions_t_pop_back(self)

    def erase(self, *args):
        return _genetic_algorithm.regions_t_erase(self, *args)

    def __init__(self, *args):
        _genetic_algorithm.regions_t_swiginit(self, _genetic_algorithm.new_regions_t(*args))

    def push_back(self, x):
        return _genetic_algorithm.regions_t_push_back(self, x)

    def front(self):
        return _genetic_algorithm.regions_t_front(self)

    def back(self):
        return _genetic_algorithm.regions_t_back(self)

    def assign(self, n, x):
        return _genetic_algorithm.regions_t_assign(self, n, x)

    def resize(self, *args):
        return _genetic_algorithm.regions_t_resize(self, *args)

    def insert(self, *args):
        return _genetic_algorithm.regions_t_insert(self, *args)

    def reserve(self, n):
        return _genetic_algorithm.regions_t_reserve(self, n)

    def capacity(self):
        return _genetic_algorithm.regions_t_capacity(self)
    __swig_destroy__ = _genetic_algorithm.delete_regions_t

# Register regions_t in _genetic_algorithm:
_genetic_algorithm.regions_t_swigregister(regions_t)

class individual_t(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _genetic_algorithm.individual_t_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _genetic_algorithm.individual_t___nonzero__(self)

    def __bool__(self):
        return _genetic_algorithm.individual_t___bool__(self)

    def __len__(self):
        return _genetic_algorithm.individual_t___len__(self)

    def __getslice__(self, i, j):
        return _genetic_algorithm.individual_t___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _genetic_algorithm.individual_t___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _genetic_algorithm.individual_t___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _genetic_algorithm.individual_t___delitem__(self, *args)

    def __getitem__(self, *args):
        return _genetic_algorithm.individual_t___getitem__(self, *args)

    def __setitem__(self, *args):
        return _genetic_algorithm.individual_t___setitem__(self, *args)

    def pop(self):
        return _genetic_algorithm.individual_t_pop(self)

    def append(self, x):
        return _genetic_algorithm.individual_t_append(self, x)

    def empty(self):
        return _genetic_algorithm.individual_t_empty(self)

    def size(self):
        return _genetic_algorithm.individual_t_size(self)

    def swap(self, v):
        return _genetic_algorithm.individual_t_swap(self, v)

    def begin(self):
        return _genetic_algorithm.individual_t_begin(self)

    def end(self):
        return _genetic_algorithm.individual_t_end(self)

    def rbegin(self):
        return _genetic_algorithm.individual_t_rbegin(self)

    def rend(self):
        return _genetic_algorithm.individual_t_rend(self)

    def clear(self):
        return _genetic_algorithm.individual_t_clear(self)

    def get_allocator(self):
        return _genetic_algorithm.individual_t_get_allocator(self)

    def pop_back(self):
        return _genetic_algorithm.individual_t_pop_back(self)

    def erase(self, *args):
        return _genetic_algorithm.individual_t_erase(self, *args)

    def __init__(self, *args):
        _genetic_algorithm.individual_t_swiginit(self, _genetic_algorithm.new_individual_t(*args))

    def push_back(self, x):
        return _genetic_algorithm.individual_t_push_back(self, x)

    def front(self):
        return _genetic_algorithm.individual_t_front(self)

    def back(self):
        return _genetic_algorithm.individual_t_back(self)

    def assign(self, n, x):
        return _genetic_algorithm.individual_t_assign(self, n, x)

    def resize(self, *args):
        return _genetic_algorithm.individual_t_resize(self, *args)

    def insert(self, *args):
        return _genetic_algorithm.individual_t_insert(self, *args)

    def reserve(self, n):
        return _genetic_algorithm.individual_t_reserve(self, n)

    def capacity(self):
        return _genetic_algorithm.individual_t_capacity(self)
    __swig_destroy__ = _genetic_algorithm.delete_individual_t

# Register individual_t in _genetic_algorithm:
_genetic_algorithm.individual_t_swigregister(individual_t)

class float_v(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _genetic_algorithm.float_v_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _genetic_algorithm.float_v___nonzero__(self)

    def __bool__(self):
        return _genetic_algorithm.float_v___bool__(self)

    def __len__(self):
        return _genetic_algorithm.float_v___len__(self)

    def __getslice__(self, i, j):
        return _genetic_algorithm.float_v___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _genetic_algorithm.float_v___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _genetic_algorithm.float_v___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _genetic_algorithm.float_v___delitem__(self, *args)

    def __getitem__(self, *args):
        return _genetic_algorithm.float_v___getitem__(self, *args)

    def __setitem__(self, *args):
        return _genetic_algorithm.float_v___setitem__(self, *args)

    def pop(self):
        return _genetic_algorithm.float_v_pop(self)

    def append(self, x):
        return _genetic_algorithm.float_v_append(self, x)

    def empty(self):
        return _genetic_algorithm.float_v_empty(self)

    def size(self):
        return _genetic_algorithm.float_v_size(self)

    def swap(self, v):
        return _genetic_algorithm.float_v_swap(self, v)

    def begin(self):
        return _genetic_algorithm.float_v_begin(self)

    def end(self):
        return _genetic_algorithm.float_v_end(self)

    def rbegin(self):
        return _genetic_algorithm.float_v_rbegin(self)

    def rend(self):
        return _genetic_algorithm.float_v_rend(self)

    def clear(self):
        return _genetic_algorithm.float_v_clear(self)

    def get_allocator(self):
        return _genetic_algorithm.float_v_get_allocator(self)

    def pop_back(self):
        return _genetic_algorithm.float_v_pop_back(self)

    def erase(self, *args):
        return _genetic_algorithm.float_v_erase(self, *args)

    def __init__(self, *args):
        _genetic_algorithm.float_v_swiginit(self, _genetic_algorithm.new_float_v(*args))

    def push_back(self, x):
        return _genetic_algorithm.float_v_push_back(self, x)

    def front(self):
        return _genetic_algorithm.float_v_front(self)

    def back(self):
        return _genetic_algorithm.float_v_back(self)

    def assign(self, n, x):
        return _genetic_algorithm.float_v_assign(self, n, x)

    def resize(self, *args):
        return _genetic_algorithm.float_v_resize(self, *args)

    def insert(self, *args):
        return _genetic_algorithm.float_v_insert(self, *args)

    def reserve(self, n):
        return _genetic_algorithm.float_v_reserve(self, n)

    def capacity(self):
        return _genetic_algorithm.float_v_capacity(self)
    __swig_destroy__ = _genetic_algorithm.delete_float_v

# Register float_v in _genetic_algorithm:
_genetic_algorithm.float_v_swigregister(float_v)

class vector1(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _genetic_algorithm.vector1_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _genetic_algorithm.vector1___nonzero__(self)

    def __bool__(self):
        return _genetic_algorithm.vector1___bool__(self)

    def __len__(self):
        return _genetic_algorithm.vector1___len__(self)

    def __getslice__(self, i, j):
        return _genetic_algorithm.vector1___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _genetic_algorithm.vector1___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _genetic_algorithm.vector1___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _genetic_algorithm.vector1___delitem__(self, *args)

    def __getitem__(self, *args):
        return _genetic_algorithm.vector1___getitem__(self, *args)

    def __setitem__(self, *args):
        return _genetic_algorithm.vector1___setitem__(self, *args)

    def pop(self):
        return _genetic_algorithm.vector1_pop(self)

    def append(self, x):
        return _genetic_algorithm.vector1_append(self, x)

    def empty(self):
        return _genetic_algorithm.vector1_empty(self)

    def size(self):
        return _genetic_algorithm.vector1_size(self)

    def swap(self, v):
        return _genetic_algorithm.vector1_swap(self, v)

    def begin(self):
        return _genetic_algorithm.vector1_begin(self)

    def end(self):
        return _genetic_algorithm.vector1_end(self)

    def rbegin(self):
        return _genetic_algorithm.vector1_rbegin(self)

    def rend(self):
        return _genetic_algorithm.vector1_rend(self)

    def clear(self):
        return _genetic_algorithm.vector1_clear(self)

    def get_allocator(self):
        return _genetic_algorithm.vector1_get_allocator(self)

    def pop_back(self):
        return _genetic_algorithm.vector1_pop_back(self)

    def erase(self, *args):
        return _genetic_algorithm.vector1_erase(self, *args)

    def __init__(self, *args):
        _genetic_algorithm.vector1_swiginit(self, _genetic_algorithm.new_vector1(*args))

    def push_back(self, x):
        return _genetic_algorithm.vector1_push_back(self, x)

    def front(self):
        return _genetic_algorithm.vector1_front(self)

    def back(self):
        return _genetic_algorithm.vector1_back(self)

    def assign(self, n, x):
        return _genetic_algorithm.vector1_assign(self, n, x)

    def resize(self, *args):
        return _genetic_algorithm.vector1_resize(self, *args)

    def insert(self, *args):
        return _genetic_algorithm.vector1_insert(self, *args)

    def reserve(self, n):
        return _genetic_algorithm.vector1_reserve(self, n)

    def capacity(self):
        return _genetic_algorithm.vector1_capacity(self)
    __swig_destroy__ = _genetic_algorithm.delete_vector1

# Register vector1 in _genetic_algorithm:
_genetic_algorithm.vector1_swigregister(vector1)

class vector2(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _genetic_algorithm.vector2_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _genetic_algorithm.vector2___nonzero__(self)

    def __bool__(self):
        return _genetic_algorithm.vector2___bool__(self)

    def __len__(self):
        return _genetic_algorithm.vector2___len__(self)

    def __getslice__(self, i, j):
        return _genetic_algorithm.vector2___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _genetic_algorithm.vector2___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _genetic_algorithm.vector2___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _genetic_algorithm.vector2___delitem__(self, *args)

    def __getitem__(self, *args):
        return _genetic_algorithm.vector2___getitem__(self, *args)

    def __setitem__(self, *args):
        return _genetic_algorithm.vector2___setitem__(self, *args)

    def pop(self):
        return _genetic_algorithm.vector2_pop(self)

    def append(self, x):
        return _genetic_algorithm.vector2_append(self, x)

    def empty(self):
        return _genetic_algorithm.vector2_empty(self)

    def size(self):
        return _genetic_algorithm.vector2_size(self)

    def swap(self, v):
        return _genetic_algorithm.vector2_swap(self, v)

    def begin(self):
        return _genetic_algorithm.vector2_begin(self)

    def end(self):
        return _genetic_algorithm.vector2_end(self)

    def rbegin(self):
        return _genetic_algorithm.vector2_rbegin(self)

    def rend(self):
        return _genetic_algorithm.vector2_rend(self)

    def clear(self):
        return _genetic_algorithm.vector2_clear(self)

    def get_allocator(self):
        return _genetic_algorithm.vector2_get_allocator(self)

    def pop_back(self):
        return _genetic_algorithm.vector2_pop_back(self)

    def erase(self, *args):
        return _genetic_algorithm.vector2_erase(self, *args)

    def __init__(self, *args):
        _genetic_algorithm.vector2_swiginit(self, _genetic_algorithm.new_vector2(*args))

    def push_back(self, x):
        return _genetic_algorithm.vector2_push_back(self, x)

    def front(self):
        return _genetic_algorithm.vector2_front(self)

    def back(self):
        return _genetic_algorithm.vector2_back(self)

    def assign(self, n, x):
        return _genetic_algorithm.vector2_assign(self, n, x)

    def resize(self, *args):
        return _genetic_algorithm.vector2_resize(self, *args)

    def insert(self, *args):
        return _genetic_algorithm.vector2_insert(self, *args)

    def reserve(self, n):
        return _genetic_algorithm.vector2_reserve(self, n)

    def capacity(self):
        return _genetic_algorithm.vector2_capacity(self)
    __swig_destroy__ = _genetic_algorithm.delete_vector2

# Register vector2 in _genetic_algorithm:
_genetic_algorithm.vector2_swigregister(vector2)

class dict_t(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _genetic_algorithm.dict_t_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _genetic_algorithm.dict_t___nonzero__(self)

    def __bool__(self):
        return _genetic_algorithm.dict_t___bool__(self)

    def __len__(self):
        return _genetic_algorithm.dict_t___len__(self)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()

    def __getitem__(self, key):
        return _genetic_algorithm.dict_t___getitem__(self, key)

    def __delitem__(self, key):
        return _genetic_algorithm.dict_t___delitem__(self, key)

    def has_key(self, key):
        return _genetic_algorithm.dict_t_has_key(self, key)

    def keys(self):
        return _genetic_algorithm.dict_t_keys(self)

    def values(self):
        return _genetic_algorithm.dict_t_values(self)

    def items(self):
        return _genetic_algorithm.dict_t_items(self)

    def __contains__(self, key):
        return _genetic_algorithm.dict_t___contains__(self, key)

    def key_iterator(self):
        return _genetic_algorithm.dict_t_key_iterator(self)

    def value_iterator(self):
        return _genetic_algorithm.dict_t_value_iterator(self)

    def __setitem__(self, *args):
        return _genetic_algorithm.dict_t___setitem__(self, *args)

    def asdict(self):
        return _genetic_algorithm.dict_t_asdict(self)

    def __init__(self, *args):
        _genetic_algorithm.dict_t_swiginit(self, _genetic_algorithm.new_dict_t(*args))

    def empty(self):
        return _genetic_algorithm.dict_t_empty(self)

    def size(self):
        return _genetic_algorithm.dict_t_size(self)

    def swap(self, v):
        return _genetic_algorithm.dict_t_swap(self, v)

    def begin(self):
        return _genetic_algorithm.dict_t_begin(self)

    def end(self):
        return _genetic_algorithm.dict_t_end(self)

    def rbegin(self):
        return _genetic_algorithm.dict_t_rbegin(self)

    def rend(self):
        return _genetic_algorithm.dict_t_rend(self)

    def clear(self):
        return _genetic_algorithm.dict_t_clear(self)

    def get_allocator(self):
        return _genetic_algorithm.dict_t_get_allocator(self)

    def count(self, x):
        return _genetic_algorithm.dict_t_count(self, x)

    def erase(self, *args):
        return _genetic_algorithm.dict_t_erase(self, *args)

    def find(self, x):
        return _genetic_algorithm.dict_t_find(self, x)

    def lower_bound(self, x):
        return _genetic_algorithm.dict_t_lower_bound(self, x)

    def upper_bound(self, x):
        return _genetic_algorithm.dict_t_upper_bound(self, x)
    __swig_destroy__ = _genetic_algorithm.delete_dict_t

# Register dict_t in _genetic_algorithm:
_genetic_algorithm.dict_t_swigregister(dict_t)

class map0(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _genetic_algorithm.map0_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _genetic_algorithm.map0___nonzero__(self)

    def __bool__(self):
        return _genetic_algorithm.map0___bool__(self)

    def __len__(self):
        return _genetic_algorithm.map0___len__(self)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()

    def __getitem__(self, key):
        return _genetic_algorithm.map0___getitem__(self, key)

    def __delitem__(self, key):
        return _genetic_algorithm.map0___delitem__(self, key)

    def has_key(self, key):
        return _genetic_algorithm.map0_has_key(self, key)

    def keys(self):
        return _genetic_algorithm.map0_keys(self)

    def values(self):
        return _genetic_algorithm.map0_values(self)

    def items(self):
        return _genetic_algorithm.map0_items(self)

    def __contains__(self, key):
        return _genetic_algorithm.map0___contains__(self, key)

    def key_iterator(self):
        return _genetic_algorithm.map0_key_iterator(self)

    def value_iterator(self):
        return _genetic_algorithm.map0_value_iterator(self)

    def __setitem__(self, *args):
        return _genetic_algorithm.map0___setitem__(self, *args)

    def asdict(self):
        return _genetic_algorithm.map0_asdict(self)

    def __init__(self, *args):
        _genetic_algorithm.map0_swiginit(self, _genetic_algorithm.new_map0(*args))

    def empty(self):
        return _genetic_algorithm.map0_empty(self)

    def size(self):
        return _genetic_algorithm.map0_size(self)

    def swap(self, v):
        return _genetic_algorithm.map0_swap(self, v)

    def begin(self):
        return _genetic_algorithm.map0_begin(self)

    def end(self):
        return _genetic_algorithm.map0_end(self)

    def rbegin(self):
        return _genetic_algorithm.map0_rbegin(self)

    def rend(self):
        return _genetic_algorithm.map0_rend(self)

    def clear(self):
        return _genetic_algorithm.map0_clear(self)

    def get_allocator(self):
        return _genetic_algorithm.map0_get_allocator(self)

    def count(self, x):
        return _genetic_algorithm.map0_count(self, x)

    def erase(self, *args):
        return _genetic_algorithm.map0_erase(self, *args)

    def find(self, x):
        return _genetic_algorithm.map0_find(self, x)

    def lower_bound(self, x):
        return _genetic_algorithm.map0_lower_bound(self, x)

    def upper_bound(self, x):
        return _genetic_algorithm.map0_upper_bound(self, x)
    __swig_destroy__ = _genetic_algorithm.delete_map0

# Register map0 in _genetic_algorithm:
_genetic_algorithm.map0_swigregister(map0)

class map1(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _genetic_algorithm.map1_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _genetic_algorithm.map1___nonzero__(self)

    def __bool__(self):
        return _genetic_algorithm.map1___bool__(self)

    def __len__(self):
        return _genetic_algorithm.map1___len__(self)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()

    def __getitem__(self, key):
        return _genetic_algorithm.map1___getitem__(self, key)

    def __delitem__(self, key):
        return _genetic_algorithm.map1___delitem__(self, key)

    def has_key(self, key):
        return _genetic_algorithm.map1_has_key(self, key)

    def keys(self):
        return _genetic_algorithm.map1_keys(self)

    def values(self):
        return _genetic_algorithm.map1_values(self)

    def items(self):
        return _genetic_algorithm.map1_items(self)

    def __contains__(self, key):
        return _genetic_algorithm.map1___contains__(self, key)

    def key_iterator(self):
        return _genetic_algorithm.map1_key_iterator(self)

    def value_iterator(self):
        return _genetic_algorithm.map1_value_iterator(self)

    def __setitem__(self, *args):
        return _genetic_algorithm.map1___setitem__(self, *args)

    def asdict(self):
        return _genetic_algorithm.map1_asdict(self)

    def __init__(self, *args):
        _genetic_algorithm.map1_swiginit(self, _genetic_algorithm.new_map1(*args))

    def empty(self):
        return _genetic_algorithm.map1_empty(self)

    def size(self):
        return _genetic_algorithm.map1_size(self)

    def swap(self, v):
        return _genetic_algorithm.map1_swap(self, v)

    def begin(self):
        return _genetic_algorithm.map1_begin(self)

    def end(self):
        return _genetic_algorithm.map1_end(self)

    def rbegin(self):
        return _genetic_algorithm.map1_rbegin(self)

    def rend(self):
        return _genetic_algorithm.map1_rend(self)

    def clear(self):
        return _genetic_algorithm.map1_clear(self)

    def get_allocator(self):
        return _genetic_algorithm.map1_get_allocator(self)

    def count(self, x):
        return _genetic_algorithm.map1_count(self, x)

    def erase(self, *args):
        return _genetic_algorithm.map1_erase(self, *args)

    def find(self, x):
        return _genetic_algorithm.map1_find(self, x)

    def lower_bound(self, x):
        return _genetic_algorithm.map1_lower_bound(self, x)

    def upper_bound(self, x):
        return _genetic_algorithm.map1_upper_bound(self, x)
    __swig_destroy__ = _genetic_algorithm.delete_map1

# Register map1 in _genetic_algorithm:
_genetic_algorithm.map1_swigregister(map1)

class config_t(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _genetic_algorithm.config_t_swiginit(self, _genetic_algorithm.new_config_t(*args))
    first = property(_genetic_algorithm.config_t_first_get, _genetic_algorithm.config_t_first_set)
    second = property(_genetic_algorithm.config_t_second_get, _genetic_algorithm.config_t_second_set)
    def __len__(self):
        return 2
    def __repr__(self):
        return str((self.first, self.second))
    def __getitem__(self, index): 
        if not (index % 2):
            return self.first
        else:
            return self.second
    def __setitem__(self, index, val):
        if not (index % 2):
            self.first = val
        else:
            self.second = val
    __swig_destroy__ = _genetic_algorithm.delete_config_t

# Register config_t in _genetic_algorithm:
_genetic_algorithm.config_t_swigregister(config_t)

class region_t(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _genetic_algorithm.region_t_swiginit(self, _genetic_algorithm.new_region_t(*args))
    first = property(_genetic_algorithm.region_t_first_get, _genetic_algorithm.region_t_first_set)
    second = property(_genetic_algorithm.region_t_second_get, _genetic_algorithm.region_t_second_set)
    def __len__(self):
        return 2
    def __repr__(self):
        return str((self.first, self.second))
    def __getitem__(self, index): 
        if not (index % 2):
            return self.first
        else:
            return self.second
    def __setitem__(self, index, val):
        if not (index % 2):
            self.first = val
        else:
            self.second = val
    __swig_destroy__ = _genetic_algorithm.delete_region_t

# Register region_t in _genetic_algorithm:
_genetic_algorithm.region_t_swigregister(region_t)

class Optimizer(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _genetic_algorithm.delete_Optimizer

    def Run(self, energies):
        return _genetic_algorithm.Optimizer_Run(self, energies)

    def SetAlpha(self, value):
        return _genetic_algorithm.Optimizer_SetAlpha(self, value)

    def SetBeta(self, value):
        return _genetic_algorithm.Optimizer_SetBeta(self, value)

    def SetGamma(self, value):
        return _genetic_algorithm.Optimizer_SetGamma(self, value)

    def GetLearningTrace(self):
        return _genetic_algorithm.Optimizer_GetLearningTrace(self)

    def GetTerm1Trace(self):
        return _genetic_algorithm.Optimizer_GetTerm1Trace(self)

    def GetTerm2Trace(self):
        return _genetic_algorithm.Optimizer_GetTerm2Trace(self)

    def GetBestCoverage(self):
        return _genetic_algorithm.Optimizer_GetBestCoverage(self)

    def GetBestOverlapping(self):
        return _genetic_algorithm.Optimizer_GetBestOverlapping(self)

# Register Optimizer in _genetic_algorithm:
_genetic_algorithm.Optimizer_swigregister(Optimizer)

class GeneticAlgorithm(Optimizer):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, exclusive, overlapping, ids, config):
        _genetic_algorithm.GeneticAlgorithm_swiginit(self, _genetic_algorithm.new_GeneticAlgorithm(exclusive, overlapping, ids, config))
    __swig_destroy__ = _genetic_algorithm.delete_GeneticAlgorithm

# Register GeneticAlgorithm in _genetic_algorithm:
_genetic_algorithm.GeneticAlgorithm_swigregister(GeneticAlgorithm)



