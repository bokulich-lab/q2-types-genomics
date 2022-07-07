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

        with ArbitraryHeaderTSVFmt(filepath, mode='r') as ff:
            obs = ff.view(pd.DataFrame)
            run_checker = True
            self.assertTrue(obs.equals(exp))

        assert run_checker

    def test_headerless_data(self):
        run_checker = False
        filename = "noheadersample.txt"
        filepath = self.get_data_path(filename)

        exp = pd.read_csv(filepath, sep="\t", header=None)

        with ArbitraryHeaderTSVFmt(filepath, mode='r') as fh:
            # invoking view so that we know the validator runs? Possibly
            # un-necessary...
            obs = ff.view(pd.DataFrame)
            run_checker = True
            self.assertEqual(obs, exp)
        assert run_checker


if __name__ == '__main__':
    unittest.main()
