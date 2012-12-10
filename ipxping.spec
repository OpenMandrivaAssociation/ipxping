Summary:	The ipxping utility
Name:		ipxping
Version:	0.0
Release:	%mkrel 4
License:	Public Domain
Group:		Networking/Other
URL:		ftp://ftp.metalab.unc.edu/pub/Linux/system/Network/
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/Network/%{name}-%{version}.tar.gz
Patch0:		ipxping-kernel-2.2.patch
Requires:	ipxutils
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is Linux version of IPXPING wich was originally written for SUN machine
using the /dev/nit interface, by Stephen Clover <cloverst@kai.ee.cit.ac.nz>
and Justin Hoon <hoonju@kai.ee.cit.ac.nz>.

%prep

%setup -q -n %{name}
%patch0 -p0

%build
gcc %{optflags} -o ipxping ipxping-linux.c

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install ipxping %{buildroot}%{_bindir}
install ipxping.1 %{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc README*
%attr(0755,root,root) %{_bindir}/ipxping
%{_mandir}/man1/ipxping.1*


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0-4mdv2011.0
+ Revision: 619682
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.0-3mdv2010.0
+ Revision: 429544
- rebuild

* Sun Jul 20 2008 Oden Eriksson <oeriksson@mandriva.com> 0.0-2mdv2009.0
+ Revision: 239036
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Apr 17 2007 Oden Eriksson <oeriksson@mandriva.com> 0.0-1mdv2008.0
+ Revision: 13776
- Import ipxping



* Wed Apr 11 2007 Oden Eriksson <oeriksson@mandriva.com> 0.0-1mdv2007.1
- initial Mandriva package

* Tue Oct 26 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.0-3.mdk10.1.thac
- 3.mdk10.1.thac
- Where "3" is the release of the package, "mdk" is the distro, "10.1" is the release of the distro, and "thac" is the Torbjorn Turpeinen extension.

* Fri May 28 2004 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.0-2thac
- Recompiled for Mandrake 10.0

* Mon Oct 27 2003 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.0-1thac
- Recompiled for Mandrake 9.2

* Mon Mar 31 2003 Torbjorn Turpeinen <tobbe@nyvalls.se> 0.0-11mdk
- Rebuilt for Mandrake 9.1

* Mon Oct 07 2002 Torbjrn Turpeinen <tobbe@nyvalls.se> 0.0-10mdk
-rebuilt under Mandrake 9.0

* Wed Sep 18 2002 Torbjrn Turpeinen <tobbe@nyvalls.se> 0.0-9mdk
- rebuilt under Mandrake 8.2

* Mon Oct 01 2001 Peter Soos  <sp@osb.hu>
- rebuilt under RedHat Linux 7.2 beta

* Thu May 03 2001 Peter Soos  <sp@osb.hu>
- rebuilt under RedHat Linux 7.1

* Wed Apr 18 2001 Peter Soos <sp@osb.hu>
- Recompiled under RedHat Linux 7.0

* Wed May 12 1999 Peter Soos <sp@osb.hu>
- corrected the file and directory attributes to rebuild the package
  under RedHat Linux 6.0

* Fri Dec 25 1998 Peter Soos <sp@osb.hu>
- Recompiled under RedHat Linux 5.2

* Mon Jun 22 1998 Peter Soos <sp@osb.hu>
- Using %%attr

* Tue Dec 9 1997 Peter Soos <sp@osb.hu>
- Recompiled under RedHat Linux 5.0
- Now we use BuildRoot
