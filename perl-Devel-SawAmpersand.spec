#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Devel
%define		pnam	SawAmpersand
Summary:	Devel::SawAmpersand Perl module
Summary(cs):	Modul Devel::SawAmpersand pro Perl
Summary(da):	Perlmodul Devel::SawAmpersand
Summary(de):	Devel::SawAmpersand Perl Modul
Summary(es):	M�dulo de Perl Devel::SawAmpersand
Summary(fr):	Module Perl Devel::SawAmpersand
Summary(it):	Modulo di Perl Devel::SawAmpersand
Summary(ja):	Devel::SawAmpersand Perl �⥸�塼��
Summary(ko):	Devel::SawAmpersand �� ����
Summary(no):	Perlmodul Devel::SawAmpersand
Summary(pl):	Modu� Perla Devel::SawAmpersand
Summary(pt):	M�dulo de Perl Devel::SawAmpersand
Summary(pt_BR):	M�dulo Perl Devel::SawAmpersand
Summary(ru):	������ ��� Perl Devel::SawAmpersand
Summary(sv):	Devel::SawAmpersand Perlmodul
Summary(uk):	������ ��� Perl Devel::SawAmpersand
Summary(zh_CN):	Devel::SawAmpersand Perl ģ��
Name:		perl-Devel-SawAmpersand
Version:	0.30
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::SawAmpersand perl module querying sawampersand variable.

%description -l cs
Modul Devel::SawAmpersand pro Perl.

%description -l da
Perlmodul Devel::SawAmpersand.

%description -l de
Devel::SawAmpersand Perl Modul.

%description -l es
M�dulo de Perl Devel::SawAmpersand.

%description -l fr
Module Perl Devel::SawAmpersand.

%description -l it
Modulo di Perl Devel::SawAmpersand.

%description -l ja
Devel::SawAmpersand Perl �⥸�塼��

%description -l ko
Devel::SawAmpersand �� ����.

%description -l no
Perlmodul Devel::SawAmpersand.

%description -l pl
Modu� perla Devel::SawAmpersand.

%description -l pt
M�dulo de Perl Devel::SawAmpersand.

%description -l pt_BR
M�dulo Perl Devel::SawAmpersand.

%description -l ru
������ ��� Perl Devel::SawAmpersand.

%description -l sv
Devel::SawAmpersand Perlmodul.

%description -l uk
������ ��� Perl Devel::SawAmpersand.

%description -l zh_CN
Devel::SawAmpersand Perl ģ��

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_sitearch}/B/FindAmpersand.pm
%{perl_sitearch}/Devel/*.pm
%dir %{perl_sitearch}/auto/Devel/SawAmpersand
%{perl_sitearch}/auto/Devel/SawAmpersand/SawAmpersand.bs
%attr(755,root,root) %{perl_sitearch}/auto/Devel/SawAmpersand/SawAmpersand.so
%{_mandir}/man3/*
