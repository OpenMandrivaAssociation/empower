#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/empower empower; \
#cd empower; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#VERSION=$(cat configure.ac | grep "empower" | grep INIT | sed 's@\[@@g' | sed 's@\]@@g' | sed 's@)@@g' | cut -d, -f 2 | sed "s@ @@"); \
#PKG_VERSION=$VERSION.$SVNREV; \
#cd ..; \
#tar -Jcf empower-$PKG_VERSION.tar.xz empower/ --exclude .svn --exclude .*ignore

%define gitdate 20150504

Summary:	A graphical sudo tool based on the Enlightenment Foundation Libraries
Name:		empower
Version:	2.0.999
Release:	0.%{gitdate}.1
License:	3-clause BSD
Group:		System/Base
URL: 		http://enlightenment.org
Source0: 	%{name}-%{version}.%{gitdate}.tar.xz

BuildRequires: 	gettext-devel
BuildRequires: 	pkgconfig(edje)
BuildRequires:	pkgconfig(efl)
BuildRequires: 	pkgconfig(elementary)
BuildRequires:	pkgconfig(eweather)
BuildRequires:	pkgconfig(e_dbus)

%description
A graphical sudo tool based on the Enlightenment Foundation Libraries

%prep
%setup -qn %{name}

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x 
%make

%install
%makeinstall_std
mkdir -p %{buildroot}/%{_docdir}/%{name}/

mv %{buildroot}/%{_datadir}/%{name}/AUTHORS %{buildroot}/%{_docdir}/%{name}/
mv %{buildroot}/%{_datadir}/%{name}/COPYING %{buildroot}/%{_docdir}/%{name}/

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/*
%{_datadir}/%{name}/data/*.png
