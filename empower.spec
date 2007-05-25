%define name empower
%define version 0.2.0
%define release %mkrel 1

Summary:	A graphical sudo tool based on the Enlightenment Foundation Libraries
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	3-clause BSD
Group:		System/Base
URL: 		http://www.satus.net/empower
Source: 	%{name}-%{version}.tar.bz2
BuildRequires: 	evas-devel >= 0.9.9.038, ecore-devel >= 0.9.9.038, ewl-devel >= 0.5.1.008
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root

%description
A graphical sudo tool based on the Enlightenment Foundation Libraries

%prep
%setup -q

%build
%configure2_5x --enable-etk
%make

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/*
