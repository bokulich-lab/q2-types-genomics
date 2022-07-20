# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import unittest
import os

from qiime2.plugin.testing import TestPluginBase

from q2_types_genomics.feature_data import (
        MAGSequencesDirFmt, ArbitraryHeaderTSVFmt,
)

from qiime2.core.exceptions import ValidationError


class TestFeatureDataFormats(TestPluginBase):
    package = 'q2_types_genomics.feature_data.tests'

    def test_mag_dirfmt_fa(self):
        dirpath = self.get_data_path('mags-fa')
        format = MAGSequencesDirFmt(dirpath, mode='r')

        format.validate()

    def test_mag_dirfmt_fasta(self):
        dirpath = self.get_data_path('mags-fasta')
        format = MAGSequencesDirFmt(dirpath, mode='r')

        format.validate()


class TestArbitraryHeaderTSVFmt(TestPluginBase):
    """This format is for files written as TSVs with arbitrary header and/or
    footer lengths and locations, verification of content should be performed
    using Semantic Validators"""
    package = 'q2_types_genomics.feature_data.tests'

    def test_registration(self):
        filepath = self.get_data_path(os.path.join('./sample_annotations.txt'))
        format = ArbitraryHeaderTSVFmt(filepath, mode='r')
        format.validate()


    def test_separator_incorrect(self):
        has_run = False
        filename = 'sample.csv'
        filepath = self.get_data_path(filename)

        fmt = ArbitraryHeaderTSVFmt(filepath, mode='r')

        with self.assertRaisesRegex(ValueError,
                                    r"No correct separator detected in "
                                    "input file on line: [0-9]*"
                                    ):
            fmt.validate()
        has_run = True
        assert has_run

    def test_separator_correct(self):
        has_run = False
        filename = 'sample_annotations.txt'
        filepath = self.get_data_path(filename)

        fmt = ArbitraryHeaderTSVFmt(filepath, mode='r')

        fmt.validate()
        has_run = True
        assert has_run

    def test_no_header(self):
        has_run = False
        filename = 'no_header_sample.txt'
        filepath = self.get_data_path(filename)

        fmt = ArbitraryHeaderTSVFmt(filepath, mode='r')
        fmt.validate()
        has_run = True
        assert has_run

        print(fmt.header)
        self.assertEqual(fmt.header, 0)

    def test_encoding(self):
        pass


if __name__ == '__main__':
    unittest.main()
