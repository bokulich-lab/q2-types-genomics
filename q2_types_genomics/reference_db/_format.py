# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
import re
from qiime2.plugin import model
from qiime2.core.exceptions import ValidationError
from q2_types_genomics.plugin_setup import plugin
from q2_types_genomics.reference_db._type import (
    ReferenceDB, Eggnog, Diamond, EggnogSequenceTaxa
)
from q2_types.feature_data import MixedCaseProteinFASTAFormat


class EggnogRefTextFileFmt(model.TextFileFormat):
    _expected_columns = [
            '# Taxid',
            'Sci.Name',
            'Rank',
            'Named Lineage',
            'Taxid Lineage'
    ]
    _line_pattern = re.compile(
        r'^\d+\t'  # Taxid
        r'([^\t]*\t)'  # Sci.Name
        r'(no rank|species|subspecies)\t'  # Rank
        r'([^\t]*\t)'  # Named Lineage
        r'\d+(,\d+)*$'  # 'Taxid Lineage'
    )

    def _validate_1st_line(self, line):
        fields = line.strip("\n").split("\t")
        if len(fields) > 5:
            raise ValidationError(
                "Too many columns.\n"
                "Expected columns:\n"
                f"{self._expected_columns}\n"
                "Columns given:\n"
                f"{fields}"
            )

        if not (
            fields[0] == '# Taxid' and
            fields[1] == 'Sci.Name' and
            fields[2] == 'Rank' and
            fields[3] == 'Named Lineage' and
            fields[4] == 'Taxid Lineage'
        ):
            raise ValidationError(
                "Wrong columns.\n"
                "Expected columns:\n"
                f"{self._expected_columns}\n"
                "Columns given:\n"
                f"{fields}"
            )

    def _validate_Nth_line(self, line, line_no):
        if not self._line_pattern.match(line):
            raise ValidationError(
                f"Invalid line at line {line_no}:\n"
                f"{line}"
            )

    def _validate_(self, level):
        with open(str(self), "r") as file:
            line_no = 0
            is_fist_line = True

            for line in file:
                # Validate first line
                if is_fist_line:
                    self._validate_1st_line(line)
                    line_no += 1
                    is_fist_line = False

                # Validate N'th line
                else:
                    self._validate_Nth_line(line, line_no)
                    line_no += 1


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


class EggnogProteinSequencesDirFmt(model.DirectoryFormat):
    taxid_info = model.File("e5.taxid_info.tsv", format=EggnogRefTextFileFmt)
    proteins = model.File(
        "e5.proteomes.faa", format=MixedCaseProteinFASTAFormat
    )


plugin.register_formats(EggnogProteinSequencesDirFmt)
plugin.register_semantic_type_to_format(ReferenceDB[EggnogSequenceTaxa],
                                        EggnogProteinSequencesDirFmt)
