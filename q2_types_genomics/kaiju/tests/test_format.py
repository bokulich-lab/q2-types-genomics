# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
import unittest

from qiime2.core.exceptions import ValidationError
from qiime2.plugin.testing import TestPluginBase

from q2_types_genomics.kaiju._format import (
    KaijuDBDirectoryFormat,
    NCBITaxonomyNamesFormat,
    NCBITaxonomyNodesFormat,
)


class TestFormats(TestPluginBase):
    package = "q2_types_genomics.kaiju.tests"

    def test_kaiju_dirfmt(self):
        dirpath = self.get_data_path("db-valid")
        format = KaijuDBDirectoryFormat(dirpath, mode="r")
        format.validate()

    def test_ncbi_tax_names_dmp_ok(self):
        fp = self.get_data_path("names-ok.dmp")
        format = NCBITaxonomyNamesFormat(fp, "r")
        format.validate()

    def test_ncbi_tax_names_dmp_too_few_cols(self):
        fp = self.get_data_path("names-wrong-cols.dmp")
        format = NCBITaxonomyNamesFormat(fp, "r")
        with self.assertRaisesRegex(
                ValidationError, r"found 3 columns on line 2."
        ):
            format.validate()

    def test_ncbi_tax_names_dmp_nonnumeric(self):
        fp = self.get_data_path("names-non-numeric.dmp")
        format = NCBITaxonomyNamesFormat(fp, "r")
        with self.assertRaisesRegex(
                ValidationError, r"value on line 3: x."
        ):
            format.validate()

    def test_ncbi_tax_nodes_dmp_ok(self):
        fp = self.get_data_path("nodes-ok.dmp")
        format = NCBITaxonomyNodesFormat(fp, "r")
        format.validate()

    def test_ncbi_tax_nodes_dmp_too_few_cols(self):
        fp = self.get_data_path("nodes-wrong-cols.dmp")
        format = NCBITaxonomyNodesFormat(fp, "r")
        with self.assertRaisesRegex(
                ValidationError, r"found 12 columns on line 2."
        ):
            format.validate()

    def test_ncbi_tax_nodes_dmp_nonnumeric_id(self):
        fp = self.get_data_path("nodes-non-numeric.dmp")
        format = NCBITaxonomyNodesFormat(fp, "r")
        with self.assertRaisesRegex(ValidationError, r"value on line 3."):
            format.validate()

    def test_ncbi_tax_nodes_dmp_nonnumeric_other(self):
        fp = self.get_data_path("nodes-non-numeric-other.dmp")
        format = NCBITaxonomyNodesFormat(fp, "r")
        with self.assertRaisesRegex(ValidationError, r"line 2, column 6: x."):
            format.validate()


if __name__ == "__main__":
    unittest.main()
