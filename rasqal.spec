Summary:	Rasqal RDF Query Library
Summary(pl):	Rasqal - biblitoteka zapytañ RDF
Name:		rasqal
Version:	0.9.9
Release:	1
Epoch:		1
License:	LGPL v2.1+ or GPL v2+ or Apache v2.0+
Group:		Libraries
Source0:	http://librdf.org/dist/source/%{name}-%{version}.tar.gz
# Source0-md5:	758e331ce0dbf5b8f3e74c34cb065412
URL:		http://librdf.org/rasqal/
BuildRequires:	automake >= 1:1.7
BuildRequires:	flex >= 2.5.31
BuildRequires:	libraptor-devel >= 1.4.4
BuildRequires:	pcre-devel >= 3.9
#BuildRequires:	redland-devel >= 0.9.16
Requires:	libraptor >= 1.4.4
Requires:	pcre >= 3.9
#Requires:	redland >= 0.9.16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RDF Query Language.

%description -l pl
Jêzyk zapytañ RDF.

%package devel
Summary:	Header files for the Rasqal RDF query library
Summary(pl):	Pliki nag³ówkowe do biblioteki zapytañ RDF Rasqal
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libraptor-devel >= 1.4.4
Requires:	pcre-devel >= 3.9
#Requires:	redland-devel >= 0.9.16

%description devel
Header files for the Rasqal RDF query library.

%description devel -l pl
Pliki nag³ówkowe do biblioteki zapytañ RDF Rasqal.

%package static
Summary:	Static Rasqal library
Summary(pl):	Statyczna biblioteka Rasqal
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static Rasqal library.

%description static -l pl
Statyczna biblioteka Rasqal.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* .
%configure \
	--enable-release \
	--with-raptor=system \
	--with-triples-source=raptor
# don't use redland as triples-source, as it would cause linking loop

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
%attr(755,root,root) %{_bindir}/roqet
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man1/roqet.1*

%files devel
%defattr(644,root,root,755)
%doc docs/{README.html,api}
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
