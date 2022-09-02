# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


from qiime2.plugin import model
from ._util import parse_header_line, parse_footer_line
from qiime2.plugin import ValidationError

from ..plugin_setup import plugin

import re

class EggnogRefBinFileFmt(model.BinaryFileFormat):
    def _validate_(self, level):
        pass


class EggnogRefTextFileFmt(model.TextFileFormat):
    def _validate_(self, level):
        pass


plugin.register_formats(EggnogRefBinFileFmt, EggnogRefTextFileFmt)

# Below is the definition for a Directory Format to hold all of the refer
# databases for eggnog mapper, this probably should be moved somewhere else in
# the future, possibly an eggnog specificy module in this plugin


class EggnogRefDirFmt(model.DirectoryFormat):
    # match annotations
    # [any]\.[any]\."annotations"

    eggnog_db = model.File(r"eggnog\.db",
                           format=EggnogRefBinFileFmt)

    eggnog_tax = model.File(r"eggnog\.taxa\.tar",
                            format=EggnogRefBinFileFmt)

    eggnog_proteins = model.File(r"eggnog_proteins\.dmnd",
                                 format=EggnogRefBinFileFmt)

    novel_fams = model.File(r"novel_fams.dmnd",
                            format=EggnogRefBinFileFmt)

    eggnogtaxadbtraversepkl = model.File(r"eggnog.taxa.db.traverse.pkl",
                                         format=EggnogRefBinFileFmt)

    def _validate_(self, level):
        pass


plugin.register_formats(EggnogRefDirFmt)

class EggnogOutputDirFmt(model.DirectoryFormat):
    annotations = model.File(r".*\..*\.annotations",
                             format=EggnogRefBinFileFmt)

    gene_pred_seqs = model.File(r".*\.*\.genepred\.fasta",
                                format=EggnogRefTextFileFmt
                                )

    gene_pred_gff = model.File(r".*\..*\.genepred.gff",
                               format=EggnogRefTextFileFmt
                               )

    seed_orthologs = model.File(r".*\..*\.seed_orthologs",
                                format=EggnogRefTextFileFmt
                                )
plugin.register_formats(EggnogOutputDirFmt)
# ----------------------------------------------------------------------------
