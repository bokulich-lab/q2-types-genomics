# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.plugin.testing import TestPluginBase

from q2_types_genomics.reference_db._format import (
        DiamondDatabaseFileFmt, DiamondDatabaseDirFmt, EggnogRefBinFileFmt,
        EggnogRefDirFmt, NCBITaxonomyNamesFormat, NCBITaxonomyNodesFormat,
        NCBITaxonomyDirFmt, NCBITaxonomyBinaryFileFmt
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


class TestNCBIFormats(TestPluginBase):
    package = "q2_types_genomics.reference_db.tests"

    def test_ncbi_tax_names_dmp_ok(self):
        fp = self.get_data_path("ncbi/names-ok.dmp")
        format = NCBITaxonomyNamesFormat(fp, "r")
        format.validate()

    def test_ncbi_tax_names_dmp_too_few_cols(self):
        fp = self.get_data_path("ncbi/names-wrong-cols.dmp")
        format = NCBITaxonomyNamesFormat(fp, "r")
        with self.assertRaisesRegex(
                ValidationError, r"found 3 columns on line 2."
        ):
            format.validate()

    def test_ncbi_tax_names_dmp_nonnumeric(self):
        fp = self.get_data_path("ncbi/names-non-numeric.dmp")
        format = NCBITaxonomyNamesFormat(fp, "r")
        with self.assertRaisesRegex(
                ValidationError, r"value on line 3: x."
        ):
            format.validate()

    def test_ncbi_tax_nodes_dmp_ok(self):
        fp = self.get_data_path("ncbi/nodes-ok.dmp")
        format = NCBITaxonomyNodesFormat(fp, "r")
        format.validate()

    def test_ncbi_tax_nodes_dmp_too_few_cols(self):
        fp = self.get_data_path("ncbi/nodes-wrong-cols.dmp")
        format = NCBITaxonomyNodesFormat(fp, "r")
        with self.assertRaisesRegex(
                ValidationError, r"found 12 columns on line 2."
        ):
            format.validate()

    def test_ncbi_tax_nodes_dmp_nonnumeric_id(self):
        fp = self.get_data_path("ncbi/nodes-non-numeric.dmp")
        format = NCBITaxonomyNodesFormat(fp, "r")
        with self.assertRaisesRegex(ValidationError, r"value on line 3."):
            format.validate()

    def test_ncbi_tax_nodes_dmp_nonnumeric_other(self):
        fp = self.get_data_path("ncbi/nodes-non-numeric-other.dmp")
        format = NCBITaxonomyNodesFormat(fp, "r")
        with self.assertRaisesRegex(ValidationError, r"line 2, column 6: x."):
            format.validate()

    def test_ncbi_taxonomy_dir_fmt(self):
        dirpath = self.get_data_path("ncbi/db-valid")
        format = NCBITaxonomyDirFmt(dirpath, mode="r")
        format.validate()

    def test_binary_file_fmt_positive(self):
        dirpath = self.get_data_path("ncbi/db-valid/prot.accession2taxid.gz")
        format = NCBITaxonomyBinaryFileFmt(dirpath, mode="r")
        format.validate()

    def test_binary_file_fmt_wrong_col(self):
        dirpath = self.get_data_path("ncbi/wrong_col.gz")
        format = NCBITaxonomyBinaryFileFmt(dirpath, mode="r")
        with self.assertRaises(ValidationError):
            format.validate()

    def test_binary_file_fmt_extra_col(self):
        dirpath = self.get_data_path("ncbi/too_many_cols.gz")
        format = NCBITaxonomyBinaryFileFmt(dirpath, mode="r")
        with self.assertRaises(ValidationError):
            format.validate()

    def test_binary_file_fmt_wrong_accession(self):
        dirpath = self.get_data_path("ncbi/wrong_accession.gz")
        format = NCBITaxonomyBinaryFileFmt(dirpath, mode="r")
        with self.assertRaises(ValidationError):
            format.validate()

    def test_binary_file_fmt_wrong_accession_version(self):
        dirpath = self.get_data_path("ncbi/wrong_accession_version.gz")
        format = NCBITaxonomyBinaryFileFmt(dirpath, mode="r")
        with self.assertRaises(ValidationError):
            format.validate()

    def test_binary_file_fmt_wrong_taxid(self):
        dirpath = self.get_data_path("ncbi/wrong_taxid.gz")
        format = NCBITaxonomyBinaryFileFmt(dirpath, mode="r")
        with self.assertRaises(ValidationError):
            format.validate()

    def test_binary_file_fmt_wrong_gi(self):
        dirpath = self.get_data_path("ncbi/wrong_gi.gz")
        format = NCBITaxonomyBinaryFileFmt(dirpath, mode="r")
        with self.assertRaises(ValidationError):
            format.validate()
