Summary:	Type1 font metrics converters
Summary(pl):	Konwertery metryk fontów Type1
Name:		afm2pfm
Version:	1.0
Release:	8
License:	GPL
Group:		Applications
Group(de):	Applikationen
Group(pl):	Aplikacje
Source0:	ftp://sunsite.unc.edu/pub/linux/utils/text/%{name}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pfm2afm - convert Windows .pfm files to .afm files
afm2pfm - convert Adobe .afm file to MS-Windows binary .pfm file

%description -l pl
Programy do konwersji metryk fontów Type1 miêdzy formatami MS Windows
(.pfm) a Adobe (.afm).
pfm2afm - konwertuje pliki .pfm do .afm
afm2pfm - konwertuje pliki .afm do .pfm

%prep
%setup -q -n afm2pfm

%build
%{__cc} %{rpmcflags} %{rpmldflags} -o afm2pfm afm2pfm.c
%{__cc} %{rpmcflags} %{rpmldflags} -o pfm2afm pfm2afm.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install afm2pfm pfm2afm $RPM_BUILD_ROOT%{_bindir}

gzip -9nf readme README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
