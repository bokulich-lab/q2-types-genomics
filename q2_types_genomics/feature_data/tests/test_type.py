# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import unittest

from q2_types.feature_data import FeatureData
from qiime2.plugin.testing import TestPluginBase

from q2_types_genomics.feature_data import MAG, MAGSequencesDirFmt


class TestTypes(TestPluginBase):
    package = 'q2_types_genomics.feature_data.tests'

    def test_mag_semantic_type_registration(self):
        self.assertRegisteredSemanticType(MAG)

    def test_mags_semantic_type_to_format_registration(self):
        self.assertSemanticTypeRegisteredToFormat(
            FeatureData[MAG],
            MAGSequencesDirFmt
        )


if __name__ == '__main__':
    unittest.main()
