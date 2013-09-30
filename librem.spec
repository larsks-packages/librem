Name:           librem
Version:        0.4.3
Release:        3%{?dist}
Summary:        Realtime audio processing library (runtime)

License:        BSD
URL:            http://www.creytiv.com/rem.html
Source0:        http://www.creytiv.com/pub/rem-%{version}.tar.gz
Patch100:       librem-0.4.3-lib-version.patch

BuildRequires:  libre-devel

%description
Librem is a portable and generic library for real-time audio and video
processing.

This package contains the runtime libraries necessary to run programs
linked against re.

%package devel
Summary:        Realtime audio processing library (development)
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Librem is a portable and generic library for real-time audio and video
processing.

This package contains the libraries and header files necessary to compile
code that uses re.


%prep
%setup -q -n rem-%{version}
%patch100 -p1 -b.libversion

%build
make %{?_smp_mflags} LIBDIR=%{_libdir}


%install
rm -rf $RPM_BUILD_ROOT
%make_install LIBDIR=%{_libdir} MKDIR=%{_datadir}/rem
rm -f $RPM_BUILD_ROOT%{_libdir}/librem.a
ln -s librem.so.%{version} $RPM_BUILD_ROOT%{_libdir}/librem.so

%files
%doc docs/*
%{_libdir}/librem.so.*

%files devel
%dir %{_includedir}/rem/
%{_includedir}/rem/*
%{_libdir}/librem.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog

* Sun Sep 30 2013 Lars Kellogg-Stedman <lars@redhat.com> 0.4.3-3
- generated versioned shared library
- ensure correct ownership of directories
- remove static library from devel package

* Fri Sep 27 2013 Lars Kellogg-Stedman <lars@redhat.com> 0.4.3-1
- initial package

