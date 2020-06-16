#!/usr/bin/python
# encoding: utf-8

from Alfred import Tools
from Notes import Note, Search
from QuerySplitter import QuerySplitter
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

query = Tools.getArgv(1).encode('utf-8')
clipboard = Tools.getEnv('clipboard')
template = Tools.getEnv('template')
paste = Tools.getEnv('paste')

qs = QuerySplitter(query)

if query:
    note = Note(
        content=str() if not paste else clipboard,
        tags=qs.tags,
        template_path=template,
        title=qs.title,
        zettel_id=qs.zettel_id,
    )
    file_path = note.createNote()
    output = Search().getNoteFilename(file_path)

    sys.stdout.write(output)
