# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import unittest

from qiime2.plugin.testing import TestPluginBase

from .._format import (
    GenesDirectoryFormat, ProteinsDirectoryFormat
)


class TestFormats(TestPluginBase):
    package = 'q2_types_genomics.genome_data.tests'

    def test_genes_dirfmt_fa(self):
        dirpath = self.get_data_path('genes')
        format = GenesDirectoryFormat(dirpath, mode='r')

        format.validate()

    def test_proteins_dirfmt_fa(self):
        dirpath = self.get_data_path('proteins')
        format = ProteinsDirectoryFormat(dirpath, mode='r')

        format.validate()


if __name__ == '__main__':
    unittest.main()
