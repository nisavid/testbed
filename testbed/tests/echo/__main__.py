#!/usr/bin/env python

""":mod:`Echo <testbed.resources._echo>` tests."""

__copyright__ = "Copyright (C) 2013 Ivan D Vasin and Cogo Labs"
__docformat__ = "restructuredtext"

import unittest as _unittest

import spruce.logging as _logging

from ._core import *
from ._method import *
from ._resource import *


if __name__ == '__main__':
    _logging.basicConfig()
    _unittest.main()
