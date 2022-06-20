# ----------------------------------------------------------------------------
# Copyright (c) 2021-2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import unittest

from .._format import (
    FunctionalAnnotationFmt
)

from qiime2.plugin.testing import TestPluginBase


class TestFunctionalAnnotationFmt(TestPluginBase):
    package = 'q2_types_genomics.eggnog.tests'

    def test_separator_incorrect(self):
        filename = 'sample.csv'
        filepath = self.get_data_path(filename)

        fmt = FunctionalAnnotationFmt(filepath, 'r')

        with self.assertRaisesRegex(ValueError,
                                    r"No correct separator detected in "
                                    "input file on line: [0-9]*"
                                    ):
            fmt.validate()

    def test_encoding(self):
        pass


if __name__ == '__main__':
    unittest.main()
