%define name	terminator
%define version 0.12
%define release %mkrel 1

Summary:	A simple way to run multiple terminals in a single window
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://launchpad.net/terminator/trunk/0.10/+download/%{name}_%{version}.tar.gz
License:	GPLv2+
Group:		Terminals
Url:		http://www.tenshu.net/terminator/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-vte, gtk+2.0
%py_requires -d

%description 
Terminator is an attempt to maximise useful space on a given desktop
for terminals. It is a simple Python script that places multiple vte
widgets (the same used by gnome-terminal) in a window. That's the same
widget used by gnome-terminal.

%prep
%setup -q -n %{name}-%{version}

%install
%__rm -rf %{buildroot}
%__python setup.py --without-icon-cache install --root=%{buildroot}

%find_lang %name

%post
gtk-update-icon-cache -q -f %_iconsdir/hicolor

%postun
gtk-update-icon-cache -q -f %_iconsdir/hicolor

%clean
%__rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc README COPYING ChangeLog
%{_mandir}/man*/*
%{_bindir}/*
%{python_sitelib}/Terminator*.egg-info
%{python_sitelib}/terminatorlib
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/*/*
%{_datadir}/pixmaps/*
