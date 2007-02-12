Summary:	Type1 font metrics converters
Summary(pl.UTF-8):   Konwertery metryk fontów Type1
Name:		afm2pfm
Version:	1.0
Release:	8
License:	GPL
Group:		Applications
Source0:	ftp://sunsite.unc.edu/pub/linux/utils/text/%{name}.tar.gz
# Source0-md5:	b7598f46b7596c5e3e96ee11fd0a9268
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package containst two converters:
- pfm2afm - converts Windows .pfm files to .afm files,
- afm2pfm - convert Adobe .afm file to MS-Windows binary .pfm file.

%description -l pl.UTF-8
Programy do konwersji metryk fontów Type1 między formatami MS Windows
(.pfm) a Adobe (.afm):
- pfm2afm - konwertuje pliki .pfm do .afm,
- afm2pfm - konwertuje pliki .afm do .pfm.

%prep
%setup -q -n afm2pfm

%build
%{__cc} %{rpmcflags} %{rpmldflags} -o afm2pfm afm2pfm.c
%{__cc} %{rpmcflags} %{rpmldflags} -o pfm2afm pfm2afm.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install afm2pfm pfm2afm $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme README
%attr(755,root,root) %{_bindir}/*
