#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Authen-TacacsPlus perl module
Summary(pl):	Modu³ perla Authen-TacacsPlus
Name:		perl-Authen-Radius
Version:	0.08
Release:	1
License:	Perl Artistic License
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Authen/RadiusPerl-%{version}.tar.gz
Patch0:		%{name}-Digest-MD5.patch
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-Digest-MD5
%if %{!?_without_tests:1}0
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen::Radius - module for authentication using RADIUS server.

%description -l pl
Authen::Radius - modu³ do autentykacji przy pomocy serwera RADIUS.

%prep
%setup -q -n RadiusPerl-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

# tests require Radius server availability
%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Authen/Radius.pm
%{_mandir}/man3/*
