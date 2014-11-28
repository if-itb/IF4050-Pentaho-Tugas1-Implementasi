#!/usr/bin/env python

import constants
import json
import sys
import urllib
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
    print '--getCDAList--'
    for result in results['resultset']:
        print 'Filename:', result[0], 'FilePath:', result[1]
    print '--End of getCDAList--'
    print


def listQueries():
    path = constants.HOST + '/' + constants.CDA_ENDPOINT
    path = path + '/' + constants.CDA_LISTQUERIES
    path = path + '?path=' + constants.CDA_EXAMPLE_SERVICE_PATH
    
    # Authentication
    p = urllib2.HTTPPasswordMgrWithDefaultRealm()
    p.add_password(None, path, constants.USERNAME, constants.PASSWORD)
    handler = urllib2.HTTPBasicAuthHandler(p)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)
    
    # Retrieve JSON
    results = json.load(urllib2.urlopen(path))
    print '--listQueries--'
    for result in results['resultset']:
        print 'id:', result[0], 'name:', result[1], 'type:', result[2]
    print '--End of listQueries--'
    print

    
def listParameters():
    path = constants.HOST + '/' + constants.CDA_ENDPOINT
    path = path + '/' + constants.CDA_LISTPARAMETERS
    path = path + '?path=' + constants.CDA_EXAMPLE_SERVICE_PATH
    
    # Authentication
    p = urllib2.HTTPPasswordMgrWithDefaultRealm()
    p.add_password(None, path, constants.USERNAME, constants.PASSWORD)
    handler = urllib2.HTTPBasicAuthHandler(p)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)

    # Retrieve JSON
    parameters = {'dataAccessId' : 1}
    data = urllib.urlencode(parameters)
    path = path + '&' + data
    results = json.load(urllib2.urlopen(path))
    print '--listParameters--'
    for result in results['resultset']:
        print 'name:', result[0], 'type:', result[1], 'default:', result[2], 'pattern:', result[3]
    print '--End of listParameters--'
    print

    
def doQuery():
    # default parameter
    path = constants.HOST + '/' + constants.CDA_ENDPOINT
    path = path + '/' + constants.CDA_DOQUERY
    path = path + '?path=' + constants.CDA_EXAMPLE_SERVICE_PATH
    
    # Authentication
    p = urllib2.HTTPPasswordMgrWithDefaultRealm()
    p.add_password(None, path, constants.USERNAME, constants.PASSWORD)
    handler = urllib2.HTTPBasicAuthHandler(p)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)

    # Retrieve JSON
    parameters = {'dataAccessId' : 1}
    data = urllib.urlencode(parameters)
    path = path + '&' + data
    results = json.load(urllib2.urlopen(path))
    print '--doQuery--'
    print
    print 'Description: Aggregating TOTALPRICE of all Shipped Items (GROUPED by YEAR)'
    print
    for result in results['metadata']:
        print 'colIndex:', result['colIndex'], 'colName:', result['colName'], 'colType:', result['colType']
    for result in results['resultset']:
        print '0:', result[0], '1:', result[1], '2:', result[2], '3:', result[3]
    print '--End of doQuery--'


def main(argv=None):
    if argv is None:
        argv = sys.argv
    getCDAList() # get CDA List from Pentaho
    listQueries() # get list of Queries from Pentaho (CDA_EXAMPLE_SERVICE_PATH)
    listParameters() # get list of Parameters from CDA_EXAMPLE_SERVICE_PATH
    doQuery() # Aggregating TOTALPRICE of all Shipped Items (GROUPED by YEAR)

        
if __name__ == "__main__":
    sys.exit(main())

# Last Modified by: freedomofkeima - November 28, 2014