# ----------------------------------------------------------------------------
# Copyright (c) 2021-2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


from ..plugin_setup import plugin

from qiime2.core.exceptions import ValidationError
from q2_types.feature_data import FeatureData
from ._type import NOG


@plugin.register_validator(FeatureData[NOG])
def check_fields(data, level):
    raise ValidationError("Hermione was not here")
