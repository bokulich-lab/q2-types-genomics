# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


from qiime2.core.exceptions import ValidationError
from qiime2.plugin.testing import TestPluginBase
from qiime2 import Artifact


class TestEggnogValidators(TestPluginBase):
    package = 'q2_types_genomics.feature_data.tests'
    # these tests implicitly run the validators on instatiation/data loading
    # noqa comments are to have flake8 ignore errors from assigned but
    # un-accessed variables

    def test_nog_fields_passing(self):
        has_run = False
        filename = "nog_annotations.txt"
        filepath = self.get_data_path(filename)

        good_nog, has_run = (  # noqa: F841
            Artifact.import_data("FeatureData[NOG]", filepath),
            True,
        )

        assert has_run

    def test_raise_on_missing_nog_field(self):
        has_run = False
        filename = "missing_nog_annotations.txt"
        filepath = self.get_data_path(filename)

        with self.assertRaisesRegex(
                ValidationError,
                "Required fields not found in data: "
                "{'seed_eggNOG_ortholog'}"):
            has_run = True
            bad_nog = Artifact.import_data(  # noqa: F841
                "FeatureData[NOG]",
                filepath)

        assert has_run

    # og validators
    def test_og_fields_passing(self):
        has_run = False
        filename = "og_annotations.txt"
        filepath = self.get_data_path(filename)

        good_og, has_run = (  # noqa: F841
                Artifact.import_data("FeatureData[OG]", filepath),
                True
        )

        assert has_run

    def test_raise_on_missing_og_field(self):
        has_run = False
        filename = "missing_og_annotations.txt"
        filepath = self.get_data_path(filename)

        with self.assertRaisesRegex(
                ValidationError,
                "Required fields not found in data: {"
                "'(eggNOG OGs|narr_og_cat|narr_og_name)',"
                " '(eggNOG OGs|narr_og_cat|narr_og_name)',"
                " '(eggNOG OGs|narr_og_cat|narr_og_name)'}"):
            has_run = True
            bad_og = Artifact.import_data(  # noqa: F841
                "FeatureData[OG]",
                filepath
            )

        assert has_run

    def test_kegg_fields_passing(self):
        has_run = False
        filename = "kegg_annotations.txt"
        filepath = self.get_data_path(filename)

        good_kegg, has_run = (  # noqa: F841
            Artifact.import_data("FeatureData[KEGG]", filepath),
            True,
        )

        assert has_run

    def test_raise_on_missing_kegg_field(self):
        has_run = False
        filename = "missing_kegg_annotations.txt"
        filepath = self.get_data_path(filename)

        with self.assertRaisesRegex(
                ValidationError,
                r"Required fields not found in data: {'KEGG_Pathway'}"):
            has_run = True
            bad_kegg = Artifact.import_data(  # noqa: F841
                "FeatureData[KEGG]",
                filepath
            )

        assert has_run
