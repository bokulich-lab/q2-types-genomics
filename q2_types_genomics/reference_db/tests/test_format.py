# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2.plugin.testing import TestPluginBase

from q2_types_genomics.reference_db._format import (
        DiamondDatabaseFileFmt, DiamondDatabaseDirFmt
        )
from q2_types_genomics.reference_db._type import ReferenceDB, Diamond
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

    def test_diamond_semantic_type_registered_to_dmnd_db_dir_fmt(self):
        self.assertSemanticTypeRegisteredToFormat(
                ReferenceDB[Diamond],
                DiamondDatabaseDirFmt
                )
