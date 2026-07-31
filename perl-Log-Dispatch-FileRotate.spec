%define modname	Log-Dispatch-FileRotate
Summary:	Log to files that archive/rotate themselves in Perl
Name:		perl-%{modname}
Version:	1.38
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Log/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Path::Tiny)
BuildRequires:	perl(Log::Dispatch)
BuildRequires:	perl(Package::Stash)
BuildRequires:	perl(Sub::Identify)
BuildRequires:	perl(Date::Manip)
BuildRequires:	perl-devel

%description
Log to files that archive/rotate themselves in Perl

%prep
%setup -qn %{modname}-%{version} -n Log-Dispatch-FileRotate-1.38

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%make_install

%files
%doc README
%{perl_vendorlib}/Log/*
%{_mandir}/man3/*
