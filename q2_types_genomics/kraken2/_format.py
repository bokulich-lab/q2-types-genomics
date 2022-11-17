import pandas as pd
from qiime2.core.exceptions import ValidationError
from qiime2.plugin import model

from ..plugin_setup import plugin


class Kraken2ReportFormat(model.TextFileFormat):
    """
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _validate_(self, level):
        level_map = {'min': 100, 'max': float('inf')}
        max_lines = level_map[level]

        try:
            df = pd.read_csv(self.path, sep='\t')
            print(df)
        except:
            ...


plugin.register_formats(
    Kraken2ReportFormat
)
