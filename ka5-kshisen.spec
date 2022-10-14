#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.08.2
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kshisen
Summary:	kshisen
Name:		ka5-%{kaname}
Version:	22.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	65f543cd0c66d7f1a3d4576ae1fcc53b
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
scrambled tiles.

%description -l pl.UTF-8
KShisen jest grą jak pasjans graną przy użyciu kafelków Mahjonga.
W odróżnieniu do Mahjonga, KShisen ma tylko jeden poziom wymieszanych
kafelków.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


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
