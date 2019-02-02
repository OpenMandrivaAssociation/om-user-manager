%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{plasmaver} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary: 	OpenMandriva user manager
Name: 		om-user-manager
Version: 	0.0.1
Release: 	1
Source0: 	https://github.com/OpenMandrivaSoftware/om-user-manager/archive/v%{version}.tar.gz
Url: 		https://github.com/OpenMandrivaSoftware/om-user-manager
License: 	GPL
Group: 		System/Libraries
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5ItemModels)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(pwquality)
BuildRequires:	pkgconfig(libxcrypt)
Requires:	accountsservice
Requires:	pam_pwquality
Requires:	desktop-common-data
Conflicts:	user-manager
Obsoletes:	user-manager < 5.15.0

%description
OpenMandriva user manager.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_datadir}/polkit-1/actions/org.openmandriva.kcm.users.policy
%{_datadir}/dbus-1/system-services/org.openmandriva.kcm.users.service
%{_sysconfdir}/dbus-1/system.d/org.openmandriva.kcm.users.conf
%{_libdir}/libexec/kauth/kcm_users_authhelper
%{_libdir}/qt5/plugins/kcm_users.so
%{_datadir}/kservices5/kcm_users.desktop
