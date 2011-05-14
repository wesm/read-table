ASCII IO utilities for tabular data suitable for `datarray`, `pandas`, `larry`,
etc. use

Looking to have functionality as flexible and easy-to-use as R's `read.table`
function.

Existing functions
------------------
* numpy.lib.npyio.{genfromtxt, ndfromtxt}
* numpy.loadtxt
* pandas.io.parsers.{parseTest, parseCSV, parseExcel}
* tabular.loadSV
* matplotlib.mlab.{csv2rec, rec2csv}

Necessary features
------------------
* Inference of space, tab, or other standard delimited formats
* Handle quoted strings (a la `csv` module)
* Handle column and row names
* Ability to apply conversion function to a column (e.g. convert date strings to
  datetime objects)
* Handling of missing data (e.g. NA strings from R)
