# encoding: utf-8

"""
Objects shared by docx modules.
"""

from __future__ import absolute_import, print_function, unicode_literals


class Length(int):
    """
    Base class for length constructor classes Inches, Cm, Mm, Px, and Emu.
    Behaves as an int count of English Metric Units, 914,400 to the inch,
    36,000 to the mm. Provides convenience unit conversion methods in the form
    of read-only properties. Immutable.
    """
    _EMUS_PER_INCH = 914400
    _EMUS_PER_CM = 360000
    _EMUS_PER_MM = 36000
    _EMUS_PER_PT = 12700
    _EMUS_PER_TWIP = 635

    def __new__(cls, emu):
        return int.__new__(cls, emu)

    @property
    def cm(self):
        """
        The equivalent length expressed in centimeters (float).
        """
        return self / float(self._EMUS_PER_CM)

    @property
    def emu(self):
        """
        The equivalent length expressed in English Metric Units (int).
        """
        return self

    @property
    def inches(self):
        """
        The equivalent length expressed in inches (float).
        """
        return self / float(self._EMUS_PER_INCH)

    @property
    def mm(self):
        """
        The equivalent length expressed in millimeters (float).
        """
        return self / float(self._EMUS_PER_MM)

    @property
    def pt(self):
        """
        Floating point length in points
        """
        return self / float(self._EMUS_PER_PT)

    @property
    def twips(self):
        """
        The equivalent length expressed in twips (int).
        """
        return int(round(self / float(self._EMUS_PER_TWIP)))


class Inches(Length):
    """
    Convenience constructor for length in inches, e.g.
    ``width = Inches(0.5)``.
    """
    def __new__(cls, inches):
        emu = int(inches * Length._EMUS_PER_INCH)
        return Length.__new__(cls, emu)


class Cm(Length):
    """
    Convenience constructor for length in centimeters, e.g.
    ``height = Cm(12)``.
    """
    def __new__(cls, cm):
        emu = int(cm * Length._EMUS_PER_CM)
        return Length.__new__(cls, emu)


class Emu(Length):
    """
    Convenience constructor for length in English Metric Units, e.g.
    ``width = Emu(457200)``.
    """
    def __new__(cls, emu):
        return Length.__new__(cls, int(emu))


class Mm(Length):
    """
    Convenience constructor for length in millimeters, e.g.
    ``width = Mm(240.5)``.
    """
    def __new__(cls, mm):
        emu = int(mm * Length._EMUS_PER_MM)
        return Length.__new__(cls, emu)


class Pt(Length):
    """
    Convenience value class for specifying a length in points
    """
    def __new__(cls, points):
        emu = int(points * Length._EMUS_PER_PT)
        return Length.__new__(cls, emu)


class Twips(Length):
    """
    Convenience constructor for length in twips, e.g. ``width = Twips(42)``.
    A twip is a twentieth of a point, 635 EMU.
    """
    def __new__(cls, twips):
        emu = int(twips * Length._EMUS_PER_TWIP)
        return Length.__new__(cls, emu)


class RGBColor(tuple):
    """
    Immutable value object defining a particular RGB color.
    """
    def __new__(cls, r, g, b):
        msg = 'RGBColor() takes three integer values 0-255'
        for val in (r, g, b):
            if not isinstance(val, int) or val < 0 or val > 255:
                raise ValueError(msg)
        return super(RGBColor, cls).__new__(cls, (r, g, b))

    def __repr__(self):
        return 'RGBColor(0x%02x, 0x%02x, 0x%02x)' % self

    def __str__(self):
        """
        Return a hex string rgb value, like '3C2F80'
        """
        return '%02X%02X%02X' % self

    @classmethod
    def from_string(cls, rgb_hex_str):
        """
        Return a new instance from an RGB color hex string like ``'3C2F80'``.
        """
        # Assume RGB value
        try:
            r = int(rgb_hex_str[:2], 16)
            g = int(rgb_hex_str[2:4], 16)
            b = int(rgb_hex_str[4:], 16)
        # But if we don't get an RGB value, see if we get a named color
        except ValueError:
            # We will support named Highlight Colors.  I'm not aware of other
            # color name definitions for DOCx
            if rgb_hex_str.lower() == 'black':
                r = 0x00
                g = 0x00
                b = 0x00
            elif rgb_hex_str.lower() == 'blue':
                r = 0x00
                g = 0x00
                b = 0xFF
            elif rgb_hex_str.lower() == 'cyan':
                r = 0x00
                g = 0xFF
                b = 0xFF
            elif rgb_hex_str.lower() == 'darkblue':
                r = 0x00
                g = 0x00
                b = 0x80
            elif rgb_hex_str.lower() == 'darkcyan':
                r = 0x00
                g = 0x80
                b = 0x80
            elif rgb_hex_str.lower() == 'darkgreen':
                r = 0x00
                g = 0x80
                b = 0x00
            elif rgb_hex_str.lower() == 'darkgray':
                r = 0x80
                g = 0x80
                b = 0x80
            elif rgb_hex_str.lower() == 'darkmagenta':
                r = 0x80
                g = 0x00
                b = 0x80
            elif rgb_hex_str.lower() == 'darkred':
                r = 0x80
                g = 0x00
                b = 0x00
            elif rgb_hex_str.lower() == 'darkyellow':
                r = 0x80
                g = 0x80
                b = 0x00
            elif rgb_hex_str.lower() == 'green':
                r = 0x00
                g = 0xFF
                b = 0x00
            elif rgb_hex_str.lower() == 'lightgray':
                r = 0xC0
                g = 0xC0
                b = 0xC0
            elif rgb_hex_str.lower() == 'magenta':
                r = 0xFF
                g = 0x00
                b = 0xFF
            elif rgb_hex_str.lower() == 'red':
                r = 0xFF
                g = 0x00
                b = 0x00
            elif rgb_hex_str.lower() == 'white':
                r = 0xFF
                g = 0xFF
                b = 0xFF
            elif rgb_hex_str.lower() == 'yellow':
                r = 0xFF
                g = 0xFF
                b = 0x00
            # For all other names, return BLACK
            else:
                r = 0x00
                g = 0x00
                b = 0x00
        return cls(r, g, b)


def lazyproperty(f):
    """
    @lazyprop decorator. Decorated method will be called only on first access
    to calculate a cached property value. After that, the cached value is
    returned.
    """
    cache_attr_name = '_%s' % f.__name__  # like '_foobar' for prop 'foobar'
    docstring = f.__doc__

    def get_prop_value(obj):
        try:
            return getattr(obj, cache_attr_name)
        except AttributeError:
            value = f(obj)
            setattr(obj, cache_attr_name, value)
            return value

    return property(get_prop_value, doc=docstring)


def write_only_property(f):
    """
    @write_only_property decorator. Creates a property (descriptor attribute)
    that accepts assignment, but not getattr (use in an expression).
    """
    docstring = f.__doc__

    return property(fset=f, doc=docstring)


class ElementProxy(object):
    """
    Base class for lxml element proxy classes. An element proxy class is one
    whose primary responsibilities are fulfilled by manipulating the
    attributes and child elements of an XML element. They are the most common
    type of class in python-docx other than custom element (oxml) classes.
    """

    __slots__ = ('_element', '_parent')

    def __init__(self, element, parent=None):
        self._element = element
        self._parent = parent

    def __eq__(self, other):
        """
        Return |True| if this proxy object refers to the same oxml element as
        does *other*. ElementProxy objects are value objects and should
        maintain no mutable local state. Equality for proxy objects is
        defined as referring to the same XML element, whether or not they are
        the same proxy object instance.
        """
        if not isinstance(other, ElementProxy):
            return False
        return self._element is other._element

    def __ne__(self, other):
        if not isinstance(other, ElementProxy):
            return True
        return self._element is not other._element

    @property
    def element(self):
        """
        The lxml element proxied by this object.
        """
        return self._element

    @property
    def part(self):
        """
        The package part containing this object
        """
        return self._parent.part


class Parented(object):
    """
    Provides common services for document elements that occur below a part
    but may occasionally require an ancestor object to provide a service,
    such as add or drop a relationship. Provides ``self._parent`` attribute
    to subclasses.
    """
    def __init__(self, parent):
        super(Parented, self).__init__()
        self._parent = parent

    @property
    def part(self):
        """
        The package part containing this object
        """
        return self._parent.part
