# ----------------------------------------------------------------------------
# Copyright (c) 2021-2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import unittest

from qiime2 import Artifact as Artifact
from qiime2.plugin.testing import TestPluginBase
from pandas import DataFrame as DataFrame

from q2_types_genomics.eggnog import NOG


class TestEggnogTypes(TestPluginBase):
    package = 'q2_types_genomics.eggnog.tests'

    def test_nog_registration(self):
        self.assertRegisteredSemanticType(NOG)

    def test_base_eggnog_validation(self):
        run_checker = False
        filename = 'sample.csv'
        filepath = self.get_data_path(filename)

        test_file = Artifact.import_data('FeatureData[NOG]', filepath)

        test_file.view(DataFrame)
        run_checker = True
        assert run_checker






if __name__ == '__main__':
    unittest.main()
