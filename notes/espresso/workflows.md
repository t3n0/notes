# Quantum Espresso workflows

A table with some of the possible workflows of Quantum Espresso.
Each column represents a workflow with property that we want to calculate.
The first column are the executable tools (e.g. `pw.x`, `ph.x`, `dos.x`, etc.) needed to be run to execute that specific workflow.
For any given column, each entry is labeled by a number and a brief description of the executable.
Numbers may have a "dot" such as 4.1, this happens when a workflow has multiple branches.
The top entry of any workflow is a link to a zip file that can be download and run.

|            | DOS                     | Bands                                                   | Wannier90 |
|------------|-------------------------|---------------------------------------------------------|-----------|
|`pw.x`      | (1) scf<br><br>(2) nscf | (1) scf <br><br> (2) nscf <br><br> (3) bands            |           |
|`bands.x`   |                         | (4) default <br><br> (4.1) non-coll                     |           |
|`projwfc.x` | (3) default             | (7) proj <br><br> (9) k-resolve                         |           |
|`dos.x`     | (4) default             |                                                         |           |
|`plotband.x`|                         | (5) default <br><br> (6.1) non-coll <br><br> (8) proj   |           |

Each workflow is executed by running the commands in increasing numerical order on the same branch. For example:
 - standard bands workflow: (1) &rarr; (2) &rarr; (3) &rarr; (4) &rarr; (5) &rarr; (7) &rarr; (8) &rarr; (9)
 - non-coll bands workflow: (1) &rarr; (2) &rarr; (3) &rarr; (4.1) &rarr; (5) &rarr; (6.1) &rarr; (7) &rarr; (8) &rarr; (9)
