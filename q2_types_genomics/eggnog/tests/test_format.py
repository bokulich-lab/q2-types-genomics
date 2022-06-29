# ----------------------------------------------------------------------------
# Copyright (c) 2021-2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import unittest

from .._format import (
    EggnogAnnotationFmt
)

from qiime2.plugin.testing import TestPluginBase


class TestEggnogAnnotationFmt(TestPluginBase):
    package = 'q2_types_genomics.eggnog.tests'

    def test_separator_incorrect(self):
        has_run = False
        filename = 'sample.csv'
        filepath = self.get_data_path(filename)

        fmt = EggnogAnnotationFmt(filepath, mode='r')

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

        fmt = EggnogAnnotationFmt(filepath, mode='r')

        #with self.assertNotRegex(ValueError,
        #                         r"No correct separator detected in "
        #                         "input file on line: [0-9]*"
        #                         ):
        fmt.validate()
        has_run = True
        assert has_run


    def test_encoding(self):
        pass


if __name__ == '__main__':
    unittest.main()
