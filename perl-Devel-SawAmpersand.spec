%include	/usr/lib/rpm/macros.perl
Summary:	Devel-SawAmpersand perl module
Summary(pl):	Modu³ perla Devel-SawAmpersand
Name:		perl-Devel-SawAmpersand
Version:	0.20
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Devel/Devel-SawAmpersand-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Devel-SawAmpersand perl module querying sawampersand variable.

%description -l pl
Modu³ perla Devel-SawAmpersand.

%prep
%setup -q -n Devel-SawAmpersand-%{version}

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded \
	$RPM_BUILD_ROOT/%{perl_sitearch}/auto/Devel/SawAmpersand/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Devel/SawAmpersand
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitearch}/B/FindAmpersand.pm
%{perl_sitearch}/Devel/*.pm

%dir %{perl_sitearch}/auto/Devel/SawAmpersand
%{perl_sitearch}/auto/Devel/SawAmpersand/.packlist
%{perl_sitearch}/auto/Devel/SawAmpersand/SawAmpersand.bs
%attr(755,root,root) %{perl_sitearch}/auto/Devel/SawAmpersand/SawAmpersand.so

%{_mandir}/man3/*
