# AGPL-3.0 License
# Copyright (C) Arthur Milchior  2018 - 2023  <https://github.com/Arthur-Milchior>
# Copyright (C) Shigeyuki 2024 <http://patreon.com/Shigeyuki>
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

import os

# from anki.lang import _
def _(str: str) -> str:
    return str


from .config import getUserOption

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
js_file = os.path.join(__location__, "deckbrowser.js")
css_file = os.path.join(__location__, "defaultcss.css")

with open(js_file, "r") as f:
    js = f.read()
with open(css_file, "r") as f:
    css = f.read()


######################
#header related html #
######################
start_header = """
  <tr style = "vertical-align:text-top">"""

deck_header = f"""
    <th colspan = 5 align = left>
      {_("Deck")}
    </th>"""


def column_header(heading, colpos):
    return f"""
    <th class = "count ui-draggable ui-draggable-handle ui-droppable" colpos = "{colpos}">
      <a onclick = "return pycmd('optsColumn:{colpos}');">
        {_(heading)}
      </a>
    </th>"""


option_header = """
    <th></th>"""

option_name_header = """
    <td></td>"""

end_header = """
  </tr>"""


##############
#deck's html #
##############
def start_line(klass, did):
    return f"""
  <tr class = '{klass}' id = '{did}'>"""


def collapse_children_html(did, name, prefix):
    return f"""
      <a class = collapse onclick = 'return pycmd("collapse:{did}")' id = "{name}" href = "#{name}" >
         {prefix}
      </a>"""


collapse_no_child = """
      <span class = collapse></span>"""


def deck_name(depth, collapse, extraclass, did, cssStyle, name):
    return f"""
    <td class = decktd colspan = 5>
      {"&nbsp;"*6*depth}{collapse}
      <a class = "deck{extraclass}" href="#" onclick = "return pycmd('open:{did}')">
        <font style = '{cssStyle}'>
          {name}
        </font>
      </a>
    </td>
"""


def number_cell(colour, number, description):
    if description is None or description is False:
        description = ""
        t = f"""
    <td align = 'right' class='number_cell'>"""
    else:
        description = f"""
      <span class = 'custom_shige_tooltiptext'>
        {description}
      </span>"""
        t = f"""
    <td align = 'right' class = 'custom_shige_tooltip number_cell'>"""
    # if number:
    t += f"""
      <font color = '{colour}'>
        {number}
      </font>"""
    if description:
        t += f"""
      {description}"""
    t += """
    </td>"""
    return t


def custom_number_cell(number, description):
    if description is None or description is False:
        description = ""
        t = f"""
    <td align = 'right' class='number_cell'>"""
    else:
        description = f"""
      <span class = 'custom_shige_tooltiptext'>
        {description}
      </span>"""
        t = f"""

    <td align = 'right' class = 'custom_shige_tooltip number_cell'>"""
    # if number:
    t += f"""
        {number}"""
    if description:
        t += f"""
      {description}"""
    t += """
    </td>"""
    return t




def gear(did):
    return f"""
    <td align = center class = opts>
      <a onclick = 'return pycmd(\"opts:{int(did)}\");'>
        <img src = '/_anki/imgs/gears.svg' class = gears>
      </a>
    </td>"""


def deck_option_name(option):
    return f"""
    <td>
      {option}
    </td>"""


end_line = """
  </tr>"""


def bar(name, width, left, color, overlay):
    return f"""
          <div class="custom_shige_tooltip bar" style="position:absolute; height:100%; width:{width}%; background-color:{color}; left :{left}% ;">
            <!-- {name}-->
            <span class="custom_shige_tooltiptext">
              {overlay}
            </span>
          </div>"""

# def progress(content):
#     return f"""
#       <div class="progress" style="position:relative;	height:1em;	display:inline-block;	width:100px;		">{content}
#       </div>"""

def progress(content):
    return f"""
      <div class="progress" style="position:relative; height:1em; display:inline-block; width:100px; border-radius:5px; overflow:hidden; " >
        {content}
      </div>
      """
