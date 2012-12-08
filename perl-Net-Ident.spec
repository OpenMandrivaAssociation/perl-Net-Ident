%define upstream_name    Net-Ident
%define upstream_version 1.23

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(FileHandle\\)'
%define __noautoprov 'perl\\(FileHandle\\)'
%else
%define _provides_exceptions perl(FileHandle)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Net::Ident - lookup the username on the remote end of a TCP/IP connection
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Net::Ident is a module that looks up the username on the remote
side of a TCP/IP connection through the ident (auth/tap) protocol
described in RFC1413 (which supersedes RFC931). Note that this
requires the remote site to run a daemon (often called identd) to
provide the requested information, so it is not always available
for all TCP/IP connections.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
yes "" | %__perl Makefile.PL INSTALLDIRS=vendor
%make
# tests are borked...
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Net/Ident.pm
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.230.0-5mdv2012.0
+ Revision: 765527
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.230.0-4
+ Revision: 764052
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.230.0-3
+ Revision: 667275
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.230.0-2mdv2011.0
+ Revision: 564749
- rebuild for perl 5.12.1

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.230.0-1mdv2011.0
+ Revision: 552436
- update to 1.23

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.200.0-1mdv2010.1
+ Revision: 404094
- rebuild using %%perl_convert_version

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.20-5mdv2009.1
+ Revision: 351818
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.20-4mdv2009.0
+ Revision: 223852
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.20-3mdv2008.1
+ Revision: 180517
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 1.20-2mdv2008.0
+ Revision: 67486
- buildrequires obsoletes buildprereq


* Mon Nov 20 2006 Oden Eriksson <oeriksson@mandriva.com> 1.20-2mdv2007.0
+ Revision: 85610
- use the mkrel macro
- Import perl-Net-Ident

* Fri Sep 16 2005 Oden Eriksson <oeriksson@mandriva.com> 1.20-1mdk
- initial Mandriva package

