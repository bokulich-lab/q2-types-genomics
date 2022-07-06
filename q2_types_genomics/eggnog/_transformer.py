# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


from ..plugin_setup import plugin
from ._format import ArbitraryHeaderTSVFmt
import pandas as pd
from qiime2 import Metadata


def _parse_annotation_fmt_to_dataframe(ff):
    df = pd.read_csv(str(ff), sep='\t', header=ff.header)
    return df


def _tsvfmt_to_metadata(data: ArbitraryHeaderTSVFmt) -> Metadata:
    df = _parse_annotation_fmt_to_dataframe(data)
    df.index = df.index.astype(str).rename("id")
    return Metadata(df)


@plugin.register_transformer
def _1(data: ArbitraryHeaderTSVFmt) -> pd.DataFrame:
    return _parse_annotation_fmt_to_dataframe(data)


@plugin.register_transformer
def _2(df: pd.DataFrame) -> ArbitraryHeaderTSVFmt:
    ff = ArbitraryHeaderTSVFmt()
    df.to_csv(str(ff), sep='\t', header=True, index=True)
    return ff


@plugin.register_transformer
def _3(data: ArbitraryHeaderTSVFmt) -> Metadata:
    _tsvfmt_to_metadata(data)
