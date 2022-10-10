# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


import importlib

from ._format import (
        EggnogRefBinFileFmt, EggnogRefTextFileFmt, EggnogRefDirFmt,
        EggnogOutputDirFmt, PfamDirFmt, DiamondRefDirFmt, MMseqsDirFmt,
        ArbitraryHeaderTSVFmt, ArbitraryHeaderTSVDirFmt
        )

from ._type import (
        Orthologs, Seed, Eggnog, ReferenceDB, Annotation, NOG, KEGG, OG,
        EggnogDB,
        )

__all__ = [
        'EggnogRefBinFileFmt', 'EggnogRefTextFileFmt', 'EggnogRefDirFmt',
        'EggnogOutputDirFmt', 'Eggnog', 'ReferenceDB', 'PfamDirFmt',
        'DiamondRefDirFmt',  'MMseqsDirFmt', 'Orthologs', 'Seed', 'ArbitraryHeaderTSVFmt',
        'ArbitraryHeaderTSVDirFmt', 'EggnogDB', 'KEGG', 'OG', 'DiamondDB', 'MMseq2DB',
        'NOG',
        ]

importlib.import_module('q2_types_genomics.eggnog._transformer')
importlib.import_module('q2_types_genomics.eggnog._validator')
    #'ArbitraryHeaderTSVDirFmt',
     #'BinaryReferenceDBFmt',
    #'BinaryReferenceDBDirFmt',
    #ArbitraryHeaderTSVDirFmt, #BinaryReferenceDBFmt, BinaryReferenceDBDirFmt,

