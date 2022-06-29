# ----------------------------------------------------------------------------
# Copyright (c) 2021-2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import re
from ._util import parse_header_line, parse_footer_line

import qiime2.plugin.model as model

from ..plugin_setup import plugin


class EggnogAnnotationFmt(model.TextFileFormat):
    def _check_seperator(self, level):
        with self.open() as fh:
            for i, line in enumerate(fh, 1):
                if not re.search(r'\t', line) and i >= self.header \
                    and i < self.footer:
                    raise ValueError("No correct separator detected in input "
                                     "file on line: {}".format(i))

                #re.split(r'\t', line)
                if i == level:
                    break

    def _validate_(self, level):
        self._check_seperator(level={'min': 5, 'max': None}[level])

    @property
    def header(self):
        try:
            return self._header
        except Exception:
            self._header = parse_header_line(self)
            return self._header

    @header.setter
    def set_header(self):
        self._header = parse_header_line(self)

    @property
    def footer(self):
        try:
            return self._footer
        except Exception:
            self._footer = parse_footer_line(self)
            return self._footer
    @footer.setter
    def set_footer(self):
        self._footer = parse_footer_line(self)




class HeaderlessEggnogAnnotationFmt(EggnogAnnotationFmt):
    pass


plugin.register_formats(EggnogAnnotationFmt)

EggnogAnnotationDirFmt = model.SingleFileDirectoryFormat(
                                 'EggnogAnnotationDirFmt',
                                 'eggnog.tsv',
                                 EggnogAnnotationFmt)

plugin.register_formats(EggnogAnnotationDirFmt)


class OrthologousGroupsFormat(model.TextFileFormat):
    def _check_seperator(self, level):
        with self.open() as fh:
            for i, line in enumerate(fh, 1):
                if not re.search(r'\t', line):
                    raise ValueError("No correct separator detected in input "
                                     "file on line: {}".format(i))

                re.split(r'\t', line)
                if i == level:
                    break

    def _validate_(self, level):
        self._check_seperator(level={'min': 5, 'max': None}[level])
