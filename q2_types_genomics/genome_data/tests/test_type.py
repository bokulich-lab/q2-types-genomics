# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import unittest

from q2_types_genomics.genome_data import (
    GenomeData, Genes, Proteins, GenesDirectoryFormat, ProteinsDirectoryFormat
)
from qiime2.plugin.testing import TestPluginBase


class TestTypes(TestPluginBase):
    package = "q2_types_genomics.genome_data.tests"

    def test_genome_data_semantic_type_registration(self):
        self.assertRegisteredSemanticType(GenomeData)

    def test_genes_semantic_type_registration(self):
        self.assertRegisteredSemanticType(Genes)

    def test_proteins_semantic_type_registration(self):
        self.assertRegisteredSemanticType(Proteins)

    def test_genome_data_genes_to_genes_dir_fmt_registration(self):
        self.assertSemanticTypeRegisteredToFormat(
            GenomeData[Genes], GenesDirectoryFormat)

    def test_genome_data_proteins_to_proteins_dir_fmt_registration(self):
        self.assertSemanticTypeRegisteredToFormat(
            GenomeData[Proteins], ProteinsDirectoryFormat)


if __name__ == '__main__':
    unittest.main()
