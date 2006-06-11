Summary:	Digital circuit simulator
Summary(pl):	Symulator uk³adów cyfrowych
Name:		klogic
Version:	1.63
Release:	0.1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://www.a-rostin.de/klogic/Version/%{name}-%{version}.tar.gz
# Source0-md5:	83b6b6eb20046bbbb6a9860d28132d16
Source1:	%{name}.desktop
URL:		http://www.a-rostin.de/klogic/
BuildRequires:	artsc-devel
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautocompressdoc *.circuit

%description
KLogic is an application for building and simulating digital circuits.
It provides an easy way for building circuits containing standard
components like AND, OR, XOR and flipflops like RS and JK. In order to
build more complex, more structured and reuseable circuits, sub
circuits can be used.

%description -l pl
KLogic jest programem przeznaczonym do budowy i symulacji uk³adów
cyfrowych. Pozwala na tworzenie uk³adów zawieraj±cych elementy takie
jak bramki AND, OR, XOR i przerzutniki RS i JK. Bardziej rozbudowane
uk³ady mog± zostaæ podzielone na poduk³ady.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
kde_appsdir="%{_desktopdir}/kde"; export kde_appsdir
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
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

mv $RPM_BUILD_ROOT/%{_pixmapsdir}/klogic/* $RPM_BUILD_ROOT/%{_pixmapsdir}/
install -d $RPM_BUILD_ROOT/%{_desktopdir}/Edutainment
install %{SOURCE1} $RPM_BUILD_ROOT/%{_desktopdir}/Edutainment/KLogic.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc examples/*.circuit
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/Edutainment/*
%{_datadir}/apps/klogic
%{_pixmapsdir}/klogic*.xpm
