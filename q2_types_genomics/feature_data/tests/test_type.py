# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import unittest

from q2_types.feature_data import FeatureData
from q2_types_genomics.feature_data import (
    ArbitraryHeaderTSVFmt, NOG, MAG, MAGSequencesDirFmt,
)
from qiime2.plugin.testing import TestPluginBase

import pandas as pd


class TestTypes(TestPluginBase):
    package = 'q2_types_genomics.feature_data.tests'

    def test_mag_semantic_type_registration(self):
        self.assertRegisteredSemanticType(MAG)

    def test_mags_semantic_type_to_format_registration(self):
        self.assertSemanticTypeRegisteredToFormat(
            FeatureData[MAG],
            MAGSequencesDirFmt
        )


class TestEggnogTypes(TestPluginBase):
    package = 'q2_types_genomics.feature_data.tests'

    def test_nog_registration(self):
        self.assertRegisteredSemanticType(NOG)

    def test_base_eggnog_validation_integration(self):
        run_checker = False
        header = 4
        filename = 'sample_annotations.txt'
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
        filename = "no_header_sample.txt"
        filepath = self.get_data_path(filename)

        exp = pd.read_csv(filepath, sep="\t", header=0)
        exp.columns = [each.strip("#") for each in exp.columns]

        obs = ArbitraryHeaderTSVFmt(filepath, mode='r').view(pd.DataFrame)
        run_checker = True

        self.assertTrue(obs.equals(exp))

        assert run_checker


if __name__ == '__main__':
    unittest.main()



