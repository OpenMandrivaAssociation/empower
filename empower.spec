%define name empower
%define version 1.5.2
%define release %mkrel 3

Summary:	A graphical sudo tool based on the Enlightenment Foundation Libraries
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	3-clause BSD
Group:		System/Base
URL: 		http://www.satus.net/empower
Source: 	%{name}-%{version}.tar.bz2
BuildRequires: 	ecore-devel >= 0.9.9.050, ewl-devel >= 0.5.3.050
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root

%description
A graphical sudo tool based on the Enlightenment Foundation Libraries

%prep
%setup -q

%build
%configure2_5x --enable-ewl
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/*
