# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.plugin.testing import TestPluginBase

from q2_types_genomics.reference_db._format import (
        DiamondDatabaseFileFmt, DiamondDatabaseDirFmt,
        EggnogRefBinFileFmt, EggnogRefDirFmt, EggnogSequenceTaxaDirFmt
        )
from qiime2.plugin import ValidationError


class TestRefFormats(TestPluginBase):
    package = 'q2_types_genomics.reference_db.tests'

    def test_dmnd_ff(self):
        dmd_obj = DiamondDatabaseFileFmt(
                self.get_data_path('dmnd_db/ref_db.dmnd'),
                mode='r'
                )

        dmd_obj.validate()

    def test_dmnd_df(self):
        dmnd_obj = DiamondDatabaseDirFmt(
                self.get_data_path('dmnd_db'),
                mode='r'
                )

        dmnd_obj.validate()

    def test_dmnd_dir_fmt_fails_bad_name(self):
        dmnd_obj = DiamondDatabaseDirFmt(

                self.get_data_path('bad_dmnd_db'),
                mode='r'
                )
        with self.assertRaisesRegexp(
                ValidationError,
                "Missing one or more files for DiamondDatabaseDirFmt"):
            dmnd_obj.validate()

    def test_eggnog_ref_bin_main(self):
        dirpath = self.get_data_path('good_eggnog/eggnog.db')
        fmt_obj = EggnogRefBinFileFmt(dirpath, mode='r')

        fmt_obj.validate()

    def test_eggnog_ref_bin_pickle(self):
        dirpath = self.get_data_path('good_eggnog/eggnog.taxa.db.traverse.pkl')
        fmt_obj = EggnogRefBinFileFmt(dirpath, mode='r')

        fmt_obj.validate()

    def test_eggnog_ref_bin_taxa(self):
        dirpath = self.get_data_path('good_eggnog/eggnog.taxa.db')
        fmt_obj = EggnogRefBinFileFmt(dirpath, mode='r')

        fmt_obj.validate()

    def test_eggnog_dir_fmt_all_files(self):
        dirpath = self.get_data_path('good_eggnog')
        fmt_obj = EggnogRefDirFmt(dirpath, mode='r')

        self.assertEqual(
                len([(relpath, obj) for relpath, obj
                     in fmt_obj.eggnog.iter_views(EggnogRefBinFileFmt)]),
                3)

    def test_eggnog_dir_fmt_single_file(self):
        dirpath = self.get_data_path('single_eggnog')
        fmt_obj = EggnogRefDirFmt(dirpath, mode='r')

        self.assertEqual(
                len([(relpath, obj) for relpath, obj
                     in fmt_obj.eggnog.iter_views(EggnogRefBinFileFmt)]),
                1)

        fmt_obj.validate()

    def test_eggnog_dir_fmt(self):
        dirpath = self.get_data_path('good_eggnog')
        fmt_obj = EggnogRefDirFmt(dirpath, mode='r')

        fmt_obj.validate()

    def test_eggnog_sequence_taxa_dir_fmt(self):
        dirpath = self.get_data_path('eggnog_seq_tax')
        fmt_obj = EggnogSequenceTaxaDirFmt(dirpath, mode='r')

        fmt_obj.validate()
