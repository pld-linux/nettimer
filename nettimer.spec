# TODO:
# - make specs with required libdpcap and libkl
#   (http://mosquitonet.stanford.edu/~laik/projects/nettimer/#Download)
Summary:	Nettimer is a bandwidth measurement tool.
Name:		nettimer
Version:	2.3.8
Release:        0.1
License:	GPL
Group:		Applications/Networking
Source0:	http://mosquitonet.stanford.edu/~laik/projects/nettimer/%{name}-%{version}.tar.gz
# Source0-md5:	8fa4e2669d805a834f7f819d73d03d5a
URL:		http://mosquitonet.stanford.edu/~laik/projects/nettimer/
BuildRequires:	autoconf
BuildRequires:	automake
#BuildRequires:	libdpcap-devel
#BuildRequires:	libkl-devel
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nettimer is a tool to do network bandwidth measurement. It can
actively probe or passively listen. It can listen at multiple points
in the network. It can run in real time or analyze traces.

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1

install %{name} $RPM_BUILD_ROOT%{_sbindir}
install %{name}.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO doc/*.html
%attr(4755,root,root) %{_sbindir}/%{name}
%{_mandir}/man8/*
