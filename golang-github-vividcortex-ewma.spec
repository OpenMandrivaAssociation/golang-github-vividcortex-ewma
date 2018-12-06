# Run tests in check section
%bcond_without check

%global goipath         github.com/VividCortex/ewma
Version:                1.1.1

%global common_description %{expand:
Exponentially Weighted Moving Average algorithms for Go.}

%gometa

Name:    %{goname}
Release: 5%{?dist}
Summary: Exponentially Weighted Moving Average algorithms for Go
License: MIT
URL:     %{gourl}
Source:  %{gosource}

# https://github.com/VividCortex/ewma/pull/17
Patch0: 0001-Fix-wrong-format-type-in-Errorf.patch

%description
%{common_description}


%package    devel
Summary:    %{summary}
BuildArch:  noarch

Provides: golang-github-VividCortex-ewma-devel = %{version}-%{release}
Obsoletes: golang-github-VividCortex-ewma-devel < 1.1.1-4
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%gosetup -q
%patch0 -p1


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 09 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.1-4
- Update with the new Go packaging

* Tue Feb 13 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.1-3
- Added patch for fixing wrong format type in Errorf

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jul 24 2017 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.1-1
- First package for Fedora

