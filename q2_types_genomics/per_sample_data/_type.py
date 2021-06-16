# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from q2_types.sample_data import SampleData
from qiime2.core.type import SemanticType

from . import (
    MultiMAGSequencesDirFmt, ContigSequencesDirFmt, MultiBowtie2IndexDirFmt
)
from ..plugin_setup import plugin

MAGs = SemanticType(
    'MAGs', variant_of=SampleData.field['type'])
Contigs = SemanticType(
    'Contigs', variant_of=SampleData.field['type'])
MultiBowtie2Index = SemanticType(
    'MultiBowtie2Index', variant_of=SampleData.field['type'])

plugin.register_semantic_types(MAGs, Contigs, MultiBowtie2Index)

plugin.register_semantic_type_to_format(
    SampleData[MAGs],
    artifact_format=MultiMAGSequencesDirFmt
)
plugin.register_semantic_type_to_format(
    SampleData[Contigs],
    artifact_format=ContigSequencesDirFmt
)
plugin.register_semantic_type_to_format(
    SampleData[MultiBowtie2Index],
    artifact_format=MultiBowtie2IndexDirFmt
)
