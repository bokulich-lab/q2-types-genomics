# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from q2_types.feature_data import DNAFASTAFormat
from qiime2.plugin import model

from ..plugin_setup import plugin


class MAGFASTAFormat(DNAFASTAFormat):
    pass


MAGSequencesDirFmt = model.SingleFileDirectoryFormat(
    'MAGSequencesDirFmt', r'mag[0-9]+\.(fa|fasta)$', MAGFASTAFormat)

plugin.register_formats(
    MAGSequencesDirFmt
)
