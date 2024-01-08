# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


import gzip
import re
import time
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


class NCBITaxonomyBinaryFileFmt(model.BinaryFileFormat):
    _accession_regex = re.compile(
        r'[OPQ][0-9][A-Z0-9]{3}[0-9]|'  # UniProt
        r'[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2}|'  # UniProt
        r'[A-Z]{3}\d{3,7}|'  # EMBL-EBI
        r'[A-Z]+[-._]?\d+'  # NCBI
    )
    _accession_version_regex = re.compile(
        r'[OPQ][0-9][A-Z0-9]{3}[0-9]\.\d+|'
        r'[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2}\.\d+|'
        r'[A-Z]{3}\d{3,7}\.\d+|'
        r'[A-Z]+[-._]?\d+\.\d+'
    )
    _taxid_regex = r'\d{1,10}'
    _gi_regex = r'\d+'
    _line_regex = re.compile(
        rf"^({_accession_regex.pattern})\t"
        rf"({_accession_version_regex.pattern})"
        rf"\t({_taxid_regex})"
        rf"\t({_gi_regex})\n$"
    )

    def _validate_1st_line(self, line: list):
        if not (
            line[0] == "accession" and
            line[1] == "accession.version" and
            line[2] == "taxid" and
            line[3] == "gi"
        ):
            raise ValidationError(
                "NCBI prot.accession2taxid file must have "
                "columns: 'accession', 'accession.version' "
                f", 'taxid' and 'gi'. Got {line} instead."
            )

    def _validate_Nth_line(self, line: list, line_no: int):
        # For every filed validate one record
        splitted_line = line.rstrip("\n").split(sep="\t")

        # Raise exception if the entry does not match pattern
        if not re.match(_line_regex, line):
            raise ValidationError(
                f"Non-allowed value found in line {line_no}.\n"
                "Printing line:\n"
                f"{splitted_line}"
            )

    def _validate_(self, level):
        with gzip.open(str(self), 'rt', encoding='utf-8') as file:
            # Flag first line
            is_first_line = True
            line_no = 1

            # Set the maximum time for processing (in seconds)
            max_processing_time = 60

            # Get the current time
            start_time = time.time()

            for line in file:
                # Check time
                if time.time() - start_time >= max_processing_time:
                    break

                # Get line and split it into fields
                splitted_line = line.rstrip("\n").split(sep="\t")

                # Check that it is split in 4
                if len(splitted_line) != 4:
                    raise ValidationError(
                        "NCBI prot.accession2taxid file must have 4 columns, "
                        f"found {len(splitted_line)} columns in line "
                        f"{line_no}. \nPrinting line: \n{splitted_line}"
                    )

                # Parse first line
                if is_first_line:
                    self._validate_1st_line(splitted_line)
                    is_first_line = False
                    line_no += 1

                # Parse Nth line
                else:
                    self._validate_Nth_line(line, line_no)
                    line_no += 1


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
