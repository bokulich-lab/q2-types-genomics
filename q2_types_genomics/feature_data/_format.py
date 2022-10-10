# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from q2_types.feature_data import (
    DNAFASTAFormat,
)

from qiime2.plugin import model
from ._util import parse_header_line, parse_footer_line
from qiime2.plugin import ValidationError

from ..plugin_setup import plugin

import re

# mag
MAGSequencesDirFmt = model.SingleFileDirectoryFormat(
    'MAGSequencesDirFmt', r'mag[0-9]+\.(fa|fasta)$', DNAFASTAFormat)

plugin.register_formats(
    MAGSequencesDirFmt
)

