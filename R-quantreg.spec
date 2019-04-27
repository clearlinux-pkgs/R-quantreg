#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-quantreg
Version  : 5.38
Release  : 69
URL      : https://cran.r-project.org/src/contrib/quantreg_5.38.tar.gz
Source0  : https://cran.r-project.org/src/contrib/quantreg_5.38.tar.gz
Summary  : Quantile Regression
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-quantreg-lib = %{version}-%{release}
BuildRequires : R-MatrixModels
BuildRequires : R-SparseM
BuildRequires : R-dynlm
BuildRequires : R-zoo
BuildRequires : buildreq-R

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
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552881666

%install
export SOURCE_DATE_EPOCH=1552881666
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

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library quantreg
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library quantreg
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library quantreg
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  quantreg || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/quantreg/ChangeLog
/usr/lib64/R/library/quantreg/DESCRIPTION
/usr/lib64/R/library/quantreg/FAQ
/usr/lib64/R/library/quantreg/INDEX
/usr/lib64/R/library/quantreg/Meta/Rd.rds
/usr/lib64/R/library/quantreg/Meta/data.rds
/usr/lib64/R/library/quantreg/Meta/demo.rds
/usr/lib64/R/library/quantreg/Meta/features.rds
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
/usr/lib64/R/library/quantreg/chlog
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
/usr/lib64/R/library/quantreg/demo/Mel2.R
/usr/lib64/R/library/quantreg/demo/Panel.R
/usr/lib64/R/library/quantreg/demo/Polson.R
/usr/lib64/R/library/quantreg/demo/RB-r.R
/usr/lib64/R/library/quantreg/demo/arqss.R
/usr/lib64/R/library/quantreg/demo/cobar.R
/usr/lib64/R/library/quantreg/demo/combos.R
/usr/lib64/R/library/quantreg/demo/cpoint.R
/usr/lib64/R/library/quantreg/demo/crquis.R
/usr/lib64/R/library/quantreg/demo/engel1.R
/usr/lib64/R/library/quantreg/demo/engel2.R
/usr/lib64/R/library/quantreg/demo/hinged.R
/usr/lib64/R/library/quantreg/demo/panelfig.R
/usr/lib64/R/library/quantreg/demo/predemo.R
/usr/lib64/R/library/quantreg/demo/rqsslasso.R
/usr/lib64/R/library/quantreg/demo/stack.R
/usr/lib64/R/library/quantreg/doc/abbrev.bib
/usr/lib64/R/library/quantreg/doc/book.bib
/usr/lib64/R/library/quantreg/doc/crq.pdf
/usr/lib64/R/library/quantreg/doc/index.html
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
/usr/lib64/R/library/quantreg/tests/panel.R
/usr/lib64/R/library/quantreg/tests/rq.R
/usr/lib64/R/library/quantreg/tests/rq.fit.panel.R
/usr/lib64/R/library/quantreg/tests/run-demos.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/quantreg/libs/quantreg.so
/usr/lib64/R/library/quantreg/libs/quantreg.so.avx2
/usr/lib64/R/library/quantreg/libs/quantreg.so.avx512
