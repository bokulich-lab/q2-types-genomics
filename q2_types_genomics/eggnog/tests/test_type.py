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

from q2_types_genomics.eggnog import NOG

class TestTypes(TestPluginBase):
    package = 'q2_types_genomics.eggnog.tests'

    def test_nog_registration(self):
        self.assertRegisteredSemanticType(NOG)

if __name__ == '__main__':
    unittest.main()
