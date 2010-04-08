%define name	terminator
%define version 0.92
%define release %mkrel 1

Summary:	A simple way to run multiple terminals in a single window
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:        http://launchpad.net/terminator/trunk/%{version}/+download/%{name}-%{version}.tar.gz
License:	GPLv2
Group:		Terminals
Url:		http://www.tenshu.net/terminator/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-vte, gtk+2.0, gnome-python-gnomevfs
BuildRequires:	intltool
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
PYTHONDONTWRITEBYTECODE= %__python setup.py --without-icon-cache install --root=%{buildroot}

%find_lang %name

%post
gtk-update-icon-cache -qf %_iconsdir/hicolor &>/dev/null || :

%postun
gtk-update-icon-cache -qf %_iconsdir/hicolor &>/dev/null || :

%clean
%__rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc README COPYING ChangeLog
%{_mandir}/man1/%{name}.*
%{_mandir}/man5/%{name}_config.*
%{_bindir}/%{name}
%{python_sitelib}/Terminator*.egg-info
%{python_sitelib}/terminatorlib
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/%{name}*.svg
%{_datadir}/pixmaps/%{name}.png
