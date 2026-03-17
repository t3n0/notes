# Installing PBS on Ubuntu

PBS stands for [Postable Batch System](https://en.wikipedia.org/wiki/Portable_Batch_System) and refers to the software that schedules and organise tasks to be run on a computer or cluster of computers.
Among many others job scheduling and workload management softwares, PBS comes in an open source flavor under the name of [OpenPBS](https://www.openpbs.org/).
Other information about the OpenPBS project and community can be found in the main README page of the [project](https://github.com/openpbs/openpbs). 

This guide is based on this [link](https://drtailor.medium.com/how-to-quickly-set-up-openpbs-on-ubuntu-20-04-for-single-node-workload-scheduling-704140d074e8) and on the official github [installation guide](https://github.com/openpbs/openpbs/blob/master/INSTALL).

## Installation

Copy and paste the following into the terminal (to paste in the terminal use CTRL + SHIFT + V).
1. To *build* OpenPBS un Ubuntu we need the following libraries
   
   ```
   sudo apt install gcc make libtool libhwloc-dev libx11-dev \
   libxt-dev libedit-dev libical-dev ncurses-dev perl \
   postgresql-server-dev-all postgresql-contrib python3-dev tcl-dev tk-dev swig \
   libexpat-dev libssl-dev libxext-dev libxft-dev autoconf \
   automake g++
   ```

2. To *run* OpenPBS we further need the following libraries
   
   ```
   sudo apt install expat libedit2 postgresql python3 postgresql-contrib \
   sendmail-bin tcl tk libical3 postgresql-server-dev-all
   ```

3. Download the [last version](https://github.com/openpbs/openpbs/releases/latest) (v23.06.06 at the present date) of OpenPBS, unzip it and `cd` into the folder

   ```
   wget https://github.com/openpbs/openpbs/archive/refs/tags/v23.06.06.tar.gz
   tar -xpvf v23.06.06.tar.gz
   cd openpbs-23.06.06
   ```


PBS_DATA_SERVICE_USER=postgres

4. Generate the configure scripts and makefiles

   ```
   ./autogen.sh
   ```

5. (optional) Display the available build parameters

   ```
   ./configure --help
   ```

6. Building OpenPBS for Ubuntu

   ```
   ./configure --prefix=/opt/pbs
   ```
   NOTE: if you have anaconda installed in the system, it is possible that the `make` command will fail to find the python headers needed for the build.
   In this case, you have to specify explicitly the location of you default python, for example:
   ```
   ./configure --prefix=/opt/pbs PYTHON=/usr/bin/python3.8 
   ```

7. Run make and make install
   ```
   make
   sudo make install
   ```
   

8. Run post-installation script

   ```
   sudo /opt/pbs/libexec/pbs_postinstall
   ```
   The output should look like [this](pbs_postinstall.txt).
   
9. Setup the environment: edit file `/etc/pbs.conf` and change the value of PBS_START_MOM from zero to one.
   `<editor>` can be any text editor: `gedit`, `vim`, `nano`, ...
   
   ```
   sudo <editor> /etc/pbs.conf
   ```

10. Change persmissions

    ```
    sudo chmod 4755 /opt/pbs/sbin/pbs_iff /opt/pbs/sbin/pbs_rcp
    ```

11. Start the service

    ```
    sudo /etc/init.d/pbs start
    ```
    The output of this command should be [this](pbs_start.txt).

    
12. All configured PBS services should now be running. Update your PATH and MANPATH or log out and back in.
