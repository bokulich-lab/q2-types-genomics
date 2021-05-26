# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import unittest

import pandas as pd
from qiime2.plugin.testing import TestPluginBase

from q2_types_genomics.feature_data import (
    MAGFASTAFormat
)


class TestTransformers(TestPluginBase):
    package = 'q2_types_genomics.feature_data.tests'

    def setUp(self):
        super().setUp()
        self.mags_fa = {
            'mag1': {
                'k129_5480': 'TTATTTTCAAGATAATGAGCCAATTTAAGCGGTGTCTGGCCG'
                             'CCAAGCTGCACGATCACACCTTTAA'
            },
            'mag2': {
                'k129_5112': 'CCCCGGAAAGGGCTGGCGACCGACGATGACCTCGGGAAGCCC'
                             'CAACTCGCGGCCGATGGCGCGTACCTCGTC'
            },
            'mag3': {
                'k129_6525': 'AAACTCTATCAAGCGTATACCAAAGTGAGTGGTGTATTGATC'
                             'AGTCAGCTCATTATTGAATCGGA',
                'k129_6531': 'TCGGATTTGCCGAATGCTTTTTGTAAGGGCCTTCAATTGATT'
                             'TGGCGATAGCGAGCCCGTATTTACGGT'
            }
        }
        self.mags_fasta = {
            'mag1': {
                'k129_4684': 'TGATACCGACGCGGCACTTGAGTGCGCGCTATCCTTCAAGGA'
                             'AGCCACATGCGTTATTGTTAAACA',
                'k129_5618': 'GTGCTAATCGCACCCTCATGAGCGACACCATTATTCTTTATT'
                             'TTTGAGTCTTCAGCAAAA',
                'k129_5631': 'TCATGATGATCCAAAAGCAGTTGCGGAAGCATCTGGGATAAT'
                             'TACGCGGAGTGGATGTCGCCG',
                'k129_2817': 'GTCGCCAATTAGCAACTATGATGTCTTCTGGAGTACCTTTGG'
                             'TCCAATCATTTGAAATCA'
            },
            'mag2': {
                'k129_5401': 'CCATTGTATGTCTTTAGGTAGCTCCTCATGTTTGAGGTTCAT'
                             'GTCTTGGATTTTGTTTTCTCCAAAAATC'
            }
        }

    @staticmethod
    def mags_to_df(mags):
        df = pd.DataFrame.from_dict(mags, orient='index')
        df = df.astype(str)
        df.index.name = 'Feature ID'
        return df

    def test_mag_fa_to_dataframe(self):
        _, obs = self.transform_format(MAGFASTAFormat, pd.DataFrame,
                                       filenames=[
                                           "mags-fa/mag1.fa",
                                           "mags-fa/mag2.fa",
                                           "mags-fa/mag3.fa"
                                       ])
        exp = pd.DataFrame.from_dict(self.mags_fa, orient='index')
        exp = exp.astype(str)
        exp.index.name = 'Feature ID'
        pd.testing.assert_frame_equal(exp, obs)

    def test_mag_fasta_to_dataframe(self):
        _, obs = self.transform_format(MAGFASTAFormat, pd.DataFrame,
                                       filenames=[
                                           "mags-fasta/mag1.fasta",
                                           "mags-fasta/mag2.fasta",
                                       ])
        exp = pd.DataFrame.from_dict(self.mags_fasta, orient='index')
        exp = exp.astype(str)
        exp.index.name = 'Feature ID'
        pd.testing.assert_frame_equal(exp, obs)


if __name__ == '__main__':
    unittest.main()
