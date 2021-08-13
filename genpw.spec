Name:           genpw
Version:        1.0.0
Release:        1
Summary:        Generate strong passwords directly from the command line.
BuildArch:      noarch

License:        AGPL-3.0
#URL:
Source0:        %{name}-%{version}.tar.gz

#BuildRequires:  
Requires:       bash

%description
Generate strong passwords directly from the command line.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp genpw.sh $RPM_BUILD_ROOT/%{_bindir}/genpw
chmod +x $RPM_BUILD_ROOT/%{_bindir}/genpw

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/genpw

%changelog
* Fri Aug 13 2021 Marcel <34819524+MarcelCoding@users.noreply.github.com> 1.0.0-1
- Initial Version
