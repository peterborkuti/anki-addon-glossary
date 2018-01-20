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
from anki.utils import  ids2str
import re
import sys,os
import time

class MyTextCardExporter(TextCardExporter):

    key = _("Export deck as Html Glossary")
    ext = ".htm"
    hideTags = True
    htmlBefore="""
<!DOCTYPE html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Untitled Document</title>
<style type="text/css">

.Question{
    float: right;
    height: auto;
    width: 40%;
}
.Answer{
    float: right;
    height: auto;
    width: 40%;
}

.Answer,.Question{
    overflow: auto;
    padding:4px;
    position: relative;
    visibility: visible;
    height: auto;
}
.Card {
    min-width:25px;
    text-align: center;
    clear:both;
    height: auto;
    width: 100%;
    overflow: visible;
    border-top-width: thin;
    border-right-width: thin;
    border-bottom-width: thin;
    border-left-width: thin;
    border-top-style: solid;
    border-right-style: solid;
    border-bottom-style: solid;
    border-left-style: solid;
    display: block;
}

.Card:after {
    content: '.';
    display: block;
    clear: both;
    visibility: hidden;
    height: 0;
    line-height: 0;
}
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
<link type="text/css" rel="stylesheet" href="custom.css"/>
</head>
<body>

"""
    htmlAfter="""
</body>
</html>
"""
    def __init__(self, col):
        TextCardExporter.__init__(self, col)

    def escapeText(self, text):
        "Escape newlines, tabs and CSS and change id to class"
        text = text.replace("\n", "")
        text = text.replace("\t", "")
        text = re.sub("(?i)<style>.*?</style>", "", text)
        text = text.replace("<hr id=answer>", '<hr class="answer">')

        return text


    def doExport(self, file):
        ids = self.cardIds()

        def esc(s):
            # strip off the repeated question in answer if exists
            s = re.sub('(?si)^.*<hr id=answer>\n*', "", s)
            s = re.sub("(?si)<style.*?>.*?</style>", "", s)

            return self.escapeText(s)

        def convertSound(s):

            return re.sub(r'\[sound:(.*)]', r'<audio controls src="\1"></audio>', s, 0, re.IGNORECASE)

        out = ""

        for cid in ids:
            c = self.col.getCard(cid)

            out += '<div class="Card">\n'
            out += '<div class="Question">\n' + convertSound(esc(c.q())) + "\n</div>\n"
            out += '<div class="Answer">\n' + convertSound(esc(c.a())) + "\n</div>\n"
            out += "</div><!-- Card -->\n\n"

        out= self.htmlBefore + out + self.htmlAfter
        file.write(out.encode("utf-8"))

def addMyExporter(exps):
    def theid(obj):
        return ("%s (*%s)" % (obj.key, obj.ext), obj)
    exps.append(theid(MyTextCardExporter))

addHook("exportersList", addMyExporter)
