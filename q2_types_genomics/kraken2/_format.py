# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import pandas as pd
from pandas.core.dtypes.common import is_string_dtype
from qiime2.core.exceptions import ValidationError
from qiime2.plugin import model

from ..per_sample_data._format import MultiDirValidationMixin
from ..plugin_setup import plugin


class Kraken2ReportFormat(model.TextFileFormat):
    COLUMNS = {
        'perc_frags_covered': float, 'no_frags_covered': int,
        'no_frags_assigned': int, 'rank': str, 'ncbi_tax_id': int,
        'name': str
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _validate_(self, level):
        df = pd.read_csv(self.path, sep='\t', header=None)
        try:
            df.columns = self.COLUMNS.keys()
        except ValueError as e:
            if 'Length mismatch' in str(e):
                raise ValidationError(
                    f'Expected 6 columns in the Kraken2 report file but '
                    f'{df.shape[1]} were found.'
                )
            else:
                raise ValidationError(
                    'An error occurred when reading in the '
                    'Kraken2 report file'
                ) from e
        for col, dtype in self.COLUMNS.items():
            if dtype == str and is_string_dtype(df[col]):
                continue
            if df[col].dtype == dtype:
                continue
            raise ValidationError(
                f'Expected {dtype} type in the "{col}" column, '
                f'got {df[col].dtype}'
            )


class Kraken2ReportDirectoryFormat(MultiDirValidationMixin,
                                   model.DirectoryFormat):
    reports = model.FileCollection(
        r'.+report\.(txt|tsv)$', format=Kraken2ReportFormat
    )

    @reports.set_path_maker
    def reports_path_maker(self, sample_id, mag_id=None):
        prefix = f'{sample_id}/{mag_id}_' if mag_id else f'{sample_id}/'
        return f'{prefix}report.txt'


class Kraken2OutputFormat(model.TextFileFormat):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _validate_(self, level):
        df = pd.read_csv(self.path, sep='\t', header=None)
        if df.shape[1] != 5:
            raise ValidationError(
                f'Expected 5 columns in the Kraken2 output file but '
                f'{df.shape[1]} were found.'
            )
        if not set(df.iloc[:, 0].unique()).issubset({'C', 'U'}):
            raise ValidationError(
                'Expected the first column to contain only "C" or "U" values.'
            )


class Kraken2OutputDirectoryFormat(MultiDirValidationMixin,
                                   model.DirectoryFormat):
    reports = model.FileCollection(
        r'.+output\.(txt|tsv)$', format=Kraken2OutputFormat
    )

    @reports.set_path_maker
    def reports_path_maker(self, sample_id, mag_id=None):
        prefix = f'{sample_id}/{mag_id}_' if mag_id else f'{sample_id}/'
        return f'{prefix}output.txt'


class Kraken2DBFormat(model.TextFileFormat):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _validate_(self, level):
        pass


class Kraken2DBDirectoryFormat(model.DirectoryFormat):
    hash = model.File(r'hash.k2d', format=Kraken2DBFormat)
    opts = model.File(r'opts.k2d', format=Kraken2DBFormat)
    taxo = model.File(r'taxo.k2d', format=Kraken2DBFormat)


class BrackenDBFormat(model.TextFileFormat):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _validate_(self, level):
        pass


class BrackenDBDirectoryFormat(model.DirectoryFormat):
    kmers = model.FileCollection(r'.+\.kmer_distrib', format=BrackenDBFormat)

    @kmers.set_path_maker
    def reports_path_maker(self, read_len):
        return f'database{read_len}.kmer_distrib'


plugin.register_formats(
    Kraken2ReportDirectoryFormat, Kraken2OutputDirectoryFormat,
    Kraken2DBDirectoryFormat, BrackenDBDirectoryFormat
)
