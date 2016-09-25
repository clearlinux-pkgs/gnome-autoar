#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-autoar
Version  : 0.1.1
Release  : 1
URL      : https://download.gnome.org/sources/gnome-autoar/0.1/gnome-autoar-0.1.1.tar.xz
Source0  : https://download.gnome.org/sources/gnome-autoar/0.1/gnome-autoar-0.1.1.tar.xz
Summary  : Archives integration support for GNOME
Group    : Development/Tools
License  : LGPL-2.1
Requires: gnome-autoar-lib
Requires: gnome-autoar-data
Requires: gnome-autoar-doc
BuildRequires : docbook-xml
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libarchive)

%description
No detailed description available

%package data
Summary: data components for the gnome-autoar package.
Group: Data

%description data
data components for the gnome-autoar package.


%package dev
Summary: dev components for the gnome-autoar package.
Group: Development
Requires: gnome-autoar-lib
Requires: gnome-autoar-data
Provides: gnome-autoar-devel

%description dev
dev components for the gnome-autoar package.


%package doc
Summary: doc components for the gnome-autoar package.
Group: Documentation

%description doc
doc components for the gnome-autoar package.


%package lib
Summary: lib components for the gnome-autoar package.
Group: Libraries
Requires: gnome-autoar-data

%description lib
lib components for the gnome-autoar package.


%prep
%setup -q -n gnome-autoar-0.1.1

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/gir-1.0/GnomeAutoar-0.1.gir
/usr/share/gir-1.0/GnomeAutoarGtk-0.1.gir
/usr/share/glib-2.0/schemas/org.gnome.desktop.archives.enums.xml
/usr/share/glib-2.0/schemas/org.gnome.desktop.archives.gschema.xml

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
/usr/lib64/*.so
/usr/lib64/girepository-1.0/GnomeAutoar-0.1.typelib
/usr/lib64/girepository-1.0/GnomeAutoarGtk-0.1.typelib
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/gnome-autoar/AutoarCompressor.html
/usr/share/gtk-doc/html/gnome-autoar/AutoarExtractor.html
/usr/share/gtk-doc/html/gnome-autoar/annotation-glossary.html
/usr/share/gtk-doc/html/gnome-autoar/api-index-full.html
/usr/share/gtk-doc/html/gnome-autoar/ch01.html
/usr/share/gtk-doc/html/gnome-autoar/ch02.html
/usr/share/gtk-doc/html/gnome-autoar/ch03.html
/usr/share/gtk-doc/html/gnome-autoar/deprecated-api-index.html
/usr/share/gtk-doc/html/gnome-autoar/gnome-autoar-autoar-format-filter.html
/usr/share/gtk-doc/html/gnome-autoar/gnome-autoar-autoar-gtk-chooser.html
/usr/share/gtk-doc/html/gnome-autoar/gnome-autoar-autoar-misc.html
/usr/share/gtk-doc/html/gnome-autoar/gnome-autoar.devhelp2
/usr/share/gtk-doc/html/gnome-autoar/home.png
/usr/share/gtk-doc/html/gnome-autoar/index.html
/usr/share/gtk-doc/html/gnome-autoar/left-insensitive.png
/usr/share/gtk-doc/html/gnome-autoar/left.png
/usr/share/gtk-doc/html/gnome-autoar/object-tree.html
/usr/share/gtk-doc/html/gnome-autoar/right-insensitive.png
/usr/share/gtk-doc/html/gnome-autoar/right.png
/usr/share/gtk-doc/html/gnome-autoar/style.css
/usr/share/gtk-doc/html/gnome-autoar/up-insensitive.png
/usr/share/gtk-doc/html/gnome-autoar/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
