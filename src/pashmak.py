#!/usr/bin/env python3
#
# pashmak.py
#
# the pashmak project
# Copyright 2020 parsa mpsh <parsampsh@gmail.com>
#
# This file is part of pashmak.
#
# pashmak is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pashmak is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pashmak.  If not, see <https://www.gnu.org/licenses/>.
##################################################

''' Pashmak cli entry point '''

import sys
import os
from syntax import parser
from core import program, version

if __name__ == '__main__':
    # validate arguments
    if len(sys.argv) <= 1:
        print(sys.argv[0] + ': script file name is required: pashmak [filename]')
        sys.exit(1)

    if sys.argv[1] == '--info':
        print('Pashmak Version: ' + version.version)
        print('Python Version: ', end='')
        print(sys.version.replace('\n', ''))
        sys.exit(1)

    if sys.argv[1] == '--version' or sys.argv[1] == '-v':
        print(version.version)
        sys.exit(1)

    filename = sys.argv[1]

    if sys.argv[1] == '-':
        script_content = ''
        for line in sys.stdin.readlines():
            script_content += line
    elif not os.path.isfile(filename):
        print(sys.argv[0] + ': file "' + filename + '" not found')
        sys.exit(1)
    else:
        # read content of file and parse it with the parser
        script_f = open(filename, 'r')
        script_content = script_f.read()

    script_operations = parser.parse(script_content)

    # make pashmak program object
    prog = program.Program(args=sys.argv[1:])
    prog.main_filename = filename
    prog.set_operations(script_operations)
    prog.start()
