# SMM635 - Week 1

File created on Wed 02 Oct 2019 22:54:59 BST

Synopsis: This file provides some key commands for managing packages and
environments. For further details, go back to SMM692 (block 0).

# Package management

Anaconda users can screen and install Python libraries 'point and click' from
within the Anaconda Navigator user interface. For the command line lovers,
`conda` is the way to go. In order to search for `pkg_name` in the official
channel of Anaconda:

`conda search pkg_name`

In order to install the desired library `pkg_name`:

`conda install pkg_name`


Packages can be retrieved and installed from contributors' channels as follows:

`anaconda search (install) pkg_name`


# Managing environments

There are two main advantages in creating Python/Anaconda environments. First,
the risk of encountering package dependency issues reduces ― in other words,
creating isolated Python environments is a safe choice. Second, environments
containing just a few packages are easy to manage for humans. For example, it is
relatively easy to remember that, say, our network analysis environment has
NetworkX, Graph-Tool, and Numpy installed and working.

Anaconda users can manage Anaconda environments 'point and click' from
within the Anaconda Navigator user interface. Again, for the command line
lovers, conda is the way to go. In order to create a new environment `my_env`
the following command should be run in the terminal session:

`conda create -n my_env python=python3.X`

Once a new environment has been created, it can be activated as follows:

`conda activate my_env`

In order to deactivate the environment:

`conda deactivate my_env`
