%global debug_package %{nil}
# 1.16 errors; 1.17 untested; 1.18 is fine
%if 0%{?rhel} >= 7 || 0%{?fedora} >= 36
    %global _fetch_go 0
%else
    %global _fetch_go 1
%endif

Name: simple-tls
Version: 0.8.0
Release: 1%{?dist}
Summary: A simple TCP repeater that adds a layer of TLS wrapping
License: GPLv3
URL: https://github.com/IrineSistiana/simple-tls
Source0: %{url}/archive/v%{version}.tar.gz
BuildRequires: gcc git make
%if ! %{_fetch_go}
BuildRequires: golang
%endif

%description
simple-tls is a simple TCP connection repeater. It can wrap the original stream
with a layer of TLS encryption. gRPC protocol is supported.

%prep
%autosetup

%build
%if %{_fetch_go}
    VER="$(curl -fLsS https://golang.org/VERSION?m=text)"
    case "%{_arch}" in
        x86_64)
            ARCH=amd64
            ;;
        aarch64)
            ARCH=arm64
            ;;
        *)
            echo "Unexpected processor architecture."
            exit 1
            ;;
    esac
    FILE="${VER}.linux-${ARCH}.tar.gz"

    curl -fLOsS "https://go.dev/dl/${FILE}"
    tar -xf "${FILE}"
    export PATH="go/bin:${PATH}" # this is fine as long as we don't chdir
%endif

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
* Wed Dec 21 2022 spyophobia - 0.8.0-1
- Release 0.8.0
