# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


from q2_types_genomics.eggnog import (
        EggnogRefDirFmt, EggnogRefBinFileFmt, EggnogRefTextFileFmt,
        EggnogOutputDirFmt,
        )

from qiime2.plugin.testing import TestPluginBase

import os
import shutil

# Small, example databases were downloaded from http://eggnog5.embl.de/#/app/downloads


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
        "eggnog_proteins.dmnd", "novel_fams.dmnd", "diamond_testing.dmnd"
        ]

    # this will fail right now because Directory formats expect all files in
    # the format definition to be present. Going to work on making optional.
    def test_registration_basics(self):
        filename = 'diamond_testing.dmnd'
        filepath = self.get_data_path(filename)

        fmt = EggnogRefDirFmt(mode='w')
        shutil.copy(src=filepath, dst=fmt.path)
        fmt.validate()

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
        print(fp)


class TestEggnogOutput(TestPluginBase):
    package='q2_types_genomics.eggnog.tests'

    def test_initial_setup(self):
        # Create directory
        test_output = EggnogOutputDirFmt()

        # trying putting a file in...
        shutil.copy(self.get_data_path("sample_eggnog_annotations.annotations"),
                    test_output.path)

        shutil.copy(self.get_data_path("sample_annotations.txt"),
                    test_output.path)
        test_output.save(self.get_data_path("test_output.qza"))
        artifacted = _return_artifact(test_output)

        fh = Artifact.load(artifacted)
        self.assertIn("sample_annotations.txt", fh)


def _return_artifact(fmtd_object):
    return fmtd_object
