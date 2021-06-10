# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from q2_types.feature_data import DNAFASTAFormat, ProteinFASTAFormat
import qiime2.plugin.model as model

from ..plugin_setup import plugin


class GenesDirectoryFormat(model.DirectoryFormat):
    genes = model.FileCollection(r'genes[0-9]+\.(fa|fna|fasta)$',
                                 format=DNAFASTAFormat)

    @genes.set_path_maker
    def genes_path_maker(self, genome_id):
        return '%s_genes.fasta' % genome_id


class ProteinsDirectoryFormat(model.DirectoryFormat):
    proteins = model.FileCollection(r'proteins[0-9]+\.(fa|faa|fasta)$',
                                    format=ProteinFASTAFormat)

    @proteins.set_path_maker
    def proteins_path_maker(self, genome_id):
        return '%s_proteins.fasta' % genome_id


plugin.register_formats(GenesDirectoryFormat, ProteinsDirectoryFormat)
