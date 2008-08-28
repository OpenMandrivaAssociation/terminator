%define name terminator
%define version 0.10
%define release %mkrel 1

Summary: A simple way to run multiple terminals in a single window
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://launchpad.net/terminator/trunk/0.10/+download/%{name}_%{version}.tar.gz
License: GPLv2+
Group: Terminals
Url: http://www.tenshu.net/terminator/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires: python, python-vte
BuildRequires: python-devel

%description 
Terminator is an attempt to maximise useful space on a given desktop
for terminals. It is a simple Python script that places multiple vte
widgets (the same used by gnome-terminal) in a window. That's the same
widget used by gnome-terminal.

%prep
%setup -q -n %{name}-%{version}

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot}

%find_lang %name

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
