#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires Radius server availability)
#
%include	/usr/lib/rpm/macros.perl
Summary:	Authen::Radius - provide simple RADIUS client facilities
Summary(pl):	Authen::Radius - udostępnienie funkcji klienta RADIUS
Name:		perl-Authen-Radius
Version:	0.11
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Authen/RadiusPerl-%{version}.tar.gz
# Source0-md5:	5c320a936d5d3819220f2d639db007db
# for dependency resolving
BuildRequires:	perl-Data-HexDump
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen::Radius is Perl module for authentication using RADIUS server.

%description -l pl
Authen::Radius jest modułem Perla do autentykacji przy pomocy serwera
RADIUS.

%prep
%setup -q -n RadiusPerl-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Authen/Radius.pm
