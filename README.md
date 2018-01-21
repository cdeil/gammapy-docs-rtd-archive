# gammapy-docs-rtd-archive

Archive of Gammapy old docs versions from RTD

This archive was generatedon Jan 21, 2018
by fetching files from http://gammapy.readthedocs.io
before deleting that account.


## Download from RTD

RTD doesn't support downloading the HTML page:
https://github.com/rtfd/readthedocs.org/issues/3242

However, one can use e.g. wget to do it
https://www.guyrutenberg.com/2014/05/02/make-offline-mirror-of-a-site-using-wget/

To fetch the HTML docs, this command was used for each version:
```
wget -mkEpnp http://gammapy.readthedocs.io/en/v0.4
mv gammapy.readthedocs.io/en/v0.4 .
rm -r gammapy.readthedocs.io
```
