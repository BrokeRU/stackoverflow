"""https://stackoverflow.com/a/53296949/10650942"""

import os
from datetime import datetime

SRC_PATH = './src'
DST_PATH = './dst'

for dirpath, _, filenames in os.walk(SRC_PATH):
    for filename in filenames:
        src_filepath = os.path.join(dirpath, filename)
        last_edit = datetime.fromtimestamp(os.path.getmtime(src_filepath))

        dst_dirpath = os.path.join(DST_PATH, str(last_edit.year), str(last_edit.month), str(last_edit.day))
        dst_filepath = os.path.join(dst_dirpath, filename)

        os.makedirs(dst_dirpath, exist_ok=True)
        os.rename(src_filepath, dst_filepath)

        print(src_filepath, '->', dst_filepath)
