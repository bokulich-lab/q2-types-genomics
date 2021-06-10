# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import os

import pandas as pd
import skbio

from q2_types_genomics.genome_data import (
    GenesDirectoryFormat, ProteinsDirectoryFormat
)

from q2_types_genomics.plugin_setup import plugin


CONSTRUCTORS = {
    'DNA': skbio.DNA,
    'RNA': skbio.RNA,
    'protein': skbio.Protein
}


def _series_to_fasta(series, ff, seq_type='DNA'):
    fp = str(f"{ff.path}/{series.name}.fasta")
    with open(fp, 'w') as fh:
        for id_, seq in series.iteritems():
            if seq:
                sequence = CONSTRUCTORS[seq_type](seq, metadata={'id': id_})
                skbio.io.write(sequence, format='fasta', into=fh)


def _multi_sequences_to_df(seq_iter_view):
    data = {
        os.path.splitext(fp)[0]: pds
        for fp, pds in seq_iter_view
    }
    df = pd.DataFrame.from_dict(data, orient='index')
    df.index.name = 'Genome ID'
    df = df.astype(str).replace({'nan': None})
    return df


@plugin.register_transformer
def _1(dirfmt: GenesDirectoryFormat) -> pd.DataFrame:
    return _multi_sequences_to_df(dirfmt.genes.iter_views(pd.Series))


@plugin.register_transformer
def _2(df: pd.DataFrame) -> GenesDirectoryFormat:
    result = GenesDirectoryFormat()
    df.apply(_series_to_fasta, axis=1, ff=result, seq_type='DNA')
    return result


@plugin.register_transformer
def _3(dirfmt: ProteinsDirectoryFormat) -> pd.DataFrame:
    return _multi_sequences_to_df(dirfmt.proteins.iter_views(pd.Series))


@plugin.register_transformer
def _4(df: pd.DataFrame) -> ProteinsDirectoryFormat:
    result = ProteinsDirectoryFormat()
    df.apply(_series_to_fasta, axis=1, ff=result, seq_type='protein')
    return result
