%include	/usr/lib/rpm/macros.perl
Summary:	Authen-TacacsPlus perl module
Summary(pl):	Modu³ perla Authen-TacacsPlus
Name:		perl-Authen-Radius
Version:	0.05
Release:	2
License:	Perl Artistic License
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Authen/RadiusPerl-%{version}.tar.gz
Patch0:		%{name}-Digest-MD5.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-Digest-MD5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen-Radius - module for authentication using RADIUS server.

%description -l pl
Authen-Radius - modu³ do autentykacji przy pomocy serwera RADIUS.

%prep
%setup -q -n RadiusPerl-%{version}
%patch0 -p1

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_sitearch}/Authen

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install Authen/Radius.pm $RPM_BUILD_ROOT%{perl_sitearch}/Authen

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Authen/Radius.pm
