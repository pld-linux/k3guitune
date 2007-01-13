Summary:	K3Guitune - a simple guitar tuning program
Summary(pl):	K3Guitune - program do strojenia gitary
Name:		k3guitune
Version:	0.5.2
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://home.planet.nl/~lamer024/files/%{name}-%{version}.tar.bz2
# Source0-md5:	72f18f21073cb41fafd33e6330940fa2
Source1:        %{name}.desktop
URL:		http://home.planet.nl/~lamer024/k3guitune.html
BuildRequires:	alsa-lib-devel
BuildRequires:	artsc-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libsamplerate-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
K3Guitune is a simple musical instrument tuning program.

%description -l pl
K3Guitune to prosty program do strojenia instrumentów muzycznych.

%prep
%setup -q

%build
%configure \
	kde_htmldir="%{_datadir}/doc/kde/HTML" \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/k3guitune
%{_datadir}/apps/%{name}
%{_desktopdir}/*.desktop
