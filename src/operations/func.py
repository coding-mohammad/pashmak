#
# func.py
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

''' Starts function block '''

from syntax import parser

def run(self, op: dict):
    ''' Starts function block '''

    self.require_one_argument(op, 'func operation requires function name argument')
    arg = op['args'][0]

    # check function already declared
    try:
        self.functions[self.current_namespace() + arg]
        self.raise_error(
            'FunctionError',
            'function "' + self.current_namespace() + arg + '" already declared',
            op
        )
    except KeyError:
        pass

    # declare function
    self.current_func = self.current_namespace() + arg
    self.functions[self.current_func] = []

    # check for argument variable
    if len(op['args']) > 1:
        arg_var = op['args'][1].strip(')').strip('(')
        self.arg_should_be_variable(arg_var, op)
        self.functions[self.current_func].append(parser.parse(arg_var + ' = ^')[0])
