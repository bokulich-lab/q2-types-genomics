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
    Kraken2ReportFormat, Kraken2ReportDirectoryFormat
)


class TestFormats(TestPluginBase):
    package = 'q2_types_genomics.kraken2.tests'

    def test_report_format_ok(self):
        report_fp = self.get_data_path('reports-single/report-ok.txt')
        fmt = Kraken2ReportFormat(report_fp, mode='r')
        fmt.validate()

    def test_report_format_missing_col(self):
        report_fp = self.get_data_path(
            'reports-single/report-missing-column.txt'
        )
        fmt = Kraken2ReportFormat(report_fp, mode='r')

        with self.assertRaisesRegex(
            ValidationError, '5 were found'
        ):
            fmt.validate()

    def test_report_format_wrong_types(self):
        report_fp = self.get_data_path(
            'reports-single/report-wrong-types.txt'
        )
        fmt = Kraken2ReportFormat(report_fp, mode='r')

        with self.assertRaisesRegex(
            ValidationError,
                'Expected <class \'float\'> type in the '
                '"perc_frags_covered" column, got int64'
        ):
            fmt.validate()

    def test_report_dirfmt_from_reads(self):
        dirpath = self.get_data_path('reports-reads')
        format = Kraken2ReportDirectoryFormat(dirpath, mode='r')
        format.validate()

    def test_report_dirfmt_from_mags(self):
        dirpath = self.get_data_path('reports-mags')
        format = Kraken2ReportDirectoryFormat(dirpath, mode='r')
        format.validate()


if __name__ == '__main__':
    unittest.main()
