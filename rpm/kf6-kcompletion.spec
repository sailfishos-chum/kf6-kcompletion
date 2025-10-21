%global kf6_version 6.18.0

Name:           kf6-kcompletion
Version:        6.18.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 2 addon with auto completion widgets and classes

License:        LGPLv2+
URL:            https://invent.kde.org/frameworks/%{framework}
Source0:        %{name}-%{version}.tar.bz2

## upstream fixes

BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  kf6-rpm-macros >= %{kf6_version}
BuildRequires:  kf6-kconfig-devel 
BuildRequires:  kf6-kwidgetsaddons-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel

%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
Requires: qt6-qtbase-gui

%description
KCompletion provides widgets with advanced completion support as well as a
lower-level completion class which can be used with your own widgets.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
export QTDIR=%{_qt6_prefix}
touch .git

%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang_kf6 kcompletion6_qt

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f kcompletion6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/locale/
%{_kf6_datadir}/qlogging-categories6/kcompletion.*
%{_kf6_libdir}/libKF6Completion.so.*
%{_kf6_qtplugindir}/designer/*5widgets.so

%files devel
%{_kf6_includedir}/KF6/KCompletion/
%{_kf6_libdir}/libKF6Completion.so
%{_kf6_libdir}/cmake/KF6Completion/
%{_kf6_archdatadir}/mkspecs/modules/qt_KCompletion.pri

