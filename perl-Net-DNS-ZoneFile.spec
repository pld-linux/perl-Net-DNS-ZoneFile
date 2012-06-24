#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	DNS-ZoneFile
Summary:	Net::DNS::ZoneFile - convert a zone file to a collection of RRs
Summary(pl):	Net::DNS::ZoneFile - konwersja pliku stref do zbioru rekord�w RR
Name:		perl-Net-DNS-ZoneFile
Version:	1.04
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4fe0b670b00bc725ead2e7e13ccf89c2
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

%description -l pl
Ten modu� analizuje plik strefy i zwraca referencj� do tablicy
obiekt�w Net::DNS::RR zawieraj�cych wszystkie RR podane w strefie - w
przypadku, kiedy ca�y plik strefy zosta� pomy�lnie przetworzony. W
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
