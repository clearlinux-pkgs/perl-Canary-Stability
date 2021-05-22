#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Canary-Stability
Version  : 2013
Release  : 19
URL      : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Canary-Stability-2013.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Canary-Stability-2013.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Canary-Stability-license = %{version}-%{release}
Requires: perl-Canary-Stability-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Canary::Stability - canary to check perl compatibility for schmorp's
modules

%package dev
Summary: dev components for the perl-Canary-Stability package.
Group: Development
Provides: perl-Canary-Stability-devel = %{version}-%{release}
Requires: perl-Canary-Stability = %{version}-%{release}

%description dev
dev components for the perl-Canary-Stability package.


%package license
Summary: license components for the perl-Canary-Stability package.
Group: Default

%description license
license components for the perl-Canary-Stability package.


%package perl
Summary: perl components for the perl-Canary-Stability package.
Group: Default
Requires: perl-Canary-Stability = %{version}-%{release}

%description perl
perl components for the perl-Canary-Stability package.


%prep
%setup -q -n Canary-Stability-2013
cd %{_builddir}/Canary-Stability-2013

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Canary-Stability
cp %{_builddir}/Canary-Stability-2013/COPYING %{buildroot}/usr/share/package-licenses/perl-Canary-Stability/9a56f3b919dfc8fced3803e165a2e38de62646e5
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Canary::Stability.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Canary-Stability/9a56f3b919dfc8fced3803e165a2e38de62646e5

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Canary/Stability.pm
