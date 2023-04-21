%bcond_with	tests

Summary:	A simple way to run multiple terminals in a single window
Name:		terminator
License:	GPLv2
Group:		Terminals
Release:	5
Version:	2.1.3
Url:            https://github.com/gnome-terminator
Source0:        https://github.com/gnome-terminator/terminator/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	intltool
BuildRequires:	pkgconfig(python)
#BuildRequires:	python%{py_ver}dist(pytest-runner)
BuildRequires:	python%{py_ver}dist(setuptools)
BuildRequires:	python%{py_ver}dist(pip)
BuildRequires:	python%{py_ver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{py_ver}dist(configobj)
BuildRequires:	python%{py_ver}dist(dbus-python)
BuildRequires:	python%{py_ver}dist(pycairo)
BuildRequires:	python%{py_ver}dist(pygobject)
BuildRequires:	python%{py_ver}dist(psutil)
BuildRequires:	python%{py_ver}dist(pytest)
BuildRequires:  x11-server-xvfb
%endif

Requires:	keybinder
Requires:	vte
Requires:	typelib(Vte) = 2.91
Requires:	typelib(Notify)
Requires:	typelib(Keybinder)

%description 
Terminator is an attempt to maximise useful space on a given desktop
for terminals. It is a simple Python script that places multiple vte
widgets (the same used by gnome-terminal) in a window. That's the same
widget used by gnome-terminal.

%prep
%autosetup -p1

%build
%py_build

%install
%py_install

%files
%{_bindir}/%{name}
%{_bindir}/remotinator
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/terminator.metainfo.xml
%{_datadir}/pixmaps/%{name}.png
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/%{name}*.svg
%{_iconsdir}/HighContrast/*/*/*.png
%{_iconsdir}/HighContrast/*/*/%{name}*.svg
%{python_sitelib}/%{name}-%{version}-py%{python_version}.*-info
%{python_sitelib}/terminatorlib/
%{_mandir}/man1/%{name}.*
%{_mandir}/man5/%{name}_config.*
%{_datadir}/locale/*/LC_MESSAGES/terminator.mo
%{_datadir}/terminator/terminatorlib/themes/*

%check
%if %{with tests}
#export LC_ALL=en_US.UTF-8
let "dnum = $RANDOM % 90 + 10"
xvfb-run -n $dnum %__python setup.py test
%endif

