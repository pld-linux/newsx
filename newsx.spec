Summary:	NNTP news exchange utility
Summary(pl):	Narzêdzie do wymiany newsów po NNTP
Name:		newsx
Version:	1.4
Release:	1
License:	GPL
Group:		Networking/News
Source0:	ftp://ftp.kvaleberg.com/pub/%{name}-%{version}.tar.gz
# Source0-md5:	446214ac6ef1f821dcd96106c6e689c5
Patch0:		%{name}-make.patch
URL:		http://www.kvaleberg.com/newsx.html
BuildRequires:	autoconf
Requires:	inn
Provides:	news-sucker
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Newsx is an NNTP client that will connect to a remote NNTP server and
post outgoing news articles batched by the news system (e.g. INN), as
well as fetch incoming articles.

%description -l pl
Newsx jest klientem NNTP który ³±czy siê ze zdalnym serwerem i wysy³a
wychodz±ce artyku³y zgromadzone przez system newsów (np. INN) oraz
pobiera przychodz±ce artyku³y.

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(770,root,news) %dir /var/spool/news/inhosts
%{_mandir}/*/*
