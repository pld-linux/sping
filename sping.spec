Summary:	Small ping
Summary(pl):	Ma/ly ping
Name:		sping
Version:	1.2
Release:	1
Group:		Networking/Admin
Group(pl):	-
License:	BSD
Source0:	http://box3n.gumbynet.org/~fyre/software/%{name}-%{version}.tar.gz
URL:		http://box3n.gumbynet.org/~fyre/software
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sping sends ICMP ECHO requests to network hosts to determine whether they
are alive. It is a small and hopefully secure implementation of the common
ping utility that offers far less control over the packet options that may
be specified (packet size, delay between packets, etc.), for both security
and bandwidth reasons.
      
%description -l pl
sping wysy³a ¿±dania ICMP ECHO do hostów w sieci, ¿eby sprawdziæ czy
¿yj±. Jest ma³± i, miejmy nadziejê, bezpieczn± implementacj±
znanego narzêdzia "ping", która oferuje du¿o mniejsz± kontrolê nad
w³asciwo¶ciami pakietu które mo¿na ustawiæ (rozmiar pakietu, przerwy
miedzy pakietami itp.), ze wzglêdu zarówno na bezpieczeñstwo jak i na
stopieñ obci±¿enia ³±cza.

%prep
%setup  -q

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install sping $RPM_BUILD_ROOT%{_sbindir}
install sping.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(4750,root,icmp) %{_sbindir}/*
%{_mandir}/man*/*

%changelog
* %{date} PLD Team <pld-list@pld.org.pl>
All persons listed below can be reached at <cvs_login>@pld.org.pl

$Log: sping.spec,v $
Revision 1.1  2001-01-11 11:17:53  zagrodzki
- initial release
