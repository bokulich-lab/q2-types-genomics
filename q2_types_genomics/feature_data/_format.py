# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from q2_types.feature_data import DNAFASTAFormat
from q2_types_genomics.genome_data._format import OrthologFileFmt
from qiime2.plugin import model

from ..plugin_setup import plugin


class MAGSequencesDirFmt(model.DirectoryFormat):
    sequences = model.FileCollection(
        r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-4[0-9a-fA-F]{3}-"
        r"[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}\.(fa|fasta)$",
        format=DNAFASTAFormat
    )

    @sequences.set_path_maker
    def sequences_path_maker(self, mag_id):
        return r'%s.fasta' % mag_id


plugin.register_formats(MAGSequencesDirFmt)


class OrthologAnnotationDirFmt(model.DirectoryFormat):
    annotations = model.FileCollection(
        r'.+\.annotations',
        format=OrthologFileFmt
    )

    @annotations.set_path_maker
    def annotations_path_maker(self, file_name):
        return file_name.split(sep="_")[0]


plugin.register_formats(OrthologAnnotationDirFmt)
