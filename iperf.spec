%define major     0
%define libname   %mklibname iperf
%define oldlibname %mklibname iperf 0
%define develname %mklibname iperf -d

Name:    iperf
Version: 3.20
Release: 1
License: BSD
Group:   Networking/Other
Summary: A TCP, UDP, and SCTP network bandwidth measurement tool
URL:     https://github.com/esnet/iperf
Source:  https://github.com/esnet/%{name}/archive/%{version}.tar.gz

BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(libssl)
BuildSystem: autotools

%description
iperf is a tool for active measurements of the maximum achievable bandwidth
on IP networks. It supports tuning of various parameters related to timing,
protocols, and buffers. For each test it reports the bandwidth, loss, and
other parameters.

%package -n %{libname}
Group:    System/Libraries
Summary:  Libraries for %{name}
Requires: %{name} >= %{version}-%{release}
%rename %{oldlibname}

%description -n %{libname}
iperf is a tool for active measurements of the maximum achievable bandwidth
on IP networks. It supports tuning of various parameters related to timing,
protocols, and buffers. For each test it reports the bandwidth, loss, and
other parameters.

%package -n %{develname}
Summary:  Development files for %{name}
Group:    Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains libraries and header files for
developing applications that use %{name}.

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}3
%{_mandir}/man1/%{name}*

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}{,.*}

%files -n %{develname}
%{_includedir}/%{name}_api.h
%{_libdir}/lib%{name}.so
%{_mandir}/man3/lib%{name}*
