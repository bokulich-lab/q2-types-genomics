# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import unittest

from qiime2.plugin.testing import TestPluginBase

from q2_types_genomics.feature_data._format import (
        MAGSequencesDirFmt, OrthologAnnotationDirFmt,
        )


class TestFeatureDataFormats(TestPluginBase):
    package = 'q2_types_genomics.feature_data.tests'

    def test_mag_dirfmt_fa(self):
        dirpath = self.get_data_path('mags-fa')
        fmt_obj = MAGSequencesDirFmt(dirpath, mode='r')

        fmt_obj.validate()

    def test_mag_dirfmt_fasta(self):
        dirpath = self.get_data_path('mags-fasta')
        fmt_obj = MAGSequencesDirFmt(dirpath, mode='r')

        fmt_obj.validate()

    def test_ortholog_annotation_dir_fmt(self):
        dirpath = self.get_data_path('good_ortholog_annotation')
        fmt_obj = OrthologAnnotationDirFmt(dirpath, mode='r')
        fmt_obj.validate()

if __name__ == '__main__':
    unittest.main()
