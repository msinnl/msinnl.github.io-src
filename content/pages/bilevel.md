Title: Bilevel Integer Programming and Interdiction Problems
URL:
save_as: pages/bilevel.html

This site contains accompanying material to the papers

> * [Intersection Cuts for Bilevel Optimization][7]  
> * [Intersection Cuts for Bilevel Optimization (journal version)][13]  
> * [A new general-purpose algorithm for mixed-integer bilevel linear programs][8]  
> * [Interdiction Games and Monotonicity][9]  
> * [A dynamic reformulation heuristic for Generalized Interdiction Problems][10]  

by Matteo Fischetti, Ivana Ljubic, Michele Monaci and Markus Sinnl.

## Solver for Mixed-Integer Bilevel Linear Problems

The intersection-cut based solver for Mixed-Integer Bilevel Linear Problems 
(described in the first three publications mentioned above) can be downloaded by [clicking here][11].
To use the solver, a **license file** must be requested from the authors, request it by [clicking here][12]

The solver is provided as binary compiled under Ubuntu 14.04 64bit with g++ 4.8.4 using CPLEX 12.7. 
It needs dynamic CPLEX libraries, which need to be generated manually by the user. 
The procedure is as follows:

1. In the script *make_cplex_dynamic.sh* provided with the binary set the environment variable CPLEX_DIR to the base directory of the CPLEX installation on your system (e.g., /opt/ibm/ILOG/CPLEX_Studio127). 
2. Run the resulting script *make_cplex_dynamic.sh* to create the dynamic CPLEX library files libconcert.so, libcplex.so and libilocplex.so. 
3. Put the generated dynamic libraries and the requested license file *bilevel.license* in the folder where the binary *bilevel* is.

The solver can be run as, e.g., 

> ./bilevel -mpsfile myInstanceFolder/myInstance.mps -setting 4

Setting refers to different settings as described in the papers, the available settings
and all other available parameters can be shown by

> ./bilevel -help

For the instance format, see below (or the file readme.md in the provided zipfile). The software is for academic purposes only, see also the file license.md in the provided zipfile.

## Instances

* Click [here][1] to download the instances based on MIPlib instances 
* Click [here][2] to download the instances based on multidimensional knapsack instances
* Click [here][3] to download the instance sets *LKIP, LCIP, GEN, TRSC+* 
* Click [here][6] to download the instance sets *INTER-FIRE, XUWANG, XUWANG-LARGE*

The format of the instances is following the format of the open-source solver [MibS][4], see also [here][5]

[1]: http://homepage.univie.ac.at/markus.sinnl/wp-content/uploads/2015/11/data_for_MPB_paper.zip
[3]: https://drive.google.com/drive/folders/0B1mYs4TT6IFMMGtBNVRZTWJjUjg?resourcekey=0-zd4i4o2Cv_tD2AArrecblQ&usp=sharing
[2]: https://drive.google.com/drive/folders/0B1mYs4TT6IFMbVNrOENEemVOZzQ?resourcekey=0-kwIfnf3m9RJ_4yHQcBL_tw&usp=sharing
[4]: https://github.com/tkralphs/MiBS
[5]: http://coral.ise.lehigh.edu/data-sets/bilevel-instances/
[6]: https://drive.google.com/drive/folders/0B1mYs4TT6IFMTEtCREc5b1E5azg?resourcekey=0-AlelaeLzIv3o7IV67xpSYw&usp=sharing
[7]: ../pdfs/IPCO_techreport.pdf
[8]: ../pdfs/secondbilevel-techreport.pdf
[9]: ../pdfs/independentSystems-techreport.pdf
[10]: ../pdfs/biheur-techreport.pdf
[11]: https://drive.google.com/drive/folders/0B1mYs4TT6IFMMVRoUm5yaXBETE0?resourcekey=0-nFfctjZNo2FuodDzQxuIgw&usp=sharing
[12]: mailto:markus.sinnl@univie.ac.at?subject=[BILEVEL]%20License%20Key%20Request&cc=m.fischetti@gmail.com,ivana.ljubic@essec.edu,michele.monaci@unibo.it
[13]: ../pdfs/MPBjournal-techreport.pdf
