# Pentaho BI CE - CDA (Community Data Access)


## Development Environment

- Pentaho CE (Business Analytics Platform)


## Description

CDA uses two different components: the ```connection``` (database / Pentaho datasource) and the ```dataAccess``` (a query over the connection)

There are several supported ```connection``` types such as metadata.metadata, sql.jdbc, sql.jndi, mondrian.jdbc, mondrian.jndi, olap4j.jdbc, olap4j.jndi, scripting.scripting, kettle.TransFromFile, and xPath.xPath.

On the other hand, there are several supported ```dataAccess``` types such as SQL, MDX, Metadata, Kettle, etc.

Service Endpoint: $BASE_URL/pentaho/plugin/cda/api/

Method Supported: doQuery, listQueries, getCdaList, listParameters, clearCache, listDataAccessTypes

Pentaho CDA also provides web interface for showing the query results: $BASE_URL/pentaho/plugin/cda/api/previewQuery

Example: $BASE_URL/pentaho/plugin/cda/api/previewQuery?path=public/plugin-samples/cda/cdafiles/service-sql-jdbc.cda


## How to Emulate

1. At first, upload ```data/service-sql-jdbc.cda``` to ```public/plugin-samples/cda/cdafiles/```

2. ```main.py``` will check all CDA files list. Also, this driver will perform several operations for ```service-sql-jdbc.cda```: listQueries, listParameters, doQuery.


## Additional Notes

The ```sales_data_sample.csv``` is taken from Pentaho BI CE sample data.

---

Last Updated: November 28, 2014