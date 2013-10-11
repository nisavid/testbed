"""Performance resources."""

__copyright__ = "Copyright (C) 2013 Ivan D Vasin and Cogo Labs"
__docformat__ = "restructuredtext"

from time import sleep as _sleep

import bedframe as _bedframe
import bedframe.webtypes as _webtypes


class Sleep(_bedframe.WebResource):
    @_bedframe.webmethod(duration=_webtypes.float)
    def get(self, duration):
        _sleep(duration)
