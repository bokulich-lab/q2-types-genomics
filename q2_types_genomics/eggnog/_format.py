# ----------------------------------------------------------------------------
# Copyright (c) 2021-2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import re

import qiime2.plugin.model as model

from ..plugin_setup import plugin


class EggnogAnnotationFmt(model.TextFileFormat):
    #def __init__(self, mode=None, header='infer'):
    #    self._mode=mode
    #    self.header=header
    #    #super().__init__(mode=self._mode)

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
        pass
        #self._check_seperator(level={'min': 5, 'max': None}[level])


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
