# ----------------------------------------------------------------------------
# Copyright (c) 2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages

import versioneer

setup(
    name="q2-types-genomics",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    author="Michal Ziemski",
    author_email="ziemski.michal@gmail.com",
    description="QIIME 2 semantic types for genomics applications.",
    license='BSD-3-Clause',
    url="https://github.com/bokulich-lab/q2-types-genomics",
    entry_points={
        'qiime2.plugins':
        ['q2-types-genomics=q2_types_genomics.plugin_setup:plugin']
    },
    package_data={
        'q2_types_genomics': ['citations.bib'],
        'q2_types_genomics.tests': ['data/*'],
        'q2_types_genomics.per_sample_data.tests':
            ['data/*',
             'data/mags/mags-fa/sample1/*', 'data/mags/mags-fa/sample2/*',
             'data/mags/mags-fasta/sample1/*',
             'data/mags/mags-fasta/sample2/*',
             'data/mags/mags-unorganized/*',
             'data/manifests/*',
             'data/bowtie/unorganized/*',
             'data/bowtie/valid/sample1/mag1/*',
             'data/bowtie/valid/sample2/mag1/*'],
        'q2_types_genomics.feature_data':
            ['data/*', 'data/mags-fa/*', 'data/mags-fasta/*']
    },
    zip_safe=False,
)
