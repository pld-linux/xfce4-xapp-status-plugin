Summary:	Xapp status icon plugin for Xfce panel
Summary(pl.UTF-8):	Wtyczka ikony statusu Xapp dla panelu Xfce
Name:		xfce4-xapp-status-plugin
Version:	0.4.1
Release:	2
License:	GPL v2+
Group:		X11/Applications
#Source0Download: https://github.com/linuxmint/xfce4-xapp-status-plugin/tags
Source0:	https://github.com/linuxmint/xfce4-xapp-status-plugin/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	468dcae3e36c34dd878afa24d4730493
URL:		https://github.com/linuxmint/xfce4-xapp-status-plugin
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.37.3
BuildRequires:	gtk+3-devel >= 3.3.16
BuildRequires:	json-glib-devel >= 1.4.2
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	xapps-devel >= 1.8.7
BuildRequires:	xfce4-panel-devel >= 4.12.2
Requires:	glib2 >= 1:2.37.3
Requires:	gtk+3 >= 3.3.16
Requires:	json-glib >= 1.4.2
Requires:	xapps >= 1.8.7
Requires:	xfce4-panel >= 4.12.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xapp status icon plugin for Xfce panel.

%description -l pl.UTF-8
Wtyczka ikony statusu Xapp dla panelu Xfce.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

# not supported by glibc (as of 2.40)
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{ie,rue}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc debian/changelog
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libxapp-status-plugin.so
%{_datadir}/glib-2.0/schemas/org.x.apps.xfce4-status-plugin.gschema.xml
%{_datadir}/xfce4-xapp-status-plugin
%{_datadir}/xfce4/panel/plugins/xapp-status-plugin.desktop
