"""General resources."""

__copyright__ = "Copyright (C) 2013 Ivan D Vasin and Cogo Labs"
__docformat__ = "restructuredtext"

import bedframe as _bedframe


class NoOp(_bedframe.WebResource):

    @_bedframe.webmethod()
    def get(self):
        pass

    @_bedframe.webmethod()
    def post(self):
        pass
