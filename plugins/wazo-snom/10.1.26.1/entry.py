# Copyright 2018-2022 The Wazo Authors  (see AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

common_globals = {}
execfile_('common.py', common_globals)

MODELS = [
    'D735',
]
VERSION = '10.1.26.1'


class SnomPlugin(common_globals['BaseSnomPlugin']):
    IS_PLUGIN = True

    _MODELS = MODELS

    pg_associator = common_globals['BaseSnomPgAssociator'](MODELS, VERSION)
