Summary:	NNTP news exchange utility
Summary(pl):	Narz�dzie do wymiany news�w po NNTP
Name:		newsx
Version:	1.6
Release:	1
License:	GPL
Group:		Networking/News
Source0:	ftp://ftp.kvaleberg.com/pub/%{name}-%{version}.tar.gz
# Source0-md5:	ad9c76c53d5c7d21d86bec805fe8cd34
Patch0:		%{name}-make.patch
URL:		http://www.kvaleberg.com/newsx.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	inn-devel
Requires:	inn
Provides:	news-sucker
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Newsx is an NNTP client that will connect to a remote NNTP server and
post outgoing news articles batched by the news system (e.g. INN), as
well as fetch incoming articles.

%description -l pl
Newsx jest klientem NNTP kt�ry ��czy si� ze zdalnym serwerem i wysy�a
wychodz�ce artyku�y zgromadzone przez system news�w (np. INN) oraz
pobiera przychodz�ce artyku�y.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
# `innconfval -s` inaccessible for builder - pass everything explicitly
%configure \
	HISTORY="/var/lib/news/history" \
	INCOMING="/var/spool/news/incoming" \
	LOCKS="/var/run/news" \
	NEWSBIN="/usr/bin" \
	NEWSFEEDS="/etc/news/newsfeeds" \
	NEWSHOME="/usr" \
	NEWSLIB="/usr/share/news" \
	PATHETC="/etc/news" \
	PATHSPOOL="/var/spool/news" \
	--with-inhosts=/var/spool/news/inhosts \
	--with-newsconfig=/usr/share/news/innshellvars \
	--with-newsinclude=/usr/include/inn \
	--with-newslib=/usr/lib
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(770,root,news) %dir /var/spool/news/inhosts
%{_mandir}/man[158]/*
