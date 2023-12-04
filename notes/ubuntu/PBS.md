# Installing PBS on Ubuntu

PBS stands for [Postable Batch System](https://en.wikipedia.org/wiki/Portable_Batch_System) and refers to the software that schedules and organise tasks to be run on a computer or cluster of computers.
Among many others job scheduling and workload management softwares, PBS comes in an open source flavor under the name of [OpenPBS](https://www.openpbs.org/).
Other information about the OpenPBS project and community can be found in the main README page of the [project](https://github.com/openpbs/openpbs). 

This guide is based on this [link](https://drtailor.medium.com/how-to-quickly-set-up-openpbs-on-ubuntu-20-04-for-single-node-workload-scheduling-704140d074e8) and on the official github [installation guide](https://github.com/openpbs/openpbs/blob/master/INSTALL).

## Installation

1. To run PBS un Ubuntu we need the following libraries
   
   ```
   sudo apt install gcc make libtool libhwloc-dev libx11-dev \
   libxt-dev libedit-dev libical-dev ncurses-dev perl \
   postgresql-server-dev-all postgresql-contrib python3-dev tcl-dev tk-dev swig \
   libexpat-dev libssl-dev libxext-dev libxft-dev autoconf \
   automake g++
   ```

2. Further
   
   ```
   sudo apt install expat libedit2 postgresql python3 postgresql-contrib \
   sendmail-bin tcl tk libical3 postgresql-server-dev-all
   ```
