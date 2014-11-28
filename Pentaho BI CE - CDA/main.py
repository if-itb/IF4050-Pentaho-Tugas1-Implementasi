#!/usr/bin/env python

import constants
import json
import sys
import urllib2

def getCDAList():
    path = constants.HOST + '/' + constants.CDA_ENDPOINT
    path = path + '/' + constants.CDA_GETCDALIST
    
    # Authentication
    p = urllib2.HTTPPasswordMgrWithDefaultRealm()
    p.add_password(None, path, constants.USERNAME, constants.PASSWORD)
    handler = urllib2.HTTPBasicAuthHandler(p)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)
    
    # Retrieve JSON
    results = json.load(urllib2.urlopen(path))
    for result in results['resultset']:
        print 'Filename:', result[0], 'FilePath:', result[1] 

def main(argv=None):
    if argv is None:
        argv = sys.argv
    getCDAList() # get CDA List from Pentaho

        
if __name__ == "__main__":
    sys.exit(main())

# Last Modified by: freedomofkeima - November 28, 2014