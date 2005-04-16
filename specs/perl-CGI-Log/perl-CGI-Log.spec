# $Id$
# Authority: dries
# Upstream: Jason Moore <jmoore$sober,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name CGI-Log

Summary: Centralized logging of debug, error, status and success messages
Name: perl-CGI-Log
Version: 1.00
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CGI-Log/

Source: http://search.cpan.org/CPAN/authors/id/J/JM/JMOORE/CGI-Log-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
CGI::Log is a perl extension for centralized logging of debug, error,
status and success messages from scripts or other modules.  Debugging
messages include a call trace to give you the appropriate context around
each message.

Developed for use with CGI or mod_perl, but is not limited to those
applications.  Easy to use API allows for the same calling method to be
used from other modules, libraries or scripts.

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
%doc %{_mandir}/man3/*
%{perl_vendorlib}/CGI/Log.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.00-1
- Initial package.
