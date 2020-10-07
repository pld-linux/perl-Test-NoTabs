#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Test
%define		pnam	NoTabs
Summary:	Test::NoTabs - check the presence of tabs in your project
Summary(pl.UTF-8):	Test::NoTabs - sprawdzanie obecności tabulatorów w projekcie
Name:		perl-Test-NoTabs
Version:	2.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/Test-NoTabs-%{version}.tar.gz
# Source0-md5:	e3d583673b12762d85b843ba5b2b2201
URL:		https://metacpan.org/release/Test-NoTabs
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module scans your project/distribution for any Perl files
(scripts, modules, etc) for the presence of tabs.

%description -l pl.UTF-8
Ten moduł skanuje projekt/dystrybucję w poszukiwaniu plików
perlowych (skryptów, modułów itp) i sprawdza je pod kątem obecności
znaków tabulacji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/NoTabs.pm
%{_mandir}/man3/Test::NoTabs.3pm*
