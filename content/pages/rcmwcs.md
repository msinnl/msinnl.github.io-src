Title: Relax-and-Cut for Maximum Weight Connected Subgraph Problems
URL:
save_as: pages/rcmwcs.html

This site contains accompanying material to the paper

> * [A Relax-and-Cut Framework for Large-Scale Maximum Weight Connected Subgraph Problems][1]  

by Eduardo Alvarez-Miranda and Markus Sinnl.

##Download the Code

The code associated with the paper can be downloaded by clicking [here][2]. Note that this program is intended to be run under Linux x64. [Boost libraries] [3] are needed for compliation. Please see the makefile for details. Note that in this code, only the Relax-and-Cut is available to make it independent of CPLEX.

The compiled program can be run by
> ./mwcs -f myinstancefilename

The instance format must be the MWCS or PCSPG format, see [4] (see this link also for instances). If you use the PCSPG format, the instance must have uniform edge-weights, as our code online applies to this cas of the problem (which can be transferred to MWCS). 

For more details on possible input parameters, try
> ./mwcs --help

[1]: ../pdfs/LMWCS-techreport.pdf
[2]: https://drive.google.com/open?id=0B1mYs4TT6IFMeXU2ZWhvVDBVbUk
[3]: http://www.boost.org/
[4]: http://dimacs11.zib.de/downloads.html