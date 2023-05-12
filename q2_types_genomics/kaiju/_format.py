# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
from qiime2.core.exceptions import ValidationError
from qiime2.plugin import model

from ..plugin_setup import plugin


class KaijuIndexFormat(model.BinaryFileFormat):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _validate_(self, level):
        pass


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
                        "taxonomy ID in the first two columns, found non-numeric "
                        f"value on line {i + 1}."
                    )
                for col in (5, 7, 9, 10, 11):
                    if not line[col].isnumeric() or not int(line[col]) in (0, 1):
                        raise ValidationError(
                            "NCBI taxonomy nodes file must contain 0 or 1 in columns "
                            "6, 8, 10, 11, and 12, found a non-allowed value on line "
                            f"{i + 1}, column {col + 1}: {line[col]}."
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


class KaijuDBDirectoryFormat(model.DirectoryFormat):
    nodes = model.File(r"nodes.dmp", format=NCBITaxonomyNodesFormat)
    names = model.File(r"names.dmp", format=NCBITaxonomyNamesFormat)
    index = model.File(r"kaiju_db.+\.fmi", format=KaijuIndexFormat)


plugin.register_formats(
    KaijuDBDirectoryFormat, NCBITaxonomyNodesFormat, NCBITaxonomyNamesFormat
)
