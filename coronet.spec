Summary:	Coronet library
Summary(pl.UTF-8):	Biblioteka coronet
Name:		coronet
Version:	0.23
Release:	0.1
License:	LGPL
Group:		Libraries
Source0:	http://www.xmailserver.org/%{name}-%{version}.tar.gz
# Source0-md5:	30637e028bd95d1e54774b5d07ab44b4
URL:		http://www.xmailserver.org/coronet-lib.html
BuildRequires:	libpcl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The coronet library implements an epoll and coroutine based library
that allows for async operations over certain kinds of files. Any file
that supports poll(2) and the O_NONBLOCK fcntl(2) flag can be hosted;
this includes like sockets and pipes.

The coronet library uses the epoll support available in the 2.6 series
of Linux kernels, and the libpcl library for coroutine support.

%description -l pl.UTF-8
Biblioteka coronet to implementacja biblioteki opartnej na epoll i
korutynach pozwalająca na operacje asynchroniczne na plikach
wszelkiego rodzaju. Obsługiwany może być dowolny plik obsługujący
poll(2) i flagę fcntl(2) O_NONBLOCK; obejmuje to gniazda i potoki.

Biblioteka coronet wykorzystuje wywołanie epoll dostępne w jądrach
Linuksa od wersji 2.6 oraz bibliotekę libpcl do obsługi korutyn.

%package devel
Summary:	Header files for coronet library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki coronet
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for coronet library.

%description devel -l pl.UTF-8
Pakiet zawierający pliki nagłówkowe biblioteki coronet.

%package static
Summary:	Static coronet library
Summary(pl.UTF-8):	Statyczna biblioteka coronet
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static coronet library.

%description static -l pl.UTF-8
Statyczna biblioteka coronet.

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
%doc AUTHORS
%attr(755,root,root) %{_libdir}/libcoronet.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcoronet.so
%{_libdir}/libcoronet.la
%{_includedir}/coronet.h
%{_mandir}/man3/coronet.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libcoronet.a
