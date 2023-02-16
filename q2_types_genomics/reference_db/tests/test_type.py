# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.plugin.testing import TestPluginBase

from q2_types_genomics.reference_db._format import DiamondDatabaseDirFmt
from q2_types_genomics.reference_db._type import ReferenceDB, Diamond


class TestReferenceType(TestPluginBase):
    package = 'q2_types_genomics.reference_db.tests'

    def test_ref_db_registration(self):
        self.assertRegisteredSemanticType(ReferenceDB)

    def test_diamond_registration(self):
        self.assertRegisteredSemanticType(Diamond)

    def test_diamond_semantic_type_registered_to_dmnd_db_dir_fmt(self):
        self.assertSemanticTypeRegisteredToFormat(
                ReferenceDB[Diamond],
                DiamondDatabaseDirFmt)
