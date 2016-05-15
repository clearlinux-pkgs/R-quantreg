#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-quantreg
Version  : 5.24
Release  : 23
URL      : http://cran.r-project.org/src/contrib/quantreg_5.24.tar.gz
Source0  : http://cran.r-project.org/src/contrib/quantreg_5.24.tar.gz
Summary  : Quantile Regression
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-quantreg-lib
Requires: R-MatrixModels
Requires: R-SparseM
BuildRequires : R-MatrixModels
BuildRequires : R-SparseM
BuildRequires : clr-R-helpers

%description
Versions of quantreg between 3.70 and 4.75 were removed from the CRAN
archive due to uncertainties over the licensing status of the fortran
code in src/cholesky.f.  As of 9 March 2012, original authors of cholesky.f,
Esmond Ng and Barry Peyton,  have now, very kindly,  given permission to
use cholesky.f under an open source license.  They have requested that
their code be credited via the following two publications:

%package lib
Summary: lib components for the R-quantreg package.
Group: Libraries

%description lib
lib components for the R-quantreg package.


%prep
%setup -q -c -n quantreg

%build

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library quantreg
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library quantreg || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/quantreg/ChangeLog
/usr/lib64/R/library/quantreg/DESCRIPTION
/usr/lib64/R/library/quantreg/FAQ
/usr/lib64/R/library/quantreg/INDEX
/usr/lib64/R/library/quantreg/Meta/Rd.rds
/usr/lib64/R/library/quantreg/Meta/data.rds
/usr/lib64/R/library/quantreg/Meta/demo.rds
/usr/lib64/R/library/quantreg/Meta/hsearch.rds
/usr/lib64/R/library/quantreg/Meta/links.rds
/usr/lib64/R/library/quantreg/Meta/nsInfo.rds
/usr/lib64/R/library/quantreg/Meta/package.rds
/usr/lib64/R/library/quantreg/Meta/vignette.rds
/usr/lib64/R/library/quantreg/NAMESPACE
/usr/lib64/R/library/quantreg/R/quantreg
/usr/lib64/R/library/quantreg/R/quantreg.rdb
/usr/lib64/R/library/quantreg/R/quantreg.rdx
/usr/lib64/R/library/quantreg/TODO
/usr/lib64/R/library/quantreg/data/Bosco.rda
/usr/lib64/R/library/quantreg/data/CobarOre.rda
/usr/lib64/R/library/quantreg/data/Mammals.rda
/usr/lib64/R/library/quantreg/data/Peirce.rda
/usr/lib64/R/library/quantreg/data/barro.rda
/usr/lib64/R/library/quantreg/data/engel.rda
/usr/lib64/R/library/quantreg/data/gasprice.rda
/usr/lib64/R/library/quantreg/data/uis.rda
/usr/lib64/R/library/quantreg/demo/Frank.R
/usr/lib64/R/library/quantreg/demo/KMvCRQ.R
/usr/lib64/R/library/quantreg/demo/Mammals.R
/usr/lib64/R/library/quantreg/demo/Mel.R
/usr/lib64/R/library/quantreg/demo/RB-r.R
/usr/lib64/R/library/quantreg/demo/Rplots.pdf
/usr/lib64/R/library/quantreg/demo/arqss.R
/usr/lib64/R/library/quantreg/demo/cobar.R
/usr/lib64/R/library/quantreg/demo/combos.R
/usr/lib64/R/library/quantreg/demo/cpoint.R
/usr/lib64/R/library/quantreg/demo/crquis.R
/usr/lib64/R/library/quantreg/demo/engel1.R
/usr/lib64/R/library/quantreg/demo/engel2.R
/usr/lib64/R/library/quantreg/demo/hinged.R
/usr/lib64/R/library/quantreg/demo/predemo.R
/usr/lib64/R/library/quantreg/demo/rqsslasso.R
/usr/lib64/R/library/quantreg/doc/abbrev.bib
/usr/lib64/R/library/quantreg/doc/book.bib
/usr/lib64/R/library/quantreg/doc/crq.pdf
/usr/lib64/R/library/quantreg/doc/engelcoef.pdf
/usr/lib64/R/library/quantreg/doc/index.html
/usr/lib64/R/library/quantreg/doc/rq-Frankplot.pdf
/usr/lib64/R/library/quantreg/doc/rq-cobar.pdf
/usr/lib64/R/library/quantreg/doc/rq-engellogplot.pdf
/usr/lib64/R/library/quantreg/doc/rq-engelplot.pdf
/usr/lib64/R/library/quantreg/doc/rq-eqfs.pdf
/usr/lib64/R/library/quantreg/doc/rq-mammals.pdf
/usr/lib64/R/library/quantreg/doc/rq-mcycle1.pdf
/usr/lib64/R/library/quantreg/doc/rq-regspline.pdf
/usr/lib64/R/library/quantreg/doc/rq.R
/usr/lib64/R/library/quantreg/doc/rq.Rnw
/usr/lib64/R/library/quantreg/doc/rq.pdf
/usr/lib64/R/library/quantreg/doc/rqss.pdf
/usr/lib64/R/library/quantreg/help/AnIndex
/usr/lib64/R/library/quantreg/help/aliases.rds
/usr/lib64/R/library/quantreg/help/paths.rds
/usr/lib64/R/library/quantreg/help/quantreg.rdb
/usr/lib64/R/library/quantreg/help/quantreg.rdx
/usr/lib64/R/library/quantreg/html/00Index.html
/usr/lib64/R/library/quantreg/html/R.css
/usr/lib64/R/library/quantreg/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/quantreg/libs/quantreg.so
