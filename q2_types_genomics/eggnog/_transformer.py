from ..plugin_setup import plugin
from ._format import EggnogAnnotationFmt
import pandas as pd


def _annotation_formats_to_dataframe(ff):
    df = pd.read_csv(str(ff), sep='\t', header=4)
    return df

@plugin.register_transformer
def _1(data: EggnogAnnotationFmt) -> pd.DataFrame:
    return _annotation_formats_to_dataframe(data)
