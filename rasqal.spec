Summary:	Rasqal RDF Query Library
Summary(pl):	Rasqal - biblitoteka zapytañ RDF
Name:		rasqal
Version:	1.0
Release:	1
License:	LGPL v2 or MPL v1.1
Group:		Libraries
Source0:	http://www.redland.opensource.ac.uk/dist/source/%{name}-%{version}.tar.gz
# Source0-md5:	09a5eaec2d444faea24299479482c055
URL:		http://www.redland.opensource.ac.uk/rasqal/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RDF Query Language.

%description -l pl
Jêzyk zapytañ RDF.

%package devel
Summary:	Header files for the Rasqal RDF query library
Summary(pl):	Pliki nag³ówkowe do biblioteki zapytañ RDF Rasqal
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for the Rasqal RDF query library.

%description devel -l pl
Pliki nag³ówkowe do biblioteki zapytañ RDF Rasqal.

%package static
Summary:	Static Rasqal library
Summary(pl):	Statyczna biblioteka Rasqal
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static Rasqal library.

%description static -l pl
Statyczna biblioteka Rasqal.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE.txt NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rasqal-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man1/rasqal-config.1*
%{_mandir}/man3/librasqal.3*
%{_pkgconfigdir}/rasqal.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
