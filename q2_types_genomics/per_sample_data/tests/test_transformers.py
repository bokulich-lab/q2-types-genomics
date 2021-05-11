# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
import unittest

from qiime2.plugin.testing import TestPluginBase

from q2_types_genomics.per_sample_data._format import (
    MultiFASTADirectoryFormat,
    MAGSequencesDirFmt, MultiMAGManifestFormat
)


class TestTransformers(TestPluginBase):
    package = "q2_types_genomics.per_sample_data.tests"

    def setUp(self):
        super().setUp()

    @staticmethod
    def construct_manifest(ext):
        exp_manifest = (
            "sample-id,mag-id,filename\n"
            f"sample1,mag1,sample1/mag1.{ext}\n"
            f"sample1,mag2,sample1/mag2.{ext}\n"
            f"sample1,mag3,sample1/mag3.{ext}\n"
            f"sample2,mag1,sample2/mag1.{ext}\n"
            f"sample2,mag2,sample2/mag2.{ext}\n"
        )
        return exp_manifest

    def apply_transformation(self, from_fmt, to_fmt, datafile_fp):
        transformer = self.get_transformer(from_fmt, to_fmt)
        fp = self.get_data_path(datafile_fp)
        return transformer(from_fmt(fp, 'r'))

    def test_multifile_dirfmt_to_mag_seqs_dirfmt_fa(self):
        obs = self.apply_transformation(
            MultiFASTADirectoryFormat,
            MAGSequencesDirFmt,
            'mags/mags-fa'
        )
        with obs.manifest.view(MultiMAGManifestFormat).open() as obs_manifest:
            self.assertEqual(
                obs_manifest.read(), self.construct_manifest('fasta')
            )

    def test_multifile_dirfmt_to_mag_seqs_dirfmt_fasta(self):
        obs = self.apply_transformation(
            MultiFASTADirectoryFormat,
            MAGSequencesDirFmt,
            'mags/mags-fasta'
        )
        with obs.manifest.view(MultiMAGManifestFormat).open() as obs_manifest:
            self.assertEqual(
                obs_manifest.read(), self.construct_manifest('fasta')
            )


if __name__ == '__main__':
    unittest.main()
