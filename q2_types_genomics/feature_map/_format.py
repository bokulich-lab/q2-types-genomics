# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
import json
from uuid import UUID

from qiime2.core.exceptions import ValidationError
from qiime2.plugin import model

from ..plugin_setup import plugin


class MAGtoContigsFormat(model.TextFileFormat):
    def _validate_(self, level):
        with self.path.open("r") as fh:
            data = json.load(fh)

            level_map = {"min": 1, "max": len(data)}
            max_lines = level_map[level]

            # assert keys are proper UUIDs and dict values are lists
            for _id, contigs in list(data.items())[:max_lines]:
                try:
                    UUID(_id, version=4)
                except ValueError:
                    raise ValidationError(
                        "MAG IDs must be valid UUID version 4 sequences. "
                        f'Found "{_id}", which is invalid.'
                    )

                if not isinstance(contigs, list):
                    raise ValidationError(
                        "Values corresponding to MAG IDs must be lists of "
                        f'contigs. Found "{contigs}" for MAG "{_id}".'
                    )


MAGtoContigsDirFmt = model.SingleFileDirectoryFormat(
    "MAGtoContigsDirFmt", "mag-to-contigs.json", MAGtoContigsFormat
)

plugin.register_formats(MAGtoContigsFormat, MAGtoContigsDirFmt)
