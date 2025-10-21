%global kf6_version 6.18.0

Name:           kf6-kcompletion
Version:        6.18.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 2 addon with auto completion widgets and classes
# BSD-3-Clause is in the LICENSES folder but goes unused.
License:        CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://invent.kde.org/frameworks/%{framework}
Source0:        %{name}-%{version}.tar.bz2


BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel >= %{kf6_version}
BuildRequires:  qt6-qttools-devel
BuildRequires:  kf6-kwidgets-devel
BuildRequires:  kf6-kconfig-devel 

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
%cmake_kf6 \
  -DBUILD_DESIGNERPLUGIN:BOOL=OFF \
  %{nil}
%cmake_build

%install
%cmake_install

%find_lang_kf6 kcompletion6_qt

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f kcompletion6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6Completion.so.*
%{_kf6_datadir}/qlogging-categories6/kcompletion.*

%files devel
%{_kf6_includedir}/KCompletion/
%{_kf6_libdir}/libKF6Completion.so
%{_kf6_libdir}/cmake/KF6Completion/
#%%{_kf6_qtplugindir}/designer/kcompletion6widgets.so

