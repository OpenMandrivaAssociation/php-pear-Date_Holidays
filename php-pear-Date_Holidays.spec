%define		_class		Date
%define		_subclass	Holidays
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - driver based class to calculate holidays
Name:		php-pear-%{_pearname}
Version:	0.17.1
Release:	%mkrel 2
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
URL:		http://pear.php.net/package/Date_Holidays/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Date_Holidays helps you calculating the dates and titles of
holidays and other special celebrations. The calculation is
driver-based so it is easy to add new drivers that calculate
a country's holidays. The methods of the class can be used
to get a holiday's date and title in various languages.

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/{Driver,Filter,lang/{Christian,Germany,Sweden,UNO,USA}}

install %{_pearname}-%{version}/*.php %{buildroot}%{_datadir}/pear/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/Driver/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Driver
install %{_pearname}-%{version}/%{_subclass}/Filter/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Filter
install %{_pearname}-%{version}/lang/Christian/* %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/lang/Christian
install %{_pearname}-%{version}/lang/Germany/* %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/lang/Germany
install %{_pearname}-%{version}/lang/Sweden/* %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/lang/Sweden
install %{_pearname}-%{version}/lang/UNO/* %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/lang/UNO
install %{_pearname}-%{version}/lang/USA/* %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/lang/USA

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples
%doc %{_pearname}-%{version}/pear-dh-compile-translationfile
%doc %{_pearname}-%{version}/pear-dh-ini2xml
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/%{_class}/%{_subclass}
%{_datadir}/pear/packages/%{_pearname}.xml
