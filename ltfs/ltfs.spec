# RPM specification file for LTFS.
Summary: Linear Tape File System (LTFS) - Version 3.0.0
Name: ltfs		
Version: 3.0.0	
Release: 48
Group: Util
License: LGPL	
Vendor: LTFS
Source0: ltfs_300_47.tar.gz
Requires:  fuse >= 2.8.4
Requires:  libxml2 >= 2.6.16
Requires:  libicu >= 3.6
Requires:  e2fsprogs >= 1.36
BuildRequires: gcc
BuildRequires: make
BuildRequires: icu
BuildRequires: libicu-devel
BuildRequires: fuse-devel
BuildRequires: libuuid-devel
BuildRequires: libxml2-devel

%define _unpackaged_files_terminate_build       0

%description
The LTFS software application is an open-source tape file system
implemented on dual partition tape drives.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%clean
[ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT;

%files
%defattr(-,root,root)
%config /etc/ltfs.conf
%config /etc/ltfs.conf.local
%{_datadir}/snmp/LTFS-MIB.txt
%{_datadir}/snmp/LtfsSnmpTrapDef.txt
%{_libdir}/libltfs.a
%{_libdir}/libltfs.la
%{_libdir}/libltfs.so
%{_libdir}/libltfs.so.0
%{_libdir}/libltfs.so.0.0.0
%{_libdir}/ltfs/libdriver-ltotape.la
%{_libdir}/ltfs/libdriver-ltotape.so
%{_libdir}/ltfs/libiosched-fcfs.la
%{_libdir}/ltfs/libiosched-fcfs.so
%{_libdir}/ltfs/libiosched-unified.la
%{_libdir}/ltfs/libiosched-unified.so
%{_libdir}/ltfs/libkmi-flatfile.la
%{_libdir}/ltfs/libkmi-flatfile.so
%{_libdir}/ltfs/libkmi-simple.la
%{_libdir}/ltfs/libkmi-simple.so
%{_prefix}/bin/ltfs
%{_prefix}/bin/ltfsck
%{_prefix}/bin/mkltfs
%{_prefix}/bin/unltfs

%changelog
* Wed Aug 12 2020 Jonas Svatos <jonas.svatos@nfa.cz>
- update spec and Makefiles to allow building on modern systems, especially COPR
* Wed May 11 2015 Murali <murali.vuppalapati@hp.com>
- update to 3.0.0
