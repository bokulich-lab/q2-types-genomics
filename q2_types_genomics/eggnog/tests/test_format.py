# ----------------------------------------------------------------------------
# Copyright (c) 2021-2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import unittest

from q2_types_genomics.eggnog import ArbitraryHeaderTSVFmt

from qiime2.plugin.testing import TestPluginBase


class TestArbitraryHeaderTSVFmt(TestPluginBase):
    """This format is for files written as TSVs with arbitrary header and/or
    footer lengths and locations, verification of content should be performed
    using Semantic Validators"""
    package = 'q2_types_genomics.eggnog.tests'

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
        filename = 'sampleannotations.txt'
        filepath = self.get_data_path(filename)

        fmt = ArbitraryHeaderTSVFmt(filepath, mode='r')

        fmt.validate()
        has_run = True
        assert has_run

    def test_no_header(self):
        has_run = False
        filename = 'noheadersample.txt'
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
