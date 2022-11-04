# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


from qiime2.plugin import model
from q2_types_genomics.ortholog import Ortholog, Seed, Annotation
from q2_types_genomics.plugin_setup import plugin


class OrthologFileFmt(model.TextFileFormat):
    def _validate_(self, level):
        pass


class SeedOrthologDirFmt(model.DirectoryFormat):
    seed_orthologs = model.File(r".*\..*\.seed_orthologs",
                                format=OrthologFileFmt)


plugin.register_formats(OrthologFileFmt, SeedOrthologDirFmt)

plugin.register_semantic_type_to_format(
    Ortholog[Seed],
    artifact_format=SeedOrthologDirFmt)

class AnnotationOrthologDirFmt(model.DirectoryFormat):
    annotation_orthologs = model.File(r".*\.emapper\.annotations",
                                      format=OrthologFileFmt)

plugin.register_formats(AnnotationOrthologDirFmt)

plugin.register_semantic_type_to_format(
    Ortholog[Annotation],
    artifact_format=AnnotationOrthologDirFmt)
