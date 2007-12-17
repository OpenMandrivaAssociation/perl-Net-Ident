%define pkgname Net-Ident

%define _provides_exceptions perl(FileHandle)

Summary:	Net::Ident - lookup the username on the remote end of a TCP/IP connection
Name:		perl-%{pkgname}
Version:	1.20
Release:	%mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://www.cpan.org
Source0:	%{pkgname}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl
BuildArch:	noarch

%description
Net::Ident is a module that looks up the username on the remote
side of a TCP/IP connection through the ident (auth/tap) protocol
described in RFC1413 (which supersedes RFC931). Note that this
requires the remote site to run a daemon (often called identd) to
provide the requested information, so it is not always available
for all TCP/IP connections.

%prep

%setup -q -n %{pkgname}-%{version}

# fix attribs
find . -type d -exec chmod 755 {} \;
find . -type f -exec chmod 644 {} \;
	
# cleanup
for i in `find . -type d -name CVS`  `find . -type d -name .svn` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find . -type f|xargs file|grep 'CRLF'|cut -d: -f1|xargs perl -p -i -e 's/\r//'
find . -type f|xargs file|grep 'text'|cut -d: -f1|xargs perl -p -i -e 's/\r//'

%build

yes "" | %{__perl} Makefile.PL INSTALLDIRS=vendor

%make

# tests are borked...
#make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Net/Ident.pm
%{_mandir}/*/*


