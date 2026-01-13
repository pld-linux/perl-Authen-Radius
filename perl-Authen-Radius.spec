#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires Radius server availability)
#
%define		pdir	Authen
%define		pnam	Radius
Summary:	Authen::Radius - provide simple RADIUS client facilities
Summary(pl.UTF-8):	Authen::Radius - udostępnienie funkcji klienta RADIUS
Name:		perl-%{pdir}-%{pnam}
Version:	0.20
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Authen/RadiusPerl-%{version}.tar.gz
# Source0-md5:	acd0f83204117e47bacc0105868266b1
# for dependency resolving
BuildRequires:	perl-Data-HexDump
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen::Radius is Perl module for authentication using RADIUS server.

%description -l pl.UTF-8
Authen::Radius jest modułem Perla do autentykacji przy pomocy serwera
RADIUS.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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
