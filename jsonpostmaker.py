#!/usr/bin/env python

"""
jsonpostmaker: script to convert files containing html to formatted json
------------------------------------------------------------------------
made it while learning python and deploying a custom blog to gae
too much hassle to create the json myself especially since python cannot
parse json that contains certain special characters
------------------------------------------------------------------------
__author__ = "Abhinav Das"
__copyright__ = "Copyright 2015"
__credits__ = ["Google", "Stackoverflow"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Abhinav Das"
__email__ = "a{at}adas.io"
__status__ = "Production"
"""

import sys
import json

filename = str(sys.argv[1]) 
jsonfilename = filename + ".json"

def write():
    print ("Creating file %s" % jsonfilename)
    try:
        file = open(jsonfilename, 'a')
        file.write("{\n")
        file.write("\t\"posttitle\" : \"%s\"" % filename)
        file.write(",\n")
        file.write("\t\"content\" : \"")
        with open(filename) as fo:
            while True:
                c = fo.read(1)
                if c in ('\"', '/'):
                    file.write("\\%s" % c)
                elif not c:
                    file.write("\"")
                    break
                elif c in ('\n'):
                    file.write("")
                else:
                    file.write("%s" % c)
        file.write("\n}\n")
        file.close()
    except Exception, e:
        print ("Exception occurred. Exiting with status 0. %s " % e)
        sys.exit(0)

write()
