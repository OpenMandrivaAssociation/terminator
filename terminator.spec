%define name terminator
%define version 0.8.1
%define release %mkrel 1

Summary: A simple way to run multiple terminals in a single window
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}_%{version}.tar.lzma
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

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --record=FILELIST.tmp
grep -v man/man1 FILELIST.tmp > FILELIST

%clean
%__rm -rf %{buildroot}

%files -f FILELIST
%defattr(-,root,root)
%doc README COPYING ChangeLog
%{_mandir}/man1/terminator.*

