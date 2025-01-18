import os
from datetime import datetime


# 現在のﾃﾞｨﾚｸﾄﾘを取得
current_directory = os.getcwd()

ORIGINAL_AUTHOR = "Arthur Milchior  2018 - 2023  <https://github.com/Arthur-Milchior>"

current_year_text = str(datetime.now().year)

SHIGEYUKI = f"Shigeyuki {current_year_text} <http://patreon.com/Shigeyuki>"

# AGPL3のｺﾋﾟｰﾗｲﾄﾍｯﾀﾞｰ
copyright_header = f"""# AGPL-3.0 License
# Copyright (C) {ORIGINAL_AUTHOR}
# Copyright (C) {SHIGEYUKI}
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
\n\n"""

print(copyright_header)

# 除外ﾌｫﾙﾀﾞ
excluded_folders = [ 'custom_by_shige', ]

# 除外ﾌｧｲﾙ
excluded_files = ['zzz_add_copyright.py', 'zzz_makeAnkiAddonFile.py']


# Qt Designerを除外
qt_designer_identifiers = [
    "Form implementation generated from reading ui file",
    "Created by: PyQt5 UI code generator",
    "Created by: PyQt6 UI code generator"
]

# 現在のﾃﾞｨﾚｸﾄﾘ内の`.py`ﾌｧｲﾙのﾘｽﾄを取得
for root, dirs, files in os.walk(current_directory, topdown=True):
    dirs[:] = [d for d in dirs if d not in excluded_folders]  # 特定のﾌｫﾙﾀﾞを除外
    for file in files:
        if file.endswith('.py') and file not in excluded_files:  # `.py`で終わるﾌｧｲﾙかつ除外ﾌｧｲﾙに含まれていない
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # Qt Designerによって生成されたﾌｧｲﾙかどうかを確認
                if not any(identifier in content for identifier in qt_designer_identifiers):
                    # ｺﾋﾟｰﾗｲﾄﾍｯﾀﾞｰが既に含まれているか確認
                    if copyright_header not in content:
                        # ﾍｯﾀﾞｰをﾌｧｲﾙの先頭に追加
                        print(file_path)
                        # 🟢ｺﾒﾝﾄを解除
                        with open(file_path, 'w', encoding='utf-8') as f_write:
                            f_write.write(copyright_header + content)