#!/usr/bin/env python
import libxml2, sys, re

"""kmlTrack2LineString.py - converts kml gx:Track to old style LineString elements. This is required because not even gpsbabel can convert the gx:Track elements to gpx for instance resulting in data loss. Conversion is done in place.
Example - kmlTrack2LineString.py file.kml"""

fileName = sys.argv[1]
doc = libxml2.parseFile(fileName)
ctxt = doc.xpathNewContext()
ctxt.xpathRegisterNs('kml', "http://www.opengis.net/kml/2.2")
ctxt.xpathRegisterNs('gx', "http://www.google.com/kml/ext/2.2")

nameNode = None

res = ctxt.xpathEval("//kml:Placemark/gx:Track")
if len(res) == 0:
    print 'Not found'
else:
    for p in res:
        ctxt.setContextNode(p)
        f = ctxt.xpathEval("../kml:name/text()")
        name = f[0]
        print 'Found:', name
        
        lineStringCoords = []
        coords = ctxt.xpathEval("gx:coord/text()")
        for c in coords:
            lineStringCoords.append(','.join(str(c).split(' ')))

        lineStringCoords = ' '.join(lineStringCoords)

        lsNode = libxml2.newNode('LineString')
        p.parent.addChild(lsNode)
        tNode = libxml2.newNode('tessellate')
        tNode.setContent('1')
        lsNode.addChild(tNode)
        cNode = libxml2.newNode('coordinates')
        cNode.setContent(lineStringCoords)
        lsNode.addChild(cNode)

        p.unlinkNode()
        #print lineStringCoords
        #p.setContent(str(name))

doc.saveFile(fileName)    
doc.freeDoc()
ctxt.xpathFreeContext()


