%define modname	Log-Dispatch-FileRotate
%define modver 1.35

Summary:	Log to files that archive/rotate themselves in Perl
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	3
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Log/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
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
%setup -qn %{modname}-%{modver}

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
