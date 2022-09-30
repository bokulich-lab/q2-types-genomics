# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


from qiime2.plugin import model
from q2_types_genomics.feature_data._util import (
        parse_header_line, parse_footer_line,
        )

from qiime2.plugin import ValidationError

from ..plugin_setup import plugin

import re

class EggnogRefBinFileFmt(model.BinaryFileFormat):
    def _validate_(self, level):
        pass


class EggnogRefTextFileFmt(model.TextFileFormat):
    def _validate_(self, level):
        pass


plugin.register_formats(EggnogRefBinFileFmt)
plugin.register_formats(EggnogRefTextFileFmt)

# Below is the definition for a Directory Format to hold all of the refer
# databases for eggnog mapper, this probably should be moved somewhere else in
# the future, possibly an eggnog specificy module in this plugin

class HmmerDirFmt(model.DirectoryFormat):
    pass

class MMseqsDirFmt(model.DirectoryFormat):
    mmseqs_db=model.File(r"mmseqs.db",
                      format=EggnogRefBinFileFmt,
                      optional=False)

    mmseqs_dbtype=model.File(r"mmseqs.db.dbtype",
                      format=EggnogRefBinFileFmt,
                      optional=False)

    mmseqs_index=model.File(r"mmseqs.db.index",
                            format=EggnogRefBinFileFmt,
                            optional=False)

    mmseqs_lookup=model.File(r"mmseqs.db.lookup",
                             format=EggnogRefBinFileFmt,
                             optional=True)

    mmseqs_source=model.File(r"mmseqs.db.source",
                             format=EggnogRefBinFileFmt,
                             optional=True)

    mmseqs_h_db=model.File(r"mmseqs.db_h",
                           format=EggnogRefBinFileFmt,
                           optional=True)

    mmseqs_h_dbtype=model.File(r"mmseqs.db_h.dbtype",
                               format=EggnogRefBinFileFmt,
                               optional=True)

    mmseqs_h_index=model.File(r"mmseqs.db_h.index",
                              format=EggnogRefBinFileFmt,
                              optional=True)


class PfamDirFmt(model.DirectoryFormat):

    clans=model.File(r"Pfam-A.clans.tsv.gz",
                       format=EggnogRefBinFileFmt,
                       optional=False)

    base=model.File(r"Pfam-A.hmm",
                       format=EggnogRefBinFileFmt,
                       optional=False)

    h3f=model.File(r"Pfam-A.hmm.h3f",
                       format=EggnogRefBinFileFmt,
                       optional=False)

    h3i=model.File(r"Pfam-A.hmm.h3i",
                    format=EggnogRefBinFileFmt,
                    optional=False)

    h3m=model.File(r"Pfam-A.hmm.h3m",
                     format=EggnogRefBinFileFmt,
                     optional=False)

    ssi=model.File(r"Pfam-A.hmm.h3m.ssi",
                       format=EggnogRefBinFileFmt,
                       optional=False)

    h3p=model.File(r"Pfam-A.hmm.h3p",
                       format=EggnogRefBinFileFmt,
                       optional=False)

    idmap=model.File(r"Pfam-A.hmm.idmap",
                       format=EggnogRefBinFileFmt,
                       optional=False)


class DiamondRefDirFmt(model.DirectoryFormat):

    eggnog_proteins = model.File(r"eggnog_proteins\.dmnd",
                                 format=EggnogRefBinFileFmt,
                                 optional=True)

    novel_fams = model.File(r"novel_fams.dmnd",
                            format=EggnogRefBinFileFmt,
                            optional=True)


class EggnogRefDirFmt(model.DirectoryFormat):

    eggnog_db = model.File(r"eggnog\.db",
                           format=EggnogRefBinFileFmt,
                           optional=True)

    eggnog_taxa = model.File(r"eggnog\.taxa\.db",
                            format=EggnogRefBinFileFmt,
                            optional=True)

    eggnog_taxa_pkl = model.File(r"eggnog.taxa.db.traverse.pkl",
                                 format=EggnogRefBinFileFmt,
                                 optional=True)


"""
eggnog.db
eggnog.taxa.db
eggnog.taxa.db.traverse.pkl
eggnog_proteins.dmnd
novel_fams.dmnd

hmmer
mmseqs
pfam
"""





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
