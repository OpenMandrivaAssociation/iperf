Summary:	Network performance measurement tool
Name:		iperf
Version:	2.0.5
Release:	2
License:	BSD
Group:		Networking/Other
URL:		http://dast.nlanr.net/Projects/Iperf/
Source0:	http://downloads.sourceforge.net/iperf/%{name}-%{version}.tar.gz
Patch0:         iperf-2.0.5-fix-str-fmt.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Iperf is a network performance measurement tool.

While tools to measure network performance, such as ttcp, exist, 
most are very old and have confusing options. 
Iperf was developed as a modern alternative for measuring TCP and UDP 
bandwidth performance.

Iperf is a tool to measure maximum TCP bandwidth, allowing 
the tuning of various parameters and UDP characteristics. 
Iperf reports bandwidth, delay jitter, datagram loss. 

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%doc doc/*
%{_bindir}/iperf
%{_mandir}/man1/*


%changelog
* Wed Apr 27 2011 Leonardo Coelho <leonardoc@mandriva.com> 2.0.5-1mdv2011.0
+ Revision: 659687
- new package and patch version

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.4-3mdv2011.0
+ Revision: 612403
- the mass rebuild of 2010.1 packages

* Fri Feb 19 2010 Funda Wang <fwang@mandriva.org> 2.0.4-2mdv2010.1
+ Revision: 508445
- fix str fmt

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Jul 27 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.0.4-1mdv2009.0
+ Revision: 250471
- update to new version 2.0.4
- use macros
- fix mixture of tabs and spaces
- update file list
- spec file clean

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.0.2-3mdv2009.0
+ Revision: 247248
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2.0.2-1mdv2008.1
+ Revision: 127095
- kill re-definition of %%buildroot on Pixel's request
- import iperf


* Fri Dec 16 2005 Erwan Velu <erwan@seanodes.com> 2.0.2-1mdk
- 2.0.2

* Tue Jun 29 2004 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.7.0-2mdk
- rebuild for new g++

* Thu Apr 28 2004 Bruno Cornec <bruno@HyPer-Linux.org> 1.7.0-1mdk
- first packaged
