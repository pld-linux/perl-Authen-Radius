%include	/usr/lib/rpm/macros.perl
Summary:	Authen-TacacsPlus perl module
Summary(pl):	Modu� perla Authen-TacacsPlus
Name:		perl-Authen-Radius
Version:	0.05
Release:	4
License:	Perl Artistic License
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Authen/RadiusPerl-%{version}.tar.gz
Patch0:		%{name}-Digest-MD5.patch
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-Digest-MD5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen::Radius - module for authentication using RADIUS server.

%description -l pl
Authen::Radius - modu� do autentykacji przy pomocy serwera RADIUS.

%prep
%setup -q -n RadiusPerl-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_sitearch}/Authen

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install Authen/Radius.pm $RPM_BUILD_ROOT%{perl_sitearch}/Authen

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitearch}/Authen/Radius.pm
