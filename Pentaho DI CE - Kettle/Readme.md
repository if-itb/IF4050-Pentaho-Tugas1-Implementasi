# Pentaho DI CE - Kettle (Data Integration)

## Development Environment
- Pentaho CE (Data Integration)

## Prerequisites
- Download and Extract Pentaho DI CE (Kettle) from http://sourceforge.net/projects/pentaho/files/Data%20Integration/
- Kettle requires JRE version 1.5 or newer.

## Description
Pentaho Data Integration or Kettle uses two main components : Transformations and Jobs. To save these two components, we can either use a Database repository (which has to be created the first time you use Kettle), or simply save them into files (.kjb for Jobs and .ktr for Transformations).

A Transformation is a data-flow oriented unit in Kettle that executes in asynchronous mode, completing tasks assigned to it almost simultaneously. A Transformation consist of Steps and Hops. A Step is the minimal unit inside a Transformation that designed to accomplish a specific function/task, while a Hop is a graphical representation of data flowing between two Steps, with an origin and a destination. In transformation we can also code our way to process the data, for example with javascript file.

In this example we will use transformation to access a file, read it, process the items read, and write the output in another file. Kettle can read various filetypes, such as csv, XML, JSON< LDAP, LDIF, xls, etc. The output file also can varies, ranging from JSON, LDAP, until Access or Excel, even SQL file. 

A Job is a flow-control oriented unit in Kettle that executes in sequential mode, completing tasks assigned to it in the determined order. A Job consists of Job Entries, which are the Job's units of execution. A Job entry could be another Job or a Transformation. These Job Entries are also connected by Hops, which are similar like Hops in transformation, but in Job, Hops also represent sequence of execution. 

In this example we will use Job to integrate the transformations and to check validate the input file.

All of the operations above can be configured, designed, controlled, and ran in Spoon, which is a graphical tool for Kettle. If you prefer non graphical tool, you can use Pan  for Transformations, and Kitchen for Jobs.

## How to Emulate (in this example)
1. First you need to prepare your input files, in this case, ```Files/sample_data.csv```
2. You can proceed in two ways :
	a. Using Kitchen
	   Open cmd (or terminal) with root(or administrator) authorization. Run following command :
	   
	   ```kitchen /file <.kjb file full path> <input_file> /norep```
	   
	   for this example, the <.kjb file full path> = ```Transformation and Job\KettleHello.kjb```
							 <input_file> = sample_data //(without csv)
	b. Using Spoon
	   Open Spoon.bat (or Spoon.sh) at your Pentaho DI installation folder, and it will open the Spoon graphical UI. Click File->Open->Find and Choose your .kjb file->Open. It will show the graphical representations of the Jobs and transformations on the example. Finally, click Action->Run or click the run toolbar. Finally click Launch
	   
The resulted file is the sample_data_greetings.xml at ```Files```. You can delete it and see if the system works and created the same file again. 

## Addtional Notes
More tutorial and info on http://wiki.pentaho.com/display/EAI/Pentaho+Data+Integration+%28Kettle%29+Tutorial

---
Last Updated : December 2, 2014