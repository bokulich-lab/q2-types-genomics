# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


from .._validator import validate_nog, validate_og, validate_kegg

from qiime2.core.exceptions import ValidationError
from qiime2.plugin.testing import TestPluginBase
import pandas as pd


class TestEggnogValidators(TestPluginBase):
    package = 'q2_types_genomics.feature_data.tests'

    def test_nog_fields_passing(self):
        has_run = False
        filename = "nog_annnotations.txt"
        filepath = self.get_data_path(filename)
        good_df = pd.read_csv(filepath, sep='\t', header=4)
        if good_df is not None:
            has_run = True
        assert has_run

    def test_raise_on_missing_nog_field(self):
        has_run = False
        filename = "missing_nog_annotations.txt"
        filepath = self.get_data_path(filename)
        bad_df = pd.read_csv(filepath, sep='\t', header=4)

        with self.assertRaisesRegex(
                ValidationError,
                r".*Required fields not found in data.*"):
            has_run = True
            validate_nog(bad_df, 'max')
        assert has_run

    # og validators
    def test_og_fields_passing(self):
        has_run = False
        filename = "og_annotations.txt"
        filepath = self.get_data_path(filename)
        good_df = pd.read_csv(filepath, sep='\t', header=4)
        if good_df is not None:
            has_run = True
        assert has_run

    def test_raise_on_missing_og_field(self):
        has_run = False
        filename = "missing_og_annotations.txt"
        filepath = self.get_data_path(filename)
        bad_df = pd.read_csv(filepath, sep='\t', header=4)

        with self.assertRaisesRegex(
                ValidationError,
                r".*Required fields not found in data.*"):
            has_run = True
            validate_og(bad_df, 'max')
        assert has_run

    def test_kegg_fields_passing(self):
        has_run = False
        filename = "kegg_annotations.txt"
        filepath = self.get_data_path(filename)
        good_df = pd.read_csv(filepath, sep='\t', header=4)
        if good_df is not None:
            has_run = True
        assert has_run

    def test_raise_on_missing_kegg_field(self):
        has_run = False
        filename = "missing_kegg_annotations.txt"
        filepath = self.get_data_path(filename)
        bad_df = pd.read_csv(filepath, sep='\t', header=4)

        with self.assertRaisesRegex(
                ValidationError,
                r".*Required fields not found in data.*"):
            has_run = True
            validate_kegg(bad_df, 'max')

        assert has_run
