Summary:	Network performance measurement tool
Name:		iperf
Version:	2.0.4
Release:	%mkrel 2
License:	BSD
Group:		Networking/Other
URL:		http://dast.nlanr.net/Projects/Iperf/
Source0:	http://downloads.sourceforge.net/iperf/%{name}-%{version}.tar.bz2
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