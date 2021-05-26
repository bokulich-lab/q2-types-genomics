# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
import glob
import os.path

import pandas as pd
import skbio
from q2_types.feature_data._transformer import (_fastaformats_to_series)

from . import MAGFASTAFormat
from ..plugin_setup import plugin


@plugin.register_transformer
def _1(ff: MAGFASTAFormat) -> pd.DataFrame:
    data = {}
    for fp in glob.glob(f"{str(ff)}/*.fa*"):
        fname = os.path.splitext(os.path.basename(fp))[0]
        data[fname] = _fastaformats_to_series(fp, constructor=skbio.DNA)
    df = pd.DataFrame.from_dict(data, orient='index')
    df.index.name = 'Feature ID'
    df = df.astype(str)
    return df


def row_to_file(row, root=None):
    with open(os.path.join(root, f'{row.name}.fasta'), mode='w') as f:
        for id_, seq in row.iteritems():
            if seq:
                sequence = skbio.DNA(seq, metadata={'id': id_})
                skbio.io.write(sequence, format='fasta', into=f)
