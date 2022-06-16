# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import glob
import unittest
from itertools import repeat

import pandas as pd
import skbio
from qiime2.plugin.testing import TestPluginBase
from skbio import DNA

from q2_types_genomics.feature_data import (
    MAGSequencesDirFmt, MAGIterator
)
from q2_types_genomics.feature_data._transformer import _get_filename


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
        df = df.astype(str).replace({'nan': None})
        df.index.name = 'Feature ID'
        return df

    @staticmethod
    def create_multi_generator(seqs_dict):
        for k1, v1 in seqs_dict.items():
            yield from zip(
                repeat(k1),
                (DNA(v2, metadata={'id': k2, 'description': ''})
                 for k2, v2 in v1.items())
            )

    @staticmethod
    def read_seqs_into_dict(loc):
        seqs = {}
        for f in sorted(glob.glob(f'{loc}/*')):
            seqs[_get_filename(f)] = {
                seq.metadata['id']: str(seq)
                for seq in skbio.read(f, format='fasta')
            }
        return seqs

    def test_mag_sequences_dir_fmt_to_dataframe(self):
        _, obs = self.transform_format(MAGSequencesDirFmt, pd.DataFrame,
                                       filenames=[
                                           'mags-fasta/mag1.fasta',
                                           'mags-fasta/mag2.fasta',
                                       ])
        exp = self.mags_to_df(self.mags_fasta)
        pd.testing.assert_frame_equal(exp, obs)

    def test_dataframe_to_mag_sequences_dir_fmt(self):
        transformer = self.get_transformer(pd.DataFrame, MAGSequencesDirFmt)
        df = self.mags_to_df(self.mags_fasta)

        obs = transformer(df)
        self.assertIsInstance(obs, MAGSequencesDirFmt)

        obs_seqs = self.read_seqs_into_dict(str(obs))
        self.assertDictEqual(self.mags_fasta, obs_seqs)

    def test_mag_sequences_dir_fmt_to_mag_iterator(self):
        _, obs = self.transform_format(MAGSequencesDirFmt, MAGIterator,
                                       filenames=[
                                           'mags-fasta/mag1.fasta',
                                           'mags-fasta/mag2.fasta',
                                       ])

        exp = self.create_multi_generator(self.mags_fasta)
        for e, o in zip(exp, obs):
            self.assertEqual(e, o)

    def test_mag_iterator_to_mag_sequences_dir_fmt(self):
        transformer = self.get_transformer(MAGIterator, MAGSequencesDirFmt)
        seq_iter = self.create_multi_generator(self.mags_fa)

        obs = transformer(seq_iter)
        self.assertIsInstance(obs, MAGSequencesDirFmt)

        obs_seqs = self.read_seqs_into_dict(str(obs))
        self.assertDictEqual(self.mags_fa, obs_seqs)


if __name__ == '__main__':
    unittest.main()
