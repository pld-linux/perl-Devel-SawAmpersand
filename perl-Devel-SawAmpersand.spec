#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Devel
%define		pnam	SawAmpersand
Summary:	Devel::SawAmpersand - querying sawampersand variable
Summary(pl):	Devel::SawAmpersand - pobieranie warto¶ci zmiennej sawampersand
Name:		perl-Devel-SawAmpersand
Version:	0.30
Release:	3
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7e23b11e808d7e5c57f83fe5b7c91a3c
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::SawAmpersand Perl module is for querying sawampersand variable.
The global variable sawampersand gets set to true in that moment in
which the parser sees one of $, $', and $&. It never can be set to
false again. Trying to set it to false breaks the handling of the $,
$&, and $' completely.

%description -l pl
Modu³ Perla Devel::SawAmpersand s³u¿y do pobierania warto¶ci zmiennej
sawampersand. Zmienna globalna sawampersand jest ustawiana na "true".
gdy analizator sk³adniowy Perla zobaczy $, $' lub $&. Nie mo¿na jej
ponownie ustawiæ na "false". Próba uczynienia tego spowodowa³aby
ca³kowite popsucie obs³ugi symboli $, $& i $'.

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
%doc ChangeLog README
%{perl_vendorarch}/B/FindAmpersand.pm
%{perl_vendorarch}/Devel/*.pm
%dir %{perl_vendorarch}/auto/Devel/SawAmpersand
%{perl_vendorarch}/auto/Devel/SawAmpersand/SawAmpersand.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Devel/SawAmpersand/SawAmpersand.so
%{_mandir}/man3/*
