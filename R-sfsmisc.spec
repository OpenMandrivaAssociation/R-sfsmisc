%global packname  sfsmisc
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.0.26
Release:          2
Summary:          Utilities from Seminar fuer Statistik ETH Zurich
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/sfsmisc_1.0-26.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-stats R-methods R-utils 
Requires:         R-datasets R-MASS R-tcltk 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-stats R-methods R-utils
BuildRequires:   R-datasets R-MASS R-tcltk 

%description
Useful utilities ['goodies'] from Seminar fuer Statistik ETH Zurich, quite
a few related to graphics; many ported from S-plus times.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# FIXME fail to reencode latin1 to utf (should not be latin1...)
%if 0
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/help
