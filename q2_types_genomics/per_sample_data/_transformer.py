# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from q2_types.feature_data import DNAFASTAFormat

from q2_types_genomics.plugin_setup import plugin

from q2_types_genomics.per_sample_data._util import _mag_manifest_helper
from q2_types_genomics.per_sample_data._format import (
    MultiMAGManifestFormat,
    MAGSequencesDirFmt,
    MultiFASTADirectoryFormat
)


@plugin.register_transformer
def _1(dirfmt: MultiFASTADirectoryFormat) \
        -> MAGSequencesDirFmt:
    return _mag_manifest_helper(
        dirfmt, MAGSequencesDirFmt, MultiMAGManifestFormat, DNAFASTAFormat)
