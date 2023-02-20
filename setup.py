# ----------------------------------------------------------------------------
# Copyright (c) 2023, QIIME 2 development team.
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
             'data/mags/*/*', 'data/mags/*/*/*',
             'data/manifests/*', 'data/good_contigs/*',
             'data/bad_char_contigs/*', 'data/bad_name_contigs/*',
             'data/diamond_hit/*',
             'data/bowtie/*/*', 'data/bowtie/*/*/*/*', 'data/bowtie/*/*/*'],
        'q2_types_genomics.feature_data.tests':
            ['data/*', 'data/*/*',
             'data/mags-fa/*', 'data/mags-fasta/*'],
        'q2_types_genomics.genome_data.tests':
            ['data/*/', 'data/genes/*', 'data/loci/*',
             'data/loci-invalid/*', 'data/proteins/*',
             'data/ortholog/*',
             ],
        'q2_types_genomics.kraken2.tests':
            ['data/*', 'data/db/*',
             'data/outputs-single/*', 'data/outputs-reads/*/*',
             'data/outputs-mags/*/*', 'data/reports-single/*',
             'data/reports-reads/*/*', 'data/reports-mags/*/*'],
        'q2_types_genomics.reference_db.tests':
            ['data/*', 'data/*/*',
             ],
    },
    zip_safe=False,
)
