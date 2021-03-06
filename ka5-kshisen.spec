%define		kdeappsver	21.04.3
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kshisen
Summary:	kshisen
Name:		ka5-%{kaname}
Version:	21.04.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	9f13bc11b6032921707c55f06aad848b
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Test-devel
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	ka5-libkmahjongg-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
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
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kshisen
%{_desktopdir}/org.kde.kshisen.desktop
%{_datadir}/config.kcfg/kshisen.kcfg
%{_iconsdir}/hicolor/128x128/apps/kshisen.png
%{_iconsdir}/hicolor/16x16/apps/kshisen.png
%{_iconsdir}/hicolor/22x22/apps/kshisen.png
%{_iconsdir}/hicolor/32x32/apps/kshisen.png
%{_iconsdir}/hicolor/48x48/apps/kshisen.png
%{_iconsdir}/hicolor/64x64/apps/kshisen.png
%{_datadir}/metainfo/org.kde.kshisen.appdata.xml
%dir %{_datadir}/sounds/kshisen
%{_datadir}/sounds/kshisen/tile-fall-tile.ogg
%{_datadir}/sounds/kshisen/tile-touch.ogg
%{_datadir}/qlogging-categories5/kshisen.categories
