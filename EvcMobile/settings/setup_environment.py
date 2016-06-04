import sys
import os
from common.file_utils import FileUtils

with open(FileUtils.get_current_file_path(__file__) + os.path.sep + 'temp.conf', 'w') as temp_conf:
    temp_conf.write("ENV=" + sys.argv[1])