# -*- coding: utf-8 -*-
"""
    flaskbb.auth.services
    ~~~~~~~~~~~~~~~~~~~~~
    Public module of implemenations of auth related services
    in FlaskBB. If you are developing a plugin or extending
    FlaskBB, you should import from this module rather than
    submodules.

    :copyright: (c) 2014-2018 the FlaskBB Team.
    :license: BSD, see LICENSE for more details
"""

from .activation import AccountActivator
from .factories import (account_activator_factory,
                        registration_service_factory, reset_service_factory)
from .password import ResetPasswordService
from .registration import (EmailUniquenessValidator, UsernameRequirements,
                           UsernameUniquenessValidator, UsernameValidator)