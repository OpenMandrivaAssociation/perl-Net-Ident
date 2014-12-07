%define modname	Net-Ident
%define modver	1.23

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(FileHandle\\)'
%define __noautoprov 'perl\\(FileHandle\\)'
%else
%define _provides_exceptions perl(FileHandle)
%endif

Summary:	Net::Ident - lookup the username on the remote end of a TCP/IP connection
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	15
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Net/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
Net::Ident is a module that looks up the username on the remote
side of a TCP/IP connection through the ident (auth/tap) protocol
described in RFC1413 (which supersedes RFC931). Note that this
requires the remote site to run a daemon (often called identd) to
provide the requested information, so it is not always available
for all TCP/IP connections.

%prep
%setup -qn %{modname}-%{modver}

# fix attribs
find . -type d -exec chmod 755 {} \;
find . -type f -exec chmod 644 {} \;
	
# cleanup
for i in `find . -type d -name CVS`  `find . -type d -name .svn` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find . -type f|xargs file|grep 'CRLF'|cut -d:	-f1|xargs perl -p -i -e 's/\r//'
find . -type f|xargs file|grep 'text'|cut -d:	-f1|xargs perl -p -i -e 's/\r//'

%build
yes "" | %__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# tests are borked...
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Net/Ident.pm
%{_mandir}/man3/*

