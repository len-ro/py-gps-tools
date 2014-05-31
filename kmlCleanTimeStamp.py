#!/usr/bin/env python

import libxml2, sys, re

"""kmlCleanTimeStamp.py - removes TimeStamp information from .kml files. More precisely, it removes gx:TimeStamp and //kml:Placemark/kml:TimeStamp elements. Modifies the document in place. 
Example - kmlCleanTimeStamp.py file.kml
"""

fileName = sys.argv[1]
doc = libxml2.parseFile(fileName)
ctxt = doc.xpathNewContext()
ctxt.xpathRegisterNs('kml', "http://www.opengis.net/kml/2.2")
ctxt.xpathRegisterNs('gx', "http://www.google.com/kml/ext/2.2")

nameNode = None

clean = ["//kml:Placemark/kml:TimeStamp", "//gx:TimeStamp"]

for c in clean:
    res = ctxt.xpathEval(c)
    if len(res) == 0:
        print 'Not found: ', c
    else:
        for p in res:
            p.unlinkNode()

doc.saveFile(fileName)    
doc.freeDoc()
ctxt.xpathFreeContext()


