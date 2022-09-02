# ----------------------------------------------------------------------------
# Copyright (c) 2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


import shutil

from qiime2.plugin.testing import TestPluginBase
from qiime2 import Artifact


from q2_types_genomics.feature_data import EggnogOutputDirFmt


class TestEggnogOutput(TestPluginBase):
    package='q2_types_genomics.feature_data.tests'

    def test_initial_setup(self):
        # Create directory
        test_output = EggnogOutputDirFmt()

        # trying putting a file in...
        shutil.copy(self.get_data_path("mapped.emapper.annotations"),
                    test_output.path)

        shutil.copy(self.get_data_path("sample_annotations.txt"),
                    test_output.path)
        test_output.save(self.get_data_path("test_output.qza"))
        artifacted = _return_artifact(test_output)

        fh = Artifact.load(artifacted)
        self.assertIn("sample_annotations.txt", fh)


def _return_artifact(fmtd_object):
    return fmtd_object
