
Summary:	A simple way to run multiple terminals in a single window
Name:		terminator
License:	GPLv2
Group:		Terminals
Release:	1
Version:	2.1.3
Url:            https://github.com/gnome-terminator
Source0:        https://github.com/gnome-terminator/terminator/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	intltool
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(pytest-runner)
BuildRequires:  python-setuptools

Requires: python3dist(pycairo)
Requires: python3dist(configobj)
Requires: python3dist(pygobject)
Requires: python3dist(psutil)
Requires: python-setuptools
Requires: python-dbus

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
%{python_sitelib}/%{name}-%{version}-py%{python_version}.egg-info
%{python_sitelib}/terminatorlib/
%{_mandir}/man1/%{name}.*
%{_mandir}/man5/%{name}_config.*
%{_datadir}/locale/*/LC_MESSAGES/terminator.mo
%{_datadir}/terminator/terminatorlib/themes/*


%changelog
* Fri Feb 03 2012 Lev Givon <lev@mandriva.org> 0.96-2mdv2012.0
+ Revision: 771007
- Suggest python-keybinder, python-notify.
  Correct website URI.

* Tue Oct 04 2011 Lev Givon <lev@mandriva.org> 0.96-1
+ Revision: 702652
- Update to 0.96.

* Mon Nov 01 2010 Anssi Hannula <anssi@mandriva.org> 0.95-2mdv2011.0
+ Revision: 591577
- rebuild for new python
- remove the now unneeded usage of py_requires macro

* Wed Aug 25 2010 Funda Wang <fwang@mandriva.org> 0.95-1mdv2011.0
+ Revision: 573022
- update to new version 0.95

  + Lev Givon <lev@mandriva.org>
    - Update to 0.94.

* Tue May 25 2010 Lev Givon <lev@mandriva.org> 0.93-2mdv2010.1
+ Revision: 545989
- Add patch for terminator bug #563445.

* Fri Apr 16 2010 Funda Wang <fwang@mandriva.org> 0.93-1mdv2010.1
+ Revision: 535309
- new version 0.93

* Wed Apr 14 2010 Lev Givon <lev@mandriva.org> 0.92-2mdv2010.1
+ Revision: 534626
- Backport fix for terminator bug #546665.

* Thu Apr 08 2010 Lev Givon <lev@mandriva.org> 0.92-1mdv2010.1
+ Revision: 532894
- Update to 0.92.

* Sun Apr 04 2010 Lev Givon <lev@mandriva.org> 0.91-1mdv2010.1
+ Revision: 531443
- Update to 0.91.

* Thu Dec 03 2009 Funda Wang <fwang@mandriva.org> 0.14-1mdv2010.1
+ Revision: 472981
- new version 0.14

* Thu Jun 25 2009 Lev Givon <lev@mandriva.org> 0.13-1mdv2010.0
+ Revision: 389170
- Update to 0.13.
  Suppress irritating exit notification pop-up.

* Thu Mar 19 2009 Lev Givon <lev@mandriva.org> 0.12-2mdv2009.1
+ Revision: 357777
- Add gnome-python-gnomevfs dependency.

* Mon Jan 26 2009 Lev Givon <lev@mandriva.org> 0.12-1mdv2009.1
+ Revision: 333847
- Update to 0.12.

* Sat Jan 10 2009 Funda Wang <fwang@mandriva.org> 0.11-2mdv2009.1
+ Revision: 327911
- rebuild

* Thu Oct 16 2008 Lev Givon <lev@mandriva.org> 0.11-1mdv2009.1
+ Revision: 294277
- Update to 0.11.

* Fri Aug 29 2008 Funda Wang <fwang@mandriva.org> 0.10-1mdv2009.0
+ Revision: 277157
- New version 0.10

* Wed Jul 09 2008 Lev Givon <lev@mandriva.org> 0.9-1mdv2009.0
+ Revision: 233088
- Update to 0.9.

* Thu May 15 2008 Lev Givon <lev@mandriva.org> 0.8.1-1mdv2009.0
+ Revision: 207727
- import terminator


* Thu May 15 2008 Lev Givon <lev@mandriva.org> 0.8.1-1mdv2008.1
- Package for Mandriva.

