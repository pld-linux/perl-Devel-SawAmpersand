#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Devel
%define		pnam	SawAmpersand
Summary:	Devel::SawAmpersand - querying sawampersand variable
Summary(pl.UTF-8):	Devel::SawAmpersand - pobieranie wartości zmiennej sawampersand
Name:		perl-Devel-SawAmpersand
Version:	0.31
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2ac8f290f0d54ebb79b6e8c867f9d9f5
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::SawAmpersand Perl module is for querying sawampersand variable.
The global variable sawampersand gets set to true in that moment in
which the parser sees one of $, $', and $&. It never can be set to
false again. Trying to set it to false breaks the handling of the $,
$&, and $' completely.

%description -l pl.UTF-8
Moduł Perla Devel::SawAmpersand służy do pobierania wartości zmiennej
sawampersand. Zmienna globalna sawampersand jest ustawiana na "true".
gdy analizator składniowy Perla zobaczy $, $' lub $&. Nie można jej
ponownie ustawić na "false". Próba uczynienia tego spowodowałaby
całkowite popsucie obsługi symboli $, $& i $'.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%{perl_vendorarch}/B/FindAmpersand.pm
%{perl_vendorarch}/Devel/*.pm
%dir %{perl_vendorarch}/auto/Devel/SawAmpersand
%{perl_vendorarch}/auto/Devel/SawAmpersand/SawAmpersand.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Devel/SawAmpersand/SawAmpersand.so
%{_mandir}/man3/*
