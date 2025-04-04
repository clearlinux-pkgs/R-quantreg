#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : R-quantreg
Version  : 6.1
Release  : 131
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/quantreg_6.1.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/quantreg_6.1.tar.gz
Summary  : Quantile Regression
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-quantreg-lib = %{version}-%{release}
Requires: R-MatrixModels
Requires: R-SparseM
BuildRequires : R-MatrixModels
BuildRequires : R-SparseM
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Linear and nonlinear parametric and non-parametric (total variation penalized) models 
  for conditional quantiles of a univariate response and several methods for handling
  censored survival data.  Portfolio selection methods based on expected shortfall
  risk are also now included. See Koenker, R. (2005) Quantile Regression, Cambridge U. Press,

%package lib
Summary: lib components for the R-quantreg package.
Group: Libraries

%description lib
lib components for the R-quantreg package.


%prep
%setup -q -n quantreg
pushd ..
cp -a quantreg buildavx2
popd
pushd ..
cp -a quantreg buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742477070

%install
export SOURCE_DATE_EPOCH=1742477070
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/quantreg/data/Bosco.rda
/usr/lib64/R/library/quantreg/data/CobarOre.rda
/usr/lib64/R/library/quantreg/data/Mammals.rda
/usr/lib64/R/library/quantreg/data/MelTemp.rda
/usr/lib64/R/library/quantreg/data/Peirce.rda
/usr/lib64/R/library/quantreg/data/barro.rda
/usr/lib64/R/library/quantreg/data/engel.rda
/usr/lib64/R/library/quantreg/data/gasprice.rda
/usr/lib64/R/library/quantreg/data/uis.rda
/usr/lib64/R/library/quantreg/demo/Frank.R
/usr/lib64/R/library/quantreg/demo/KMvCRQ.R
/usr/lib64/R/library/quantreg/demo/MCV.R
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
/usr/lib64/R/library/quantreg/demo/subset.R
/usr/lib64/R/library/quantreg/doc/crq.pdf
/usr/lib64/R/library/quantreg/doc/crq.pdf.asis
/usr/lib64/R/library/quantreg/doc/index.html
/usr/lib64/R/library/quantreg/doc/rq.pdf
/usr/lib64/R/library/quantreg/doc/rq.pdf.asis
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
/V3/usr/lib64/R/library/quantreg/libs/quantreg.so
/V4/usr/lib64/R/library/quantreg/libs/quantreg.so
/usr/lib64/R/library/quantreg/libs/quantreg.so
