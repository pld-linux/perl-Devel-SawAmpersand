%include	/usr/lib/rpm/macros.perl
Summary:	Devel-SawAmpersand perl module
Summary(pl):	Modu� perla Devel-SawAmpersand
Name:		perl-Devel-SawAmpersand
Version:	0.20
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Devel/Devel-SawAmpersand-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel-SawAmpersand perl module querying sawampersand variable.

%description -l pl
Modu� perla Devel-SawAmpersand.

%prep
%setup -q -n Devel-SawAmpersand-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/B/FindAmpersand.pm
%{perl_sitearch}/Devel/*.pm
%dir %{perl_sitearch}/auto/Devel/SawAmpersand
%{perl_sitearch}/auto/Devel/SawAmpersand/SawAmpersand.bs
%attr(755,root,root) %{perl_sitearch}/auto/Devel/SawAmpersand/SawAmpersand.so
%{_mandir}/man3/*
