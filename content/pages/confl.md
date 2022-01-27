Title: The Connected Facility Location problem
URL:
save_as: pages/confl.html

This site contains accompanying material to the paper

> An Algorithmic Framework for the Exact Solution of Tree-Star Problems

by Markus Leitner, Ivana Ljubic, Juan-Jose Salazar-Gonzalez and Markus Sinnl.

## Instances

To download the instances, click [here][1].  
For newSet, only the instance generator is provided, as the filesize of these instances exceeds one gigabyte.  

The file-format is as follows:  
The first line (starting with *c*) is a comment line.  
The next line (starting with *p*) first contains an (unused) string, followed by *nCoreNodes* *nCustomers* *nTotalEdges*  
Next (starting with *e*) are the edges, with *nodeID1* *nodeID2* *cost*  
Next (stating with *f*) are the core nodes, with *nodeID* *openingCost*  
The nodeIDs for core nodes are from 0 to *nCoreNodes*, the remaining nodes are the customers.  
The file is terminated by the string "s 0" in the last line.  

[1]: https://drive.google.com/drive/folders/0B1mYs4TT6IFMbkRiaFIyTENHYUE?resourcekey=0-byq71ByR3OKMWb_Cfyyu6A
