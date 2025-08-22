Name: distro-loads
Version: 1.0
Release:        %autorelease
Summary: Download ISOs over http from CLI

License: GPLv3
Source0: distroloads

BuildRequires: make

%description
Download ISOs over http from CLI


%install
mkdir -p %{buildroot}/usr/local/bin/

install -m 755 %{_sourcedir}/distroloads %{buildroot}/usr/local/bin/%{name} 

%files
%attr(755, root, root) /usr/local/bin/%{name}

