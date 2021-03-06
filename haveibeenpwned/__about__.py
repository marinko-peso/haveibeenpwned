# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import datetime


__all__ = [
    '__title__',
    '__summary__',
    '__keywords__',
    '__url__',
    '__version__',
    '__author__',
    '__email__',
    '__license__',
    '__copyright__',
]

__version__ = '0.0.6'
__title__ = 'haveibeenpwned'
__summary__ = 'PyPi quick status implementation for the awesome haveibeenpwned.com service'
__keywords__ = 'haveibeenpwned email breached status security'
__url__ = 'https://github.com/marinko-peso/haveibeenpwned/'
__author__ = 'Marinko Peso'
__email__ = 'marinko.peso@gmail.com'
__license__ = 'MIT'

now = datetime.datetime.now()
__copyright__ = '%s %s' % (now.year, __author__)
