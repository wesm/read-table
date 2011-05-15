"""readtable version information"""

# Format expected by setup.py and doc/source/conf.py: string of form "X.Y.Z"
_version_major = 0
_version_minor = 0
_version_micro = 7
__version__ = "%s.%s.%s" % (_version_major, _version_minor, _version_micro)


CLASSIFIERS = ["Development Status :: 3 - Alpha",
               "Environment :: Console",
               "Intended Audience :: Science/Research",
               "License :: OSI Approved :: BSD License",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Scientific/Engineering"]

description = "NumPy arrays with named axes and named indices."

# Note: this long_description is actually a copy/paste from the top-level
# README.txt, so that it shows up nicely on PyPI.  So please remember to edit
# it only in one place and sync it correctly.
long_description = """
=================================================================
 readtable: fast and robust loading of text into table structures
=================================================================



.. warning::

   This code is currently experimental, and its API *will* change!  It is meant
   to be a place for the community to understand and develop the right
   semantics. 
   

readtable provides a 


====  
Code
====

You can find our sources and single-click downloads:

* `Main repository`_ on Github.
* Documentation_ for all releases and current development tree.
* Download as a tar/zip file the `current trunk`_.
* Downloads of all `available releases`_.

.. _main repository: http://github.com/wesm/readtable
.. _current trunk: http://github.com/wesm/readtable/archives/master
.. _available releases: http://github.com/wesm/readtable/downloads
"""


NAME                = 'readtable'
MAINTAINER          = "Numpy Developers"
MAINTAINER_EMAIL    = "numpy-discussion@scipy.org"
DESCRIPTION         = description
LONG_DESCRIPTION    = long_description
URL                 = "http://github.com/wesm/read-table"
DOWNLOAD_URL        = "http://github.com/wesm/read-table/archives/master"
LICENSE             = "Simplified BSD"
CLASSIFIERS         = CLASSIFIERS
AUTHOR              = "readtable developers"
AUTHOR_EMAIL        = "numpy-discussion@scipy.org"
PLATFORMS           = "OS Independent"
MAJOR               = _version_major
MINOR               = _version_minor
MICRO               = _version_micro
ISRELEASED          = False
VERSION             = __version__
PACKAGES            = ["readtable", "readtable/tests"]
PACKAGE_DATA        = {'readtable': ['LICENSE']}
REQUIRES            = ["numpy"]
