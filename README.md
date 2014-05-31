py-gps-tools
============

A set of python scripts to manipulate GPS data

##kmlCleanTimeStamp.py 

Removes TimeStamp information from .kml files. More precisely, it removes gx:TimeStamp and //kml:Placemark/kml:TimeStamp elements. Modifies the document in place. 

> kmlCleanTimeStamp.py file.kml

##kmlTrack2LineString.py 
Converts kml gx:Track to old style LineString elements. This is required because 
not even gpsbabel can convert the gx:Track elements to gpx for instance resulting in data loss. Conversion is done in place.

> kmlTrack2LineString.py file.kml