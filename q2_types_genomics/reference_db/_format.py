# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


from qiime2.plugin import model
from qiime2.core.exceptions import ValidationError
from q2_types_genomics.plugin_setup import plugin
from q2_types_genomics.reference_db._type import (
    ReferenceDB, Eggnog, Diamond, NCBITaxonomy
)


class EggnogRefTextFileFmt(model.TextFileFormat):
    def _validate_(self, level):
        # TODO: have native diamond validation run on db/self.path
        pass


class EggnogRefBinFileFmt(model.BinaryFileFormat):
    def _validate_(self, level):
        pass


plugin.register_formats(EggnogRefTextFileFmt, EggnogRefBinFileFmt)


class EggnogRefDirFmt(model.DirectoryFormat):
    eggnog = model.FileCollection(r'eggnog.*db.*',
                                  format=EggnogRefBinFileFmt)

    @eggnog.set_path_maker
    def eggnog_path_maker(self, name):
        return str(name)


plugin.register_formats(EggnogRefDirFmt)

plugin.register_semantic_type_to_format(
        ReferenceDB[Eggnog],
        EggnogRefDirFmt)


class DiamondDatabaseFileFmt(model.BinaryFileFormat):
    def _validate_(self, level):
        # TODO: have native diamond validation run on db/self.path
        pass


DiamondDatabaseDirFmt = model.SingleFileDirectoryFormat(
    'DiamondDatabaseDirFmt', 'ref_db.dmnd', DiamondDatabaseFileFmt)

plugin.register_formats(DiamondDatabaseFileFmt, DiamondDatabaseDirFmt)
plugin.register_semantic_type_to_format(ReferenceDB[Diamond],
                                        DiamondDatabaseDirFmt)


class NCBITaxonomyNodesFormat(model.TextFileFormat):
    def _validate_n_records(self, n=None):
        with open(str(self), "r") as fh:
            file_ = enumerate(fh) if n is None else zip(range(n), fh)

            for i, line in file_:
                line = line.rstrip("\n").split("\t|\t")
                if 13 > len(line) or len(line) > 18:
                    raise ValidationError(
                        "NCBI taxonomy nodes file must have 13 columns, "
                        f"found {len(line)} columns on line {i + 1}."
                    )
                if not line[0].isnumeric() or not line[1].isnumeric():
                    raise ValidationError(
                        "NCBI taxonomy nodes file must contain a numeric "
                        "taxonomy ID in the first two columns, found "
                        f"non-numeric value on line {i + 1}."
                    )
                for col in (5, 7, 9, 10, 11):
                    if not line[col].isnumeric() or \
                            not int(line[col]) in (0, 1):
                        raise ValidationError(
                            "NCBI taxonomy nodes file must contain 0 or 1 "
                            "in columns 6, 8, 10, 11, and 12, found a "
                            f"non-allowed value on line {i + 1}, column "
                            f"{col + 1}: {line[col]}."
                        )

    def _validate_(self, level):
        self._validate_n_records(n={"min": 10, "max": None}[level])


class NCBITaxonomyNamesFormat(model.TextFileFormat):
    def _validate_n_records(self, n=None):
        with open(str(self), "r") as fh:
            file_ = enumerate(fh) if n is None else zip(range(n), fh)

            for i, line in file_:
                line = line.rstrip("\n").split("\t|\t")
                if len(line) != 4:
                    raise ValidationError(
                        "NCBI taxonomy names file must have 4 columns, "
                        f"found {len(line)} columns on line {i + 1}."
                    )
                if not line[0].isnumeric():
                    raise ValidationError(
                        "NCBI taxonomy name file must contain a numeric "
                        "taxonomy ID in the first column, found non-numeric "
                        f"value on line {i + 1}: {line[0]}."
                    )

    def _validate_(self, level):
        self._validate_n_records(n={"min": 10, "max": None}[level])


class NCBITaxonomyBinaryFileFmt(model.TextFileFormat):
    def _validate_(self, level):
        pass


plugin.register_formats(
    NCBITaxonomyNodesFormat, NCBITaxonomyNamesFormat, NCBITaxonomyBinaryFileFmt
    )


class NCBITaxonomyDirFmt(model.DirectoryFormat):
    node = model.File('nodes.dmp', format=NCBITaxonomyNodesFormat)
    names = model.File('names.dmp', format=NCBITaxonomyNamesFormat)
    tax_map = model.File(
        'prot.accession2taxid.gz',
        format=NCBITaxonomyBinaryFileFmt
        )


plugin.register_formats(NCBITaxonomyDirFmt)

plugin.register_semantic_type_to_format(
        ReferenceDB[NCBITaxonomy],
        NCBITaxonomyDirFmt)
