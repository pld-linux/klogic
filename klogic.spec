Summary:	Digital circuit simulator
Summary(pl):	Symulator uk³adów cyfrowych
Name:		klogic
Version:	1.5
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.a-rostin.de/klogic/Version/%{name}-%{version}.tar.gz
# Source0-md5:	f2381be30b539049f731bb39640f5d9c
URL:		http://www.a-rostin.de/klogic/
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        /usr/share/doc/kde/HTML

%description
KLogic is an application for building and simulating digital circuits.
It provides an easy way for building circuits containing standard
components like AND, OR, XOR and flipflops like RS and JK. In order to
build more complex, more structured and reuseable circuits, sub
circuits can be used.

%description -l pl
KLogic jest programem przeznaczonym do budowy o symulacji uk³adów
cyfrowych.

%prep
%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--disable-rpath \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc examples/*.circuit
%attr(755,root,root) %{_bindir}/*
##%{_applnkdir}/Applications/*
%{_datadir}/apps/klogic
%{_pixmapsdir}/klogic
