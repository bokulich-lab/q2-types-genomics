# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import os.path
import unittest

from q2_types_genomics.eggnog._format import (
    EggnogBase, EggnogFmt, HeaderlessEggnogFmt, EggnogDirFmt,
)

from qiime2.plugin.testing import TestPluginBase



class TestBase(TestPluginBase):
    package = 'q2_types_genomics.eggnog.tests'

    def setup(self):
        pass

    def test_tsv(self):
        pass

    def test_encoding(self):
        pass

if __name__ == '__main__':
    unittest.main()
