# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import re

import qiime2.plugin.model as model

#from qiime2.core.exceptions import ValidationError

from ..plugin_setup import plugin


class FunctionalAnnotationFmt(model.TextFileFormat):

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

class HeaderlessFunctionaAnnotationFmt(FunctionalAnnotationFmt):
    pass

plugin.register_formats(FunctionalAnnotationFmt)

FunctionalAnnotationDirFmt = model.SingleFileDirectoryFormat(
                                 'FunctionalAnnotationDirFmt',
                                 'eggnog.tsv',
                                 FunctionalAnnotationFmt)

plugin.register_formats(FunctionalAnnotationDirFmt)

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
