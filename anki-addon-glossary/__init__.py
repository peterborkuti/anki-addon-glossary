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
import json

ext = ".htm"

hideTags = True

directory = "/home/srghma/.local/share/Anki2/User 1/collection.media/anki-addon-glossary"

def convertSound(s):
    return re.sub(r'\[sound:(.*)]', r'<audio controls src="\1"></audio>', s, 0, re.IGNORECASE)

def getRandomId(group):
    # https://pythontips.com/2013/07/28/generating-a-random-string/
    return ' id="' + ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])+'"'

def escapeText(text):
    "Escape newlines, tabs and CSS and change id to class"
    text = text.replace("\n", "")
    text = text.replace("\t", "")
    text = text.replace("<hr id=answer>", '<hr class="answer">')

    return text

class MyTextCardExporter(TextCardExporter):
    key = _("Export deck as My Html Glossary")

    def __init__(self, col):
        TextCardExporter.__init__(self, col)

    def doExport(self, file):
        def myEscapeText(s):
            s = re.sub('(?si)^.*<hr id=answer>\n*', "", s)
            s = re.sub("(?si)<style.*?>.*?</style>", "", s)

            return convertSound(escapeText(s))

        cardIds = self.cardIds()

        for cardId in cardIds:
            card = self.col.getCard(cardId)

            template = card.template()
            template_name = template["name"]

            if template_name != 'from jp':
                continue

            kanji = card.note()["kanji"]

            if not os.path.exists(directory):
                os.makedirs(directory)

            # card.css()

            with open(directory + '/' + kanji + '.mynonjsonext', 'w') as myfile:
                data = { 'answer': card.answer() }
                json.dump(data, myfile)

            # file.write("dummy".encode("utf-8"))

def addMyExporter(exps):
    def theid(obj):
        return ("%s (*%s)" % (obj.key, obj.ext), obj)
    exps.append(theid(MyTextCardExporter))

addHook("exportersList", addMyExporter)
