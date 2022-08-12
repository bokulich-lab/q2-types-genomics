# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from q2_types.feature_data import (
    DNAFASTAFormat,
)

from qiime2.plugin import model
from ._util import parse_header_line, parse_footer_line
from qiime2.plugin import ValidationError

from ..plugin_setup import plugin

import re

# mag
MAGSequencesDirFmt = model.SingleFileDirectoryFormat(
    'MAGSequencesDirFmt', r'mag[0-9]+\.(fa|fasta)$', DNAFASTAFormat)

plugin.register_formats(
    MAGSequencesDirFmt
)


# GenericTSVfmt
class ArbitraryHeaderTSVFmt(model.TextFileFormat):
    """This format is for files written as TSVs with arbitrary header and/or
    footer lengths and locations, verification of content should be performed
    using Semantic Validators"""

    def _check_seperator(self, level):
        with self.open() as fh:
            for i, line in enumerate(fh, 1):
                if (not re.search(r'\t', line) and
                        self.header + 1 <= i < self.footer):
                    raise ValidationError("No correct separator detected in"
                                          " input file on line: {}".format(i))

                if i == level:
                    break

    def _validate_(self, level):
        self._check_seperator(level={'min': 5, 'max': None}[level])

    @property
    def header(self):
        return parse_header_line(self)

    @property
    def footer(self):
        return parse_footer_line(self)


class HeaderlessArbitraryHeaderTSVFmt(ArbitraryHeaderTSVFmt):
    pass


plugin.register_formats(ArbitraryHeaderTSVFmt)

ArbitraryHeaderTSVDirFmt = model.SingleFileDirectoryFormat(
                                 'ArbitraryHeaderTSVDirFmt',
                                 'eggnog.tsv',
                                 ArbitraryHeaderTSVFmt)

plugin.register_formats(ArbitraryHeaderTSVDirFmt)


# binary reference
class BinaryReferenceDBFmt(model.BinaryFileFormat):
    """A format to hold reference data, originally created for the diamond
    formatted reference database information needed for Eggnog Mapper"""

    def _validate_(self, level):
        bad_lines = []
        try:
            contents = self.open().readlines()
            for line, content in enumerate(contents, 1):
                if not isinstance(content, bytes):
                    bad_lines.append(line)
            if bad_lines:
                raise ValueError
        except ValueError:
            raise ValueError("Your reference database appears to contain"
                             " non-byte strings on lines: {}".format(
                                 ", ".join(bad_lines)))
        except Exception as e:
            raise e


BinaryReferenceDBDirFmt = model.SingleFileDirectoryFormat(
        'BinaryReferenceDBDirFmt', 'reference_database',
        BinaryReferenceDBFmt)

plugin.register_formats(
    BinaryReferenceDBFmt, BinaryReferenceDBDirFmt
    )
