# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
import unittest

from qiime2.plugin.testing import TestPluginBase


from q2_types_genomics.feature_map import (
    FeatureMap, MAGtoContigs, MAGtoContigsDirFmt
)


class TestTypes(TestPluginBase):
    package = "q2_types_genomics.feature_map.tests"

    def test_feature_map_semantic_type_registration(self):
        self.assertRegisteredSemanticType(FeatureMap)

    def test_feature_map_mag_to_contigs_semantic_type_registration(self):
        self.assertRegisteredSemanticType(FeatureMap[MAGtoContigs])

    def test_genome_data_genes_to_genes_dir_fmt_registration(self):
        self.assertSemanticTypeRegisteredToFormat(
            FeatureMap[MAGtoContigs], MAGtoContigsDirFmt
        )


if __name__ == "__main__":
    unittest.main()
