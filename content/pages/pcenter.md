Title: The p-center problem
URL:
save_as: pages/pcenter.html

This site contains accompanying material to the paper

> * [A scaleable projection‐based branch‐and‐cut algorithm for the p‐center problem][1]

by E.Gaar and M. Sinnl.

The solver can be downloaded by [clicking here][4]. The software is for academic purposes only, see also license.md. To use the solver, a **license file** must be requested from the authors, request it by [mail] [3]. The solver can handle two instances-formats corresponding to standard benchmark instance sets from literature, namely *TSPlib* and *pmedian*. For *TSPlib* instances the distances are rounded to the next integer as described in the paper following previous literature.

The solver is provided as binary called *pcenter* compiled under Ubuntu 20.04 64bit with g++ 9.4.0 using CPLEX 12.10 (other versions of CPLEX may also work). The solver needs the [Boost][2] libraries *system*, *filesystem* and *program_options*. A standard installation of Boost should work. It also needs dynamic CPLEX libraries, which need to be generated manually by the user. The procedure is as following:

1. In the script *make_cplex_dynamic.sh* provided with the binary set the variable *CPLEX_DIR* to the base directory of the CPLEX installation on your system (e.g., /opt/ibm/ILOG/CPLEX_Studio1210).
2. Run the resulting script *make_cplex_dynamic.sh* to create the dynamic CPLEX library files libconcert.so, libcplex.so and libilocplex.so.
3. Put the generated dynamic libraries and the requested license *pcenter.license* in the folder where the binary *pcenter* is.


## Running the Solver

The solver can be run as, e.g.,

>./pcenter -f *INSTANCENAME* --p *NUMBER* --instanceformat *NUMBER* -t *NUMBER* -m *NUMBER*

These settings and parameters can also be shown by

>./pcenter --help

### Parameter explanation

* -f instance to be solved
* --p the cardinality constraint
* --instanceformat: 1 (TSPlib-instances), 2 (Pmedian-instances)
* -t timelimit in seconds
* -m memorylimit in MB

[1]: https://www.sciencedirect.com/science/article/pii/S0377221722001187
[2]: https://www.boost.org/
[3]: mailto:markus.sinnl@jku.at?subject=[PCENTER]%20License%20Key%20Request&cc=elisabeth.gaar@jku.at
[4]: https://drive.google.com/drive/folders/1vjPlWqPFUMAdweBOn0LOBJ1GediuRc25?usp=share_link
