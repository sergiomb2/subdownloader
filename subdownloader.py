#!/usr/bin/env python3
# Copyright (c) 2017 SubDownloader Developers - See COPYING - GPLv3
# PYTHON_ARGCOMPLETE_OK

import os
import sys

from subdownloader.client.logger import logging_file_install, logging_install
from subdownloader.client.internationalization import i18n_install
from subdownloader.client.arguments import parse_arguments

sys.path.append(os.path.join(sys.path[0], 'modules'))

logging_file_install(None)
i18n_install()
options = parse_arguments()
logging_install(options.loglevel, options.logfile)

if options.mode == 'gui':
    import subdownloader.client.gui
    return_code = subdownloader.client.gui.run(options)
    sys.exit(return_code)
elif options.mode == 'cli':
    import subdownloader.client.cli.main
    cli = subdownloader.client.cli.main.Main(options)
    cli.start_session()
