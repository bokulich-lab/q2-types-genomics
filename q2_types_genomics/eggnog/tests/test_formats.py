# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


from q2_types_genomics.eggnog import (
        EggnogRefDirFmt, EggnogRefBinFileFmt, EggnogRe, 

        )
from qiime2.plugin.testing import TestPluginBase

import shutil

class TestRefFmts(TestPluginBase):
    """Some of the reference databases for Eggnog Mapper are binary files. The
    formats for storing these are very general right now"""
    package = 'q2_types_genomics.eggnog.tests'

    good_file_names = [
        "eggnog.db", "eggnog.taxa.db", "eggnog.taxa.db.traverse.pkl",
        "eggnog_proteins.dmnd", "novel_fams.dmnd",
        ]

    bad_file_names = [
        "eggnog.db", "eggnog.taxa.db", "eggnog.taxa.db.traverse.pkl",
        "eggnog_proteins.dmnd", "novel_fams.dmnd", "diamond_test.dmnd"
        ]
    def test_registration_basics(self):
        filename = 'diamond_test.dmnd'
        filepath = self.get_data_path(filename)

        fmt = BinaryReferenceDBFmt(filepath, 'r')
        fmt.validate(level='max')

#    def test_fails_on_string(self):
#        filename = 'sample_annotations.txt'
#        filepath = self.get_data_path(filename)
#
#        fmt = BinaryReferenceDBFMT(filepath, 'rb')
#        fmt.validate(level='max')

def _artifact_generator(*data):
    filenames = [each for each in data]

    for filename in filenames:
        fp = self.get_data_path(filename)
