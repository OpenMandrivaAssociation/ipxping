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
