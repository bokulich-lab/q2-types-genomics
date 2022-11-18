# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import unittest

from q2_types.sample_data import SampleData
from qiime2.plugin.testing import TestPluginBase

from q2_types_genomics.kraken2._format import Kraken2ReportDirectoryFormat
from q2_types_genomics.kraken2._type import Kraken2Reports


class TestTypes(TestPluginBase):
    package = "q2_types_genomics.kraken2.tests"

    def test_reports_semantic_type_registration(self):
        self.assertRegisteredSemanticType(Kraken2Reports)

    def test_mags_semantic_type_to_format_registration(self):
        self.assertSemanticTypeRegisteredToFormat(
            SampleData[Kraken2Reports],
            Kraken2ReportDirectoryFormat
        )


if __name__ == '__main__':
    unittest.main()
