# ----------------------------------------------------------------------------
# Copyright (c) 2021-2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


transferded_annotation_field_names = """Preferred_name
GOs
EC
KEGG_ko
KEGG_Pathway
KEGG_Module
KEGG_Reaction
KEGG_rclass
BRITE
KEGG_TC
CAZy
BiGG_Reaction
PFAMs
md5"""


transferred_annotation_fields = transferded_annotation_field_names.split("\n")


def parse_header_line(filepath, comment_char='#'):
    cnt = 0
    with filepath.open() as fh:
        while True:
            line = fh.readline()
            if line.startswith(comment_char):
                cnt += 1
            else:
                break

    return cnt - 1


def parse_footer_line(filepath, comment_char='#'):
    cnt = 0
    past_header = False
    with filepath.open() as fh:
        while True:
            line = fh.readline()
            cnt += 1
            if not past_header and not line.startswith(comment_char):
                print(line)
                past_header = True
            elif past_header and line.startswith(comment_char):
                return cnt
            else:
                continue
