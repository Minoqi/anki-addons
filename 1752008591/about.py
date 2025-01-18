# Copyright © 2017-2018 Joseph Lorimer <joseph@lorimer.me>
#
# This file is part of Chinese Support 3.
#
# Chinese Support 3 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# Chinese Support 3 is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# Chinese Support 3.  If not, see <https://www.gnu.org/licenses/>.

from aqt import mw
from aqt.qt import QDialog, QDialogButtonBox, QLabel, QVBoxLayout

from ._version import __version__


CSR_GITHUB_URL = 'https://github.com/Gustaf-C/anki-chinese-support-3'


def showAbout():
    dialog = QDialog(mw)

    label = QLabel()
    label.setStyleSheet('QLabel { font-size: 14px; }')

    contributors = [
        'Joseph Lorimer',
        'Alex Griffin',
        'Chris Hatch',
        'Joe Minicucci',
        'Roland Sieker',
        'Thomas Tempé',
    ]

    text = '''
<div style="font-weight: bold">Chinese Support 3 v%s</div><br>
<div><span style="font-weight: bold">
    Maintainer</span>: Gustaf Carefall</div>
<div><span style="font-weight: bold">Contributors</span>: %s</div>
<div><span style="font-weight: bold">Website</span>: <a href="%s">%s</a></div>
<div style="font-size: 12px">
    <br>Based on the Chinese Support add-on by Thomas Tempé and many others.
    <br>If your name is missing from here, please open an issue on GitHub.
</div>
''' % (__version__, ', '.join(contributors), CSR_GITHUB_URL, CSR_GITHUB_URL)

    label.setText(text)
    label.setOpenExternalLinks(True)

    buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
    buttonBox.accepted.connect(dialog.accept)

    layout = QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(buttonBox)

    dialog.setLayout(layout)
    dialog.setWindowTitle('About')
    dialog.exec()
