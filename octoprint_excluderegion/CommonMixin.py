# coding=utf-8
"""Module providing the CommonMixin class."""

from __future__ import absolute_import

import json


class CommonMixin(object):
    """Provides some common behavior methods and overloads."""

    def toDict(self):
        """
        Return a dictionary representation of this object.

        Returns
        -------
        dict
            All of the standard instance properties are included in the dictionary, with an
            additional "type" property containing the class name.
        """
        result = self.__dict__.copy()
        result['type'] = self.__class__.__name__
        return result

    def __repr__(self):
        """
        Return a string representation of this object.

        Returns
        -------
        string
            JSON representation of the dictionary returned by toDict()
        """
        return json.dumps(self.toDict())

    def __eq__(self, value):
        """
        Determine whether this object is equal to another value.

        Parameters
        ----------
        value : any
            The value to test for equality

        Returns
        -------
        boolean
            True if the value is the same type and has the same property values as this instance,
            and False otherwise.
        """
        return isinstance(value, type(self)) and (self.__dict__ == value.__dict__)

    def __ne__(self, value):
        """
        Determine whether this object is not equal to another value.

        Parameters
        ----------
        value : any
            The value to test for inequality

        Returns
        -------
        boolean
            True if the value is not the same type or same property value differs when compared to
            this instance, and False otherwise.
        """
        return not self.__eq__(value)
