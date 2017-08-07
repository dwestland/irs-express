# -*- coding: utf-8 -*-


class BaseIRSException(Exception):
    """ Base class for all IRS custom exceptions """

    """ We can pass custom set of parameters and they will be remembered in the 'customdata' attribute """
    def __init__(self, msg=None, **kwargs):
        super(BaseIRSException, self).__init__(msg)
        self.customdata = {}
        if kwargs:
            for a in kwargs:
                self.customdata[a] = kwargs[a]

    @property
    def c(self):
        return self.customdata

# ------------------------------------------------------ #


class DocParseError(BaseIRSException):
    pass
