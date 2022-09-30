# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


from q2_types_genomics.eggnog import (
        EggnogRefDirFmt, EggnogRefBinFileFmt, EggnogRefTextFileFmt,
        EggnogOutputDirFmt, PfamDirFmt, DiamondRefDirFmt,
        )

from qiime2.plugin.testing import TestPluginBase

import os
import shutil

# Small, example databases were downloaded from http://eggnog5.embl.de/#/app/downloads


class TestRefFmts(TestPluginBase):
    """Some of the reference databases for Eggnog Mapper are binary files. The
    formats for storing these are very general right now"""
    package = 'q2_types_genomics.eggnog.tests'

    # Diamond fmt tests are good to go.
    def test_diamond_all(self):
        test_source_fp = self.get_data_path('all_diamond/')
        fmt_obj = DiamondRefDirFmt(test_source_fp, mode='r')
        fmt_obj.validate()

    def test_diamond_only_standard(self):
        test_source_fp = self.get_data_path('standard_diamond/')
        fmt_obj = DiamondRefDirFmt(test_source_fp, mode='r')
        fmt_obj.validate()

    def test_diamond_only_novel(self):
        test_source_fp = self.get_data_path('novel_diamond/')
        fmt_obj = DiamondRefDirFmt(test_source_fp, mode='r')
        fmt_obj.validate()

    def test_eggnog_all(self):
        test_source_fp = self.get_data_path('core_eggnog/')
        fmt_obj = EggnogRefDirFmt(test_source_fp, mode='r')
        fmt_obj.validate()

    # TESTED FORMATS NOT READY
    # def test_pfam(self):
    #     test_source_fp = self.get_data_path('complete/pfam')

    #     fmt = PfamDirFmt(test_source_fp, mode='r')
    #     fmt.validate()


# TODO: GET DATA READY FOR TESTING
# class TestEggnogOutput(TestPluginBase):
#     package='q2_types_genomics.eggnog.tests'
#
#     def test_initial_setup(self):
#         # Create directory
#         test_output = EggnogOutputDirFmt()
#
#         # trying putting a file in...
#         shutil.copy(self.get_data_path("sample_eggnog_annotations.annotations"),
#                     test_output.path)
#
#         shutil.copy(self.get_data_path("sample_annotations.txt"),
#                     test_output.path)
#         test_output.save(self.get_data_path("test_output.qza"))
#         artifacted = _return_artifact(test_output)
#
#         fh = Artifact.load(artifacted)
#         self.assertIn("sample_annotations.txt", fh)


def _return_artifact(fmtd_object):
    return fmtd_object
