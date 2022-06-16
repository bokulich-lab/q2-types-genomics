# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import unittest

from qiime2.plugin.testing import TestPluginBase

from q2_types_genomics.feature_data._format import MAGSequencesDirFmt


class TestFormats(TestPluginBase):
    package = 'q2_types_genomics.feature_data.tests'

    def test_mag_dirfmt_fa(self):
        dirpath = self.get_data_path('mags-fa')
        format = MAGSequencesDirFmt(dirpath, mode='r')

        format.validate()

    def test_mag_dirfmt_fasta(self):
        dirpath = self.get_data_path('mags-fasta')
        format = MAGSequencesDirFmt(dirpath, mode='r')

        format.validate()


if __name__ == '__main__':
    unittest.main()
