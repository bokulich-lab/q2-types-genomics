# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import importlib

import qiime2.plugin

from q2_types_genomics import __version__

citations = qiime2.plugin.Citations.load(
    'citations.bib', package='q2_types_genomics')
plugin = qiime2.plugin.Plugin(
    name='types-genomics',
    version=__version__,
    website='https://github.com/bokulich-lab/q2-types-genomics',
    package='q2_types_genomics',
    description=('This QIIME 2 plugin defines semantic types and '
                 'transformers required for analysis of genomics'
                 'datasets.'),
    short_description=('Plugin defining types for analysis of '
                       'genomics datasets.')
)

importlib.import_module('q2_types_genomics.feature_data')
importlib.import_module('q2_types_genomics.per_sample_data')
importlib.import_module('q2_types_genomics.genome_data')
importlib.import_module('q2_types_genomics.eggnog')
