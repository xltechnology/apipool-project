#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.0.2"
__short_description__ = "Multiple API Key Manager"
__license__ = "MIT"
__author__ = "Sanhe Hu"
__author_email__ = "husanhe@gmail.com"
__maintainer__ = "Sanhe Hu"
__maintainer_email__ = "husanhe@gmail.com"
__github_username__ = "MacHu-GWU"

try:
    from .apikey import ApiKey
    from .manager import ApiKeyManager
    from .stats import StatusCollection
except Exception as e:  # pragma: no cover
    pass
