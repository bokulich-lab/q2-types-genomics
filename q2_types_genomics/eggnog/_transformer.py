# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


import os.path
import pandas as pd
from ..plugin_setup import plugin

from qiime2 import Metadata
from ..eggnog._format import ArbitraryHeaderTSVFmt

# EggnogTransformers
def _parse_annotation_fmt_to_dataframe(ff):
    df = pd.read_csv(str(ff), sep='\t', header=ff.header)
    df.columns = [each.strip("#") for each in df.columns]
    return df


def _tsvfmt_to_metadata(data: ArbitraryHeaderTSVFmt) -> Metadata:
    df = _parse_annotation_fmt_to_dataframe(data)
    df.index = df.index.astype(str).rename("id")
    return Metadata(df)


@plugin.register_transformer
def _6(data: ArbitraryHeaderTSVFmt) -> pd.DataFrame:
    return _parse_annotation_fmt_to_dataframe(data)


@plugin.register_transformer
def _7(df: pd.DataFrame) -> ArbitraryHeaderTSVFmt:
    ff = ArbitraryHeaderTSVFmt()
    df.to_csv(str(ff), sep='\t', header=True, index=True)
    return ff


@plugin.register_transformer
def _8(data: ArbitraryHeaderTSVFmt) -> Metadata:
    _tsvfmt_to_metadata(data)
