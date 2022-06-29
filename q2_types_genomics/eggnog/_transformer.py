# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


from ..plugin_setup import plugin
from ._format import EggnogAnnotationFmt
import pandas as pd


def _parse_annotation_fmt_to_dataframe(ff):
    df = pd.read_csv(str(ff), sep='\t', header=ff.header)
    return df

def _parse_headerless_annotation_fmt_to_dataframe(ff):
    df = pd.read_csv(str(ff), sep='\t', header=None)
    return df

@plugin.register_transformer
def _1(data: EggnogAnnotationFmt) -> pd.DataFrame:
    return _parse_annotation_fmt_to_dataframe(data)
