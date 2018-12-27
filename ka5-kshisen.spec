%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		kshisen
Summary:	kshisen
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	36a21c2e92f799f3139b6b786cc88bc9
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Test-devel
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= 18.12.0
BuildRequires:	ka5-libkmahjongg-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kconfig-devel >= 5.30.0
BuildRequires:	kf5-kcrash-devel >= 5.30.0
BuildRequires:	kf5-kdbusaddons-devel >= 5.30.0
BuildRequires:	kf5-kdoctools-devel >= 5.30.0
BuildRequires:	kf5-kxmlgui-devel >= 5.30.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KShisen is a solitaire-like game played using the standard set of
Mahjong tiles. Unlike Mahjong however, KShisen has only one layer of
scrambled tiles. Unlike Mahjong however, KShisen has only one layer of
scrambled tiles.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/kshisen.categories
%attr(755,root,root) %{_bindir}/kshisen
%{_desktopdir}/org.kde.kshisen.desktop
%{_datadir}/config.kcfg/kshisen.kcfg
%{_iconsdir}/hicolor/128x128/apps/kshisen.png
%{_iconsdir}/hicolor/16x16/apps/kshisen.png
%{_iconsdir}/hicolor/22x22/apps/kshisen.png
%{_iconsdir}/hicolor/32x32/apps/kshisen.png
%{_iconsdir}/hicolor/48x48/apps/kshisen.png
%{_iconsdir}/hicolor/64x64/apps/kshisen.png
%dir %{_datadir}/kxmlgui5/kshisen
%{_datadir}/kxmlgui5/kshisen/kshisenui.rc
%{_datadir}/metainfo/org.kde.kshisen.appdata.xml
%dir %{_datadir}/sounds/kshisen
%{_datadir}/sounds/kshisen/tile-fall-tile.ogg
%{_datadir}/sounds/kshisen/tile-touch.ogg
