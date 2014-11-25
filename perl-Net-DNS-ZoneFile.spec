#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	Net
%define	pnam	DNS-ZoneFile
%include	/usr/lib/rpm/macros.perl
Summary:	Net::DNS::ZoneFile - convert a zone file to a collection of RRs
Summary(pl.UTF-8):	Net::DNS::ZoneFile - konwersja pliku stref do zbioru rekordów RR
Name:		perl-Net-DNS-ZoneFile
Version:	1.04
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4fe0b670b00bc725ead2e7e13ccf89c2
URL:		http://search.cpan.org/dist/Net-DNS-ZoneFile/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Net-DNS
BuildRequires:	perl-NetAddr-IP >= 3.07
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module parses a zone file and returns a reference to an array of
Net::DNS::RR objects containing each of the RRs given in the zone in
the case that the whole zone file was succesfully parsed. Otherwise,
undef is returned.

%description -l pl.UTF-8
Ten moduł analizuje plik strefy i zwraca referencję do tablicy
obiektów Net::DNS::RR zawierających wszystkie RR podane w strefie - w
przypadku, kiedy cały plik strefy został pomyślnie przetworzony. W
przeciwnym wypadku zwracany jest undef.

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
%doc README
%{perl_vendorlib}/Net/DNS/*.pm
%{_mandir}/man3/*
