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


class EggnogBase(model.TextFileFormat):

    def _check_seperator(self, level):
        try:
            with self.open() as fh:
                for i, line in enumerate(fh, 1):
                    re.split(r'\t', line)
                    if i == level:
                        break

        except:
            raise ValueError("Incorrect separator in file")

    def _validate_(self, level):
        self._check_seperator(level={'min': 5, 'max': None}[level])

class EggnogFmt(EggnogBase):
    pass

class HeaderlessEggnogFmt(EggnogBase):
    pass

EggnogDirFmt = model.SingleFileDirectoryFormat('EggnogDirFmt',
                                               'eggnog.tsv',
                                               EggnogFmt)

plugin.register_formats(EggnogFmt, EggnogDirFmt)
