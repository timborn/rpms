# $Id$
# Authority: dries
# Upstream: &#9786;&#21776;&#23447;&#28450;&#9787; <autrijus$autrijus,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Convert-GeekCode

Summary: Convert and generate geek code sequences
Name: perl-Convert-GeekCode
Version: 0.51
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Convert-GeekCode/

Source: http://search.cpan.org/CPAN/authors/id/A/AU/AUTRIJUS/Convert-GeekCode-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Utility module to convert and generate geek code sequences.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man?/*
%{_bindir}/geekdec
%{_bindir}/geekgen
%{perl_vendorlib}/Convert/GeekCode.pm
%{perl_vendorlib}/Convert/GeekCode

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.51-1
- Initial package.
