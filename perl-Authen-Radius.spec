#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires Radius server availability)
#
%include	/usr/lib/rpm/macros.perl
Summary:	Authen-TacacsPlus perl module
Summary(pl):	Modu³ perla Authen-TacacsPlus
Name:		perl-Authen-Radius
Version:	0.09
Release:	1
License:	Perl Artistic License
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Authen/RadiusPerl-%{version}.tar.gz
# Source0-md5:	1a43bd93d248e54dd259b0ca560f07f1
# for dependency resolving
BuildRequires:	perl-Data-HexDump
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen::Radius - module for authentication using RADIUS server.

%description -l pl
Authen::Radius - modu³ do autentykacji przy pomocy serwera RADIUS.

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
