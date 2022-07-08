# ----------------------------------------------------------------------------
# Copyright (c) 2021-2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


import unittest
from qiime2.plugin.testing import TestPluginBase
import pandas as pd

from q2_types_genomics.eggnog._format import ArbitraryHeaderTSVFmt
from q2_types_genomics.eggnog import NOG


class TestEggnogTypes(TestPluginBase):
    package = 'q2_types_genomics.eggnog.tests'

    def test_nog_registration(self):
        self.assertRegisteredSemanticType(NOG)

    def test_base_eggnog_validation_integration(self):
        run_checker = False
        header = 4
        filename = 'sampleannotations.txt'
        filepath = self.get_data_path(filename)

        exp = pd.read_csv(filepath, sep="\t", header=header)
        exp.columns = [each.strip("#") for each in exp.columns]

        obs = ArbitraryHeaderTSVFmt(filepath, mode='r').view(pd.DataFrame)
        run_checker = True

        self.assertTrue(obs.equals(exp))

        # ensure correct comment character stripping.
        pd.util.testing.assert_index_equal(exp.columns, obs.columns)
        assert run_checker

    def test_no_header_footer_data(self):
        run_checker = False
        filename = "noheadersample.txt"
        filepath = self.get_data_path(filename)

        exp = pd.read_csv(filepath, sep="\t", header=0)
        exp.columns = [each.strip("#") for each in exp.columns]

        obs = ArbitraryHeaderTSVFmt(filepath, mode='r').view(pd.DataFrame)
        run_checker = True

        self.assertTrue(obs.equals(exp))

        assert run_checker


if __name__ == '__main__':
    unittest.main()
