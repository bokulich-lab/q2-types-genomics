# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import glob
import os

import pandas as pd
import skbio
from q2_types.feature_data._transformer import _fastaformats_to_series

from q2_types_genomics.genome_data import (
    GenesDirectoryFormat, ProteinsDirectoryFormat
)

from q2_types_genomics.plugin_setup import plugin


CONSTRUCTORS = {
    "DNA": skbio.DNA,
    "RNA": skbio.RNA,
    "protein": skbio.Protein
}


def _series_to_fasta(series, ff, seq_type="DNA"):
    fp = str(f"{ff.path}/{series.name}.fasta")
    with open(fp, 'w') as fh:
        for id_, seq in series.iteritems():
            if seq:
                sequence = CONSTRUCTORS[seq_type](seq, metadata={'id': id_})
                skbio.io.write(sequence, format='fasta', into=fh)


@plugin.register_transformer
def _1(dirfmt: GenesDirectoryFormat) -> pd.DataFrame:
    data = {}
    for fp in sorted(glob.glob(f"{str(dirfmt)}/*.fa*")):
        fname = os.path.splitext(os.path.basename(fp))[0]
        data[fname] = _fastaformats_to_series(fp, constructor=skbio.DNA)
    df = pd.DataFrame.from_dict(data, orient='index')
    df.index.name = 'Genome ID'
    df = df.astype(str).replace({'nan': None})
    return df


@plugin.register_transformer
def _2(df: pd.DataFrame) -> GenesDirectoryFormat:
    result = GenesDirectoryFormat()
    df.apply(_series_to_fasta, axis=1, ff=result, seq_type="DNA")
    return result


@plugin.register_transformer
def _3(dirfmt: ProteinsDirectoryFormat) -> pd.DataFrame:
    data = {}
    for fp in sorted(glob.glob(f"{str(dirfmt)}/*.fa*")):
        fname = os.path.splitext(os.path.basename(fp))[0]
        data[fname] = _fastaformats_to_series(fp, constructor=skbio.Protein)
    df = pd.DataFrame.from_dict(data, orient='index')
    df.index.name = 'Genome ID'
    df = df.astype(str).replace({'nan': None})
    return df


@plugin.register_transformer
def _4(df: pd.DataFrame) -> ProteinsDirectoryFormat:
    result = ProteinsDirectoryFormat()
    df.apply(_series_to_fasta, axis=1, ff=result, seq_type="protein")
    return result
