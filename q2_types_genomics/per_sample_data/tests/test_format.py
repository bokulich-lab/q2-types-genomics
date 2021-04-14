# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import os
import shutil
import string
import unittest

from qiime2.core.exceptions import ValidationError
from qiime2.plugin.testing import TestPluginBase

from q2_types_genomics.per_sample_data._format import (
    MultiFASTADirectoryFormat, MultiMAGManifestFormat, ContigSequencesDirFmt
)


class TestMultiMAGManifestFormat(TestPluginBase):
    package = 'q2_types_genomics.per_sample_data.tests'

    def template_manifest(self, filepath, ctx):
        with open(filepath) as fh:
            tmpl = string.Template(fh.read())
        basename = os.path.basename(filepath)
        file_ = os.path.join(self.temp_dir.name, basename)
        with open(file_, 'w') as fh:
            fh.write(tmpl.substitute(**ctx))
        return file_

    def test_multifasta_manifest(self):
        manifest_fp = self.get_data_path('manifests/MANIFEST-mags-fa')
        format = MultiMAGManifestFormat(manifest_fp, mode='r')

        format.validate()

    def test_multifasta_manifest_missing_column(self):
        manifest_fp = self.get_data_path('manifests/MANIFEST-missing-column')
        format = MultiMAGManifestFormat(manifest_fp, mode='r')

        with self.assertRaisesRegex(
                ValidationError, 'Found header .* with the following labels'):
            format.validate()

    def test_multifasta_manifest_missing_file(self):
        manifest_fp = self.get_data_path('manifests/MANIFEST-missing-filepath')
        format = MultiMAGManifestFormat(manifest_fp, mode='r')

        with self.assertRaisesRegex(
                ValidationError, 'Line 2 has 2 cells .* expected 3'):
            format.validate()

    def test_multifasta_manifest_no_samples(self):
        manifest_fp = self.get_data_path('manifests/MANIFEST-no-samples')
        format = MultiMAGManifestFormat(manifest_fp, mode='r')

        with self.assertRaisesRegex(
                ValidationError, 'No sample records found'):
            format.validate()

    def test_multifasta_manifest_empty(self):
        manifest_fp = self.get_data_path('manifests/MANIFEST-empty')
        format = MultiMAGManifestFormat(manifest_fp, mode='r')

        with self.assertRaisesRegex(
                ValidationError, 'No header found, expected'):
            format.validate()


class TestFormats(TestPluginBase):
    package = 'q2_types_genomics.per_sample_data.tests'

    def test_multifasta_dirfmt_fa(self):
        dirpath = self.get_data_path('mags/mags-fa')
        format = MultiFASTADirectoryFormat(dirpath, mode='r')

        format.validate()

    def test_multifasta_dirfmt_fasta(self):
        dirpath = self.get_data_path('mags/mags-fasta')
        format = MultiFASTADirectoryFormat(dirpath, mode='r')

        format.validate()

    def test_multifasta_dirfmt_unorganized(self):
        dirpath = self.get_data_path('mags/mags-unorganized')
        format = MultiFASTADirectoryFormat(dirpath, mode='r')

        with self.assertRaisesRegex(
                ValidationError, 'should be .* per-sample directories'):
            format.validate()

    def test_contig_seqs_dirfmt(self):
        filepath = self.get_data_path('mags/mags-fasta/sample2/mag1.fasta')
        shutil.copy(filepath, os.path.join(
            self.temp_dir.name, 'contigs.fasta'))
        ContigSequencesDirFmt(self.temp_dir.name, mode='r').validate()


if __name__ == '__main__':
    unittest.main()
