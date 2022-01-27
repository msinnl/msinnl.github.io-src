Title: Steiner tree problem with revenues, budget, and hop-constraints
URL:
save_as: pages/stprbh.html 

This is the documentation for the program **viennaNodehopper**, which is the implementation of the branch-and-cut algorithm  
for the *Steiner tree problem with revenues, budget and hop-constraints (STPRBH)* described in

> *A Node-Based Layered Graph Approach for the Steiner Tree Problem with Revenues, Budget and Hop-Constraints*

by Markus Sinnl and Ivana Ljubic. A technical report version of this paper can be downloaded by clicking [here][1].  
Please cite our paper, if you use our code.

Our code won the category STPRBH in the [11th DIMACS Challenge][2].

## Problem Description

## Download

To download the program, please click [here][3].  
Note that this program is intended to be run under Linux x64.

## Verifying the Results Produced in Above Paper

1.  Download the instances by clicking [here][4]
2.  Create a folder *instances* in the same folder, where *code* also resides and put the instances in this folder
3.  Execute the script **runAll.sh** (this will sequentially start the runs for every instance in the folder *instances* with settings as used in the paper)

To run a single-instance with the settings used in the paper, execute **runSingle.sh INSTANCE**.

## Trying Some Other Options

The program allows to turn on/off various separation routines, the heuristic, and some more settings.  
Please run **STPRBH --help** for details on the possible settings. See also **runSingle.sh**, where most of the available options are set (note that the values set in the script are also default in the code).

[1]: ../pdfs/STPRBH-techreport.pdf
[2]: http://dimacs11.zib.de/contest/results/results.html
[3]: https://drive.google.com/drive/folders/0B1mYs4TT6IFMSVM2MHc4eXJ4c2M?resourcekey=0-HpbIfFlZM3FOgOM1yRMVlg&usp=sharing
[4]: http://dimacs11.zib.de/instances/STPRBH-RANDOM.zip
