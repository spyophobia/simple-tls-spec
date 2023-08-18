%global debug_package %{nil}

Name: simple-tls
Version: 0.8.0
Release: 2%{?dist}
Summary: A simple TCP repeater that adds a layer of TLS wrapping
License: GPLv3
URL: https://github.com/IrineSistiana/simple-tls
Source0: %{url}/archive/v%{version}.tar.gz
BuildRequires: gcc git golang make

%description
simple-tls is a simple TCP connection repeater. It can wrap the original stream
with a layer of TLS encryption. gRPC protocol is supported.

%prep
%autosetup

%build
go build -ldflags "-X main.version=%{version}"

%check
# nothing for now

%install
# bin
install -Dpm 755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Fri Aug 18 2023 spyophobia - 0.8.0-2
- Rebuild using updated Go binaries from official repo

* Wed Dec 21 2022 spyophobia - 0.8.0-1
- Release 0.8.0
