from .redesign import Redesign
from aqt import mw
from anki.hooks import addHook
from aqt.deckbrowser import DeckBrowser

#addons should selectively load before or after a delay of 666
NM_RESERVED_DELAY = 100

redesign = None

def delayedLoader():
    """
        Delays loading of NM to avoid addon conflicts.
    """
    global redesign
    from .redesign import Redesign
    redesign = Redesign()
    redesign.load()

def onProfileLoaded():
    if not redesign:
        mw.progress.timer(
            NM_RESERVED_DELAY, delayedLoader, False
        )
    else:
        redesign.load()

addHook('profileLoaded', onProfileLoaded)







customFont = "default"; # Set your desired font here.
# Format is "Font Name With Spaces" (i.e. customFont="Times New Roman";)
# Note: If you want to change this, you need to do so in three files: _init_.py, styles.py, and stylers.py




#############################
# WHAT THIS FILE DOES

    # This code example helped me figure out centering one item with text left-justified to it by using a grid layout:
    # https://www.w3schools.com/css/css_grid.asp
    # The following code uses a 3x3 grid where the grid items are numbered 1, 2, 3 horizontally, next row 4, 5, 6 etc. and all of them are empty except for the middle ones. This way the entire grid takes up the whole screen, thereby centering the middle column, while also allowing the title text in grid-item 2 to be left-aligned.
    # This also styles the line of text on Main screen (Decks) at the bottom that says Studied x cards in x minutes
    # customFont is a variable found in styles.py and stylers.py
#############################

DeckBrowser._body = """


    <style>
        html,body,h1,h2,h3,h4,h5,h6 {font-family:""" + customFont + """}
    </style>


    <html>
    <head>
    <style>
    .grid-container {
        margin-left:auto;
        margin-right:auto;
        display: grid;
        grid-template-columns: auto auto auto;
    }
    .grid-item {
        width:auto;
        text-align: left;
    }
    </style>
    </head>
    <body>


    <div class="grid-container">
    <div class="grid-item"></div>
    <center><div class="grid-item" style="width:440px; height:100px; font-size:1.3em;"><h1>Anki</h1></div></center>
    <div class="grid-item"></div>
    <div class="grid-item"></div>
    <center><div class="grid-item" style="width:440px;">
        <table cellspacing=0 cellpading=3>
            %(tree)s
        </table>
    </div></center>
    <div class="grid-item"></div>
    <div class="grid-item"></div>
    <div class="grid-item" style="color:#bdbdbd; text-align:center">
        <br>
        %(stats)s
        %(countwarn)s</div>
    <div class="grid-item"></div>
    </div>


    </body>
    </html>
    """
