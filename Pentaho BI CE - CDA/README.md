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


---

Last Updated: November 28, 2014