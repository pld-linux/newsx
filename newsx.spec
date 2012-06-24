Summary:	NNTP news exchange utility
Summary(pl):	Narz�dzie do wymiany news�w po NNTP
Name:		newsx
Version:	1.4
Release:	1
License:	GPL
Group:		Networking/News
Source0:	ftp://ftp.kvalberg.com/%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
URL:		http://www.kvaleberg.com/newsx/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	autoconf
Requires:	inn
Provides:	news-sucker

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
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/spool/news/inhosts

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FAQ COPYING NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(770,root,news) %dir /var/spool/news/inhosts
%{_mandir}/*/*
