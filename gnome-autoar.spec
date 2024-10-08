#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v19
# autospec commit: f35655a
#
Name     : gnome-autoar
Version  : 0.4.5
Release  : 30
URL      : https://download.gnome.org/sources/gnome-autoar/0.4/gnome-autoar-0.4.5.tar.xz
Source0  : https://download.gnome.org/sources/gnome-autoar/0.4/gnome-autoar-0.4.5.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: gnome-autoar-data = %{version}-%{release}
Requires: gnome-autoar-lib = %{version}-%{release}
Requires: gnome-autoar-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : libarchive-dev
BuildRequires : pkgconfig(libarchive)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# gnome-autoar
gnome-autoar provides functions and widgets for GNOME applications which want
to use archives as a method to transfer directories over the Internet.

%package data
Summary: data components for the gnome-autoar package.
Group: Data

%description data
data components for the gnome-autoar package.


%package dev
Summary: dev components for the gnome-autoar package.
Group: Development
Requires: gnome-autoar-lib = %{version}-%{release}
Requires: gnome-autoar-data = %{version}-%{release}
Provides: gnome-autoar-devel = %{version}-%{release}
Requires: gnome-autoar = %{version}-%{release}

%description dev
dev components for the gnome-autoar package.


%package lib
Summary: lib components for the gnome-autoar package.
Group: Libraries
Requires: gnome-autoar-data = %{version}-%{release}
Requires: gnome-autoar-license = %{version}-%{release}

%description lib
lib components for the gnome-autoar package.


%package license
Summary: license components for the gnome-autoar package.
Group: Default

%description license
license components for the gnome-autoar package.


%prep
%setup -q -n gnome-autoar-0.4.5
cd %{_builddir}/gnome-autoar-0.4.5
pushd ..
cp -a gnome-autoar-0.4.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1726758619
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-autoar
cp %{_builddir}/gnome-autoar-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-autoar/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GnomeAutoar-0.1.typelib
/usr/lib64/girepository-1.0/GnomeAutoarGtk-0.1.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/gnome-autoar-0/gnome-autoar/autoar-compressor.h
/usr/include/gnome-autoar-0/gnome-autoar/autoar-enum-types.h
/usr/include/gnome-autoar-0/gnome-autoar/autoar-extractor.h
/usr/include/gnome-autoar-0/gnome-autoar/autoar-format-filter.h
/usr/include/gnome-autoar-0/gnome-autoar/autoar-gtk-chooser.h
/usr/include/gnome-autoar-0/gnome-autoar/autoar-gtk.h
/usr/include/gnome-autoar-0/gnome-autoar/autoar-mime-types.h
/usr/include/gnome-autoar-0/gnome-autoar/autoar-misc.h
/usr/include/gnome-autoar-0/gnome-autoar/gnome-autoar.h
/usr/lib64/libgnome-autoar-0.so
/usr/lib64/libgnome-autoar-gtk-0.so
/usr/lib64/pkgconfig/gnome-autoar-0.pc
/usr/lib64/pkgconfig/gnome-autoar-gtk-0.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libgnome-autoar-0.so.0.2.1
/V3/usr/lib64/libgnome-autoar-gtk-0.so.0.2.1
/usr/lib64/libgnome-autoar-0.so.0
/usr/lib64/libgnome-autoar-0.so.0.2.1
/usr/lib64/libgnome-autoar-gtk-0.so.0
/usr/lib64/libgnome-autoar-gtk-0.so.0.2.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-autoar/01a6b4bf79aca9b556822601186afab86e8c4fbf
