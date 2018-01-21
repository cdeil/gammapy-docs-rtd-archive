# gammapy-docs-rtd-archive

Archive of Gammapy old docs versions from RTD

This archive was generated on Jan 21, 2018
by fetching files from http://gammapy.readthedocs.io
before deleting that account.

You can view the old docs versions online here:

* [v0.1](https://rawgit.com/cdeil/gammapy-docs-rtd-archive/master/html/v0.1/)
* [v0.2](https://rawgit.com/cdeil/gammapy-docs-rtd-archive/master/html/v0.2/)
* [v0.3](https://rawgit.com/cdeil/gammapy-docs-rtd-archive/master/html/v0.3/)
* [v0.4](https://rawgit.com/cdeil/gammapy-docs-rtd-archive/master/html/v0.4/)
* [v0.5](https://rawgit.com/cdeil/gammapy-docs-rtd-archive/master/html/v0.5/)
* [v0.6](https://rawgit.com/cdeil/gammapy-docs-rtd-archive/master/html/v0.6/)
* [latest](https://rawgit.com/cdeil/gammapy-docs-rtd-archive/master/html/latest/)

or just download this repo via git or the zip download feature on Github,
and then view the docs locally.

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
