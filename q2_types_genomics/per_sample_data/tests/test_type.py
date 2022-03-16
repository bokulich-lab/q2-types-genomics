# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import unittest

from q2_types.bowtie2 import Bowtie2IndexDirFmt
from q2_types.sample_data import SampleData
from qiime2.plugin.testing import TestPluginBase

from q2_types_genomics.per_sample_data import (
    MAGs, MultiMAGSequencesDirFmt,
    Contigs, ContigSequencesDirFmt,
    SingleBowtie2Index, MultiBowtie2Index, MultiBowtie2IndexDirFmt, BAMDirFmt,
    MultiBAMDirFmt
)
from q2_types_genomics.per_sample_data._type import (AlignmentMap,
                                                     MultiAlignmentMap)


class TestTypes(TestPluginBase):
    package = "q2_types_genomics.per_sample_data.tests"

    def test_mags_semantic_type_registration(self):
        self.assertRegisteredSemanticType(MAGs)

    def test_mags_semantic_type_to_format_registration(self):
        self.assertSemanticTypeRegisteredToFormat(
            SampleData[MAGs],
            MultiMAGSequencesDirFmt
        )

    def test_contigs_semantic_type_registration(self):
        self.assertRegisteredSemanticType(Contigs)

    def test_contigs_semantic_type_to_format_registration(self):
        self.assertSemanticTypeRegisteredToFormat(
            SampleData[Contigs],
            ContigSequencesDirFmt
        )

    def test_singlebowtie_semantic_type_registration(self):
        self.assertRegisteredSemanticType(SingleBowtie2Index)

    def test_singlebowtie_semantic_type_to_format_registration(self):
        self.assertSemanticTypeRegisteredToFormat(
            SampleData[SingleBowtie2Index],
            Bowtie2IndexDirFmt
        )

    def test_multibowtie_index_semantic_type_registration(self):
        self.assertRegisteredSemanticType(MultiBowtie2Index)

    def test_multibowtie_index_semantic_type_to_format_registration(self):
        self.assertSemanticTypeRegisteredToFormat(
            SampleData[MultiBowtie2Index],
            MultiBowtie2IndexDirFmt
        )

    def test_aln_map_semantic_type_registration(self):
        self.assertRegisteredSemanticType(AlignmentMap)

    def test_aln_map_semantic_type_to_format_registration(self):
        self.assertSemanticTypeRegisteredToFormat(
            SampleData[AlignmentMap],
            BAMDirFmt
        )

    def test_multi_aln_map_semantic_type_registration(self):
        self.assertRegisteredSemanticType(MultiAlignmentMap)

    def test_multi_aln_map_semantic_type_to_format_registration(self):
        self.assertSemanticTypeRegisteredToFormat(
            SampleData[MultiAlignmentMap],
            MultiBAMDirFmt
        )


if __name__ == '__main__':
    unittest.main()
