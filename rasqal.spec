Summary:	Rasqal RDF Query Library
Summary(pl.UTF-8):	Rasqal - biblitoteka zapytań RDF
Name:		rasqal
Version:	0.9.33
Release:	3
Epoch:		1
License:	LGPL v2.1+ or GPL v2+ or Apache v2.0+
Group:		Libraries
Source0:	http://download.librdf.org/source/%{name}-%{version}.tar.gz
# Source0-md5:	1f5def51ca0026cd192958ef07228b52
Patch0:		%{name}-link.patch
URL:		http://librdf.org/rasqal/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.11
BuildRequires:	bison >= 3.0
BuildRequires:	flex >= 2.5.36
BuildRequires:	gtk-doc >= 1.3
BuildRequires:	libraptor2-devel >= 2.0.7
BuildRequires:	libtool >= 2:2
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel >= 1:2.6.8
BuildRequires:	mhash-devel
BuildRequires:	mpfr-devel
BuildRequires:	pcre-devel >= 3.9
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	which
Requires:	libraptor2 >= 2.0.7
Requires:	libxml2 >= 1:2.6.8
Requires:	pcre >= 3.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
RDF Query Language.

%description -l pl.UTF-8
Język zapytań RDF.

%package devel
Summary:	Header files for the Rasqal RDF query library
Summary(pl.UTF-8):	Pliki nagłówkowe do biblioteki zapytań RDF Rasqal
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libraptor2-devel >= 2.0.7
Requires:	libxml2-devel >= 1:2.6.8
Requires:	mhash-devel
Requires:	mpfr-devel
Requires:	pcre-devel >= 3.9

%description devel
Header files for the Rasqal RDF query library.

%description devel -l pl.UTF-8
Pliki nagłówkowe do biblioteki zapytań RDF Rasqal.

%package static
Summary:	Static Rasqal library
Summary(pl.UTF-8):	Statyczna biblioteka Rasqal
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static Rasqal library.

%description static -l pl.UTF-8
Statyczna biblioteka Rasqal.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-datatypes \
	--enable-release \
	--with-html-dir=%{_gtkdocdir} \
	--with-raptor=system \
	--with-triples-source=raptor
# don't use redland as triples-source, as it would cause linking loop

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/librasqal.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE.txt NEWS NOTICE README RELEASE.html
%attr(755,root,root) %{_bindir}/roqet
%attr(755,root,root) %{_libdir}/librasqal.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librasqal.so.3
%{_mandir}/man1/roqet.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rasqal-config
%attr(755,root,root) %{_libdir}/librasqal.so
%{_includedir}/rasqal
%{_pkgconfigdir}/rasqal.pc
%{_mandir}/man1/rasqal-config.1*
%{_mandir}/man3/librasqal.3*
%{_gtkdocdir}/rasqal

%files static
%defattr(644,root,root,755)
%{_libdir}/librasqal.a
