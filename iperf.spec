%define    version	2.0.2
%define    name		iperf
%define    release	%mkrel 1

Summary:   Network performance measurement tool
Name:      %name
Version:   %version
Release:   %release
License: BSD style
Group:     Networking/Other
Source:    %{name}-%{version}.tar.bz2
URL:       http://dast.nlanr.net/Projects/Iperf/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

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

%setup

%build
%configure
make

%install
cd src
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
make INSTALL_DIR=$RPM_BUILD_ROOT/%{_bindir} bindir=$RPM_BUILD_ROOT/%{_bindir} install 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README
%doc doc/*
%{_bindir}/iperf

