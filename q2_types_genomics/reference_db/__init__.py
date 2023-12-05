# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


from q2_types_genomics.reference_db._type import (
    ReferenceDB, Diamond, Eggnog, EggnogSequenceTaxa
)

from q2_types_genomics.reference_db._format import (
    EggnogRefDirFmt,
    EggnogRefTextFileFmt,
    EggnogRefBinFileFmt,
    DiamondDatabaseFileFmt,
    DiamondDatabaseDirFmt,
    EggnogSequenceTaxaDirFmt
    )

__all__ = [
    'ReferenceDB', 'Diamond', 'Eggnog', 'DiamondDatabaseFileFmt',
    'DiamondDatabaseDirFmt', 'EggnogRefDirFmt', 'EggnogRefTextFileFmt',
    'EggnogRefBinFileFmt', 'EggnogSequenceTaxaDirFmt', 'EggnogSequenceTaxa'
]
