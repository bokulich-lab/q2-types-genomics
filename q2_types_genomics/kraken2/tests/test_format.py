# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import unittest

from qiime2.core.exceptions import ValidationError
from qiime2.plugin.testing import TestPluginBase

from q2_types_genomics.kraken2._format import (
    Kraken2ReportFormat
)


class TestFormats(TestPluginBase):
    package = 'q2_types_genomics.kraken2.tests'

    def test_genes_dirfmt_fa(self):
        report_fp = self.get_data_path('kraken2_report.txt')
        fmt = Kraken2ReportFormat(report_fp, mode='r')

        fmt.validate()

    # def test_proteins_dirfmt_fa(self):
    #     dirpath = self.get_data_path('proteins')
    #     fmt = ProteinsDirectoryFormat(dirpath, mode='r')
    #
    #     fmt.validate()
    #
    # def test_gff_format_positive(self):
    #     filepath = self.get_data_path('loci/loci1.gff')
    #     fmt = GFF3Format(filepath, mode='r')
    #
    #     fmt.validate()
    #
    # def test_loci_dirfmt(self):
    #     dirpath = self.get_data_path('loci')
    #     fmt = LociDirectoryFormat(dirpath, mode='r')
    #
    #     fmt.validate()
    #
    # def test_gff_format_wrong_version(self):
    #     filepath = self.get_data_path('loci-invalid/loci-wrong-version.gff')
    #     with self.assertRaisesRegex(
    #             ValidationError, 'Invalid GFF format version: 2.'):
    #         GFF3Format(filepath, mode='r').validate()
    #
    # def test_gff_format_no_version(self):
    #     filepath = self.get_data_path('loci-invalid/loci-no-version.gff')
    #     with self.assertRaisesRegex(
    #             ValidationError, '"gff-version" directive is missing'):
    #         GFF3Format(filepath, mode='r').validate()
    #
    # def test_gff_format_empty_directive(self):
    #     filepath = self.get_data_path('loci-invalid/loci-directive-empty.gff')
    #     with self.assertRaisesRegex(
    #             ValidationError, 'directive entry on line 1 is incomplete.'):
    #         GFF3Format(filepath, mode='r').validate()
    #
    # def test_gff_format_lines_nonequal(self):
    #     filepath = self.get_data_path('loci-invalid/loci-lines-unequal.gff')
    #     with self.assertRaisesRegex(
    #             ValidationError, 'line 9 has an incorrect number of elements'):
    #         GFF3Format(filepath, mode='r').validate()
    #
    # def test_gff_format_empty_feature(self):
    #     filepath = self.get_data_path('loci-invalid/loci-empty-feature.gff')
    #     with self.assertRaisesRegex(
    #             ValidationError, r'empty feature found on line 9'):
    #         GFF3Format(filepath, mode='r').validate()
    #
    # def test_gff_format_invalid_char(self):
    #     filepath = self.get_data_path('loci-invalid/loci-invalid-char.gff')
    #     with self.assertRaisesRegex(
    #             ValidationError, r'unescaped ">". The ID on line 10 '
    #                              r'was ">AL123456.3"'):
    #         GFF3Format(filepath, mode='r').validate()
    #
    # def test_gff_format_invalid_start_stop(self):
    #     filepath = self.get_data_path('loci-invalid/loci-invalid-start.gff')
    #     with self.assertRaisesRegex(
    #             ValidationError, 'position on line 9 is bigger than stop'):
    #         GFF3Format(filepath, mode='r').validate()
    #
    # def test_gff_format_negative_position(self):
    #     filepath = self.get_data_path('loci-invalid/loci-negative-start.gff')
    #     with self.assertRaisesRegex(
    #             ValidationError, 'positions on line 8 is incorrect'):
    #         GFF3Format(filepath, mode='r').validate()
    #
    # def test_gff_format_invalid_strand(self):
    #     filepath = self.get_data_path('loci-invalid/loci-invalid-strand.gff')
    #     with self.assertRaisesRegex(
    #             ValidationError, 'feature on line 10 is not one '
    #                              'of the allowed'):
    #         GFF3Format(filepath, mode='r').validate()
    #
    # def test_gff_format_invalid_phase(self):
    #     filepath = self.get_data_path('loci-invalid/loci-invalid-phase.gff')
    #     with self.assertRaisesRegex(
    #             ValidationError, 'The phase on line 10 was 8.'):
    #         GFF3Format(filepath, mode='r').validate()


if __name__ == '__main__':
    unittest.main()
