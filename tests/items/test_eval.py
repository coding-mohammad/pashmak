#
# test_eval.py
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

''' The test '''

from TestCore import TestCore

class test_eval(TestCore):
    ''' The test '''
    def run(self):
        ''' Run test '''
        self.assert_output(
            self.run_without_error(
                ''' mem 'mem "hello from eval"\\; out ^\\;'; eval ^; '''
            ),
            'hello from eval'
        )

        self.assert_output(self.run_without_error('''
            set $code;
            mem 'mem "hello from eval"\\; out ^\\;'; copy $code;
            eval $code;
        '''), 'hello from eval')

        self.assert_has_error(self.run_script(''' eval hfgjhjhg; '''))

        self.assert_has_error(self.run_script(''' eval $not_found; '''), 'VariableError')
