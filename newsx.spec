Summary:	NNTP news exchange utility
Name:		newsx
Version:	1.4
Release:	1
License:	GPL
Group:		Networking/News
Group(pl):	Sieciowe/News
Source0:	ftp://ftp.kvalberg.com/%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
URL:		http://www.kvaleberg.com/newsx/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	inn
Provides:	news-sucker

%description
Newsx is an NNTP client that will connect to a remote NNTP server and
post outgoing news articles batched by the news system (e.g. INN), as
well as fetch incoming articles.

%prep
%setup -q
%patch0 -p1
%build
autoconf

CFLAGS="$RPM_OPT_FLAGS"; export CFLAGS
LDFLAGS="-s"; export LDFLAGS
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/var/spool/news/inhosts

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf FAQ COPYING NEWS README $RPM_BUILD_ROOT%{_mandir}/*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {FAQ,COPYING,NEWS,README}.gz
%attr(755,root,root) %{_bindir}/*
%attr(750,news,news) %dir /var/spool/news/inhosts
%{_mandir}/*/*
