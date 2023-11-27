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
    license="BSD-3-Clause",
    url="https://github.com/bokulich-lab/q2-types-genomics",
    entry_points={
        "qiime2.plugins": [
            "q2-types-genomics=q2_types_genomics.plugin_setup:plugin"
        ]
    },
    package_data={
        'q2_types_genomics': ['citations.bib'],
        'q2_types_genomics.tests': ['data/*'],
        'q2_types_genomics.per_sample_data.tests':
            ['data/*',
             'data/mags/*/*', 'data/mags/*/*/*',
             'data/manifests/*', 'data/contigs/*',
             'data/diamond_hit/*',
             'data/bowtie/*/*', 'data/bowtie/*/*/*/*', 'data/bowtie/*/*/*'],
        'q2_types_genomics.feature_data.tests':
            ['data/*', 'data/*/*',
             'data/mags-fa/*', 'data/mags-fasta/*'],
        'q2_types_genomics.genome_data.tests':
            ['data/*/', 'data/genes-with-prefix/*',
             'data/genes-with-suffix/*', 'data/genes-with-wrong-prefix/*',
             'data/loci-invalid/*',  'data/loci-with-prefix/*',
             'data/loci-with-suffix/*', 'data/loci-with-wrong-prefix/*',
             'data/ortholog/*', 'data/proteins-with-suffix/*',
             'data/proteins-with-prefix/*',
             'data/proteins-with-wrong-prefix/*',
             ],
        'q2_types_genomics.kraken2.tests': [
            'data/*',
            'data/kraken2-db/*',
            'data/bracken-db/*',
            'data/outputs-single/*',
            'data/outputs-reads/*/*',
            'data/outputs-contigs/*',
            'data/outputs-mags/*/*',
            'data/reports-single/*',
            'data/reports-reads/*/*',
            'data/reports-mags/*/*',
            'data/db-reports/**/*'
        ],
        'q2_types_genomics.kaiju.tests':
            ['data/*', 'data/db-valid/*'],
        'q2_types_genomics.reference_db.tests':
            ['data/*', 'data/*/*', ],
    },
    zip_safe=False,
)
