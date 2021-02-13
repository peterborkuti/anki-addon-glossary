# export_html_glossary Anki add-on
# based on export_to_html Anki add-on
# Author Peter Borkuti

# Exports a desk to a two-column html file. The first column is the answer, the second
# column is the question.
# It is good for creating a glossary based on an Anki deck.

# The output html file must be placed in the Anki's user media folder.
# If the style must be changed, create a custom.css file in the media folder.

from anki.lang import _
from anki.hooks import addHook
from anki.exporting import TextCardExporter
from aqt.utils import getText
from aqt.utils import showInfo
from anki.cards import Card
from anki.utils import  ids2str, splitFields
import re
import sys
import os
import time
import random
import string

ext = ".htm"

hideTags = True

htmlBefore="""
<!DOCTYPE html>
<head>
<meta charset="UTF-8">
<title>Untitled Document</title>
<style type="text/css">

img {
    max-height: 400px;
    max-width: 400px;
    display: compact;
    margin: 0px;
    padding: 1px;
    top:0;
    left:0;
}
</style>
</head>
<body>
"""

htmlAfter="""
</body>
</html>
"""

directory = "/home/srghma/anki-addon-kanji-output"

def convertSound(s):
    return re.sub(r'\[sound:(.*)]', r'<audio controls src="\1"></audio>', s, 0, re.IGNORECASE)

def getRandomId(group):
    # https://pythontips.com/2013/07/28/generating-a-random-string/
    return ' id="' + ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])+'"'

def escapeText(text):
    "Escape newlines, tabs and CSS and change id to class"
    text = text.replace("\n", "")
    text = text.replace("\t", "")
    text = re.sub("(?i)<style>.*?</style>", "", text)
    text = text.replace("<hr id=answer>", '<hr class="answer">')

    return text

class MyTextCardExporter(TextCardExporter):
    key = _("Export deck as My Html Glossary")

    def __init__(self, col):
        TextCardExporter.__init__(self, col)

    def doExport(self, file):
        def myEscapeText(s):
            # strip off the repeated question in answer if exists
            s = re.sub('(?si)^.*<hr id=answer>\n*', "", s)
            s = re.sub("(?si)<style.*?>.*?</style>", "", s)
            s = re.sub('<img src="(.*?)"', r'<img src="/Internal storage/AnkiDroid/collection.media/\1"', s)

            return convertSound(escapeText(s))

        cardIds = self.cardIds()

        for cardId in cardIds:
            card = self.col.getCard(cardId)

            template = card.template()["name"]

            if template != 'from jp':
                continue

            kanji = card.note()["kanji"]

            print(kanji)

            # only one
            out = (htmlBefore +
                "\n" + myEscapeText(card.answer()) + "\n" +
                htmlAfter)

            if not os.path.exists(directory):
                os.makedirs(directory)

            with open(directory + '/' + kanji + '.html', 'w') as myfile:
                myfile.write(out)

            # file.write("dummy".encode("utf-8"))

def addMyExporter(exps):
    def theid(obj):
        return ("%s (*%s)" % (obj.key, obj.ext), obj)
    exps.append(theid(MyTextCardExporter))

addHook("exportersList", addMyExporter)
