Name:           librem
Version:        0.4.3
Release:        1%{?dist}
Summary:        Realtime audio processing library (runtime)

License:        BSD
URL:            http://www.creytiv.com/rem.html
Source0:        http://www.creytiv.com/pub/rem-%{version}.tar.gz

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

%build
make %{?_smp_mflags} LIBDIR=%{_libdir}


%install
rm -rf $RPM_BUILD_ROOT
%make_install LIBDIR=%{_libdir} MKDIR=%{_datadir}/re


%files
%doc docs/*

%{_libdir}/librem.so

%files devel
%{_includedir}/rem/
%{_libdir}/librem.a

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog

* Fri Sep 27 2013 Lars Kellogg-Stedman <lars@redhat.com> 0.4.3-1
- initial package

