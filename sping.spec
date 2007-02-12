Summary:	Small ping
Summary(pl.UTF-8):   Mały ping
Name:		sping
Version:	1.2
Release:	2
Group:		Networking/Admin
License:	BSD
Source0:	http://box3n.gumbynet.org/~fyre/software/%{name}-%{version}.tar.gz
# Source0-md5:	72f6b121da1850845a2d88d695bf20ec
URL:		http://box3n.gumbynet.org/~fyre/software/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sping sends ICMP ECHO requests to network hosts to determine whether
they are alive. It is a small and hopefully secure implementation of
the common ping utility that offers far less control over the packet
options that may be specified (packet size, delay between packets,
etc.), for both security and bandwidth reasons.

%description -l pl.UTF-8
sping wysyła żądania ICMP ECHO do hostów w sieci, żeby sprawdzić czy
żyją. Jest małą i, miejmy nadzieję, bezpieczną implementacją znanego
narzędzia "ping", która oferuje dużo mniejszą kontrolę nad
właściwościami pakietu które można ustawić (rozmiar pakietu, przerwy
miedzy pakietami itp.), ze względu zarówno na bezpieczeństwo jak i na
stopień obciążenia łącza.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install ping $RPM_BUILD_ROOT%{_sbindir}/sping
install ping.8 $RPM_BUILD_ROOT%{_mandir}/man8/sping.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(4750,root,adm) %{_sbindir}/*
%{_mandir}/man*/*
