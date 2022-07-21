# ----------------------------------------------------------------------------
# Copyright (c) 2021-2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


from ..plugin_setup import plugin
from qiime2.core.exceptions import ValidationError

from q2_types.feature_data import FeatureData
from q2_types_genomics.feature_data import (NOG, OG, KEGG, )

import pandas as pd


nog_fields = {'query_name', 'seed_eggNOG_ortholog',
              'seed_ortholog_evalue', 'seed_ortholog_score',
              'eggNOG OGs', 'narr_og_name', 'narr_og_cat',
              'narr_og_desc', 'best_og_name', 'best_og_cat',
              'best_og_desc', 'Preferred_name', 'GOs', 'EC',
              'KEGG_ko', 'KEGG_Pathway', 'KEGG_Module', 'KEGG_Reaction',
              'KEGG_rclass', 'BRITE', 'KEGG_TC', 'CAZy',
              'BiGG_Reaction', 'PFAMs',
              }

og_fields = {'eggNOG OGs', 'narr_og_name', 'narr_og_cat',
             'narr_og_desc',
             }

kegg_fields = {'KEGG_ko', 'KEGG_Pathway', 'KEGG_Module', 'KEGG_Reaction',
               'KEGG_rclass', 'BRITE', 'KEGG_TC',
               }


@plugin.register_validator(FeatureData[NOG])
def validate_nog(data: pd.DataFrame, level='max'):
    _check_fields(data=data, level=level, reference_fields=nog_fields)


@plugin.register_validator(FeatureData[OG])
def validate_og(data: pd.DataFrame, level='max'):
    _check_fields(data=data, level=level, reference_fields=og_fields)


@plugin.register_validator(FeatureData[KEGG])
def validate_kegg(data: pd.DataFrame, level='max'):
    _check_fields(data=data, level=level, reference_fields=kegg_fields)


def _check_fields(data: pd.DataFrame, level, reference_fields):
    df_labels_set = set(data.columns)
    if not reference_fields.issubset(df_labels_set):
        raise ValidationError(
                "Required fields not found in data: {}".format(
                    reference_fields.difference(df_labels_set)))
