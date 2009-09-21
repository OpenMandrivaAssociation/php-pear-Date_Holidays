%define		_class		Date
%define		_subclass	Holidays
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	Driver based class to calculate holidays
Name:		php-pear-%{_pearname}
Version:	0.21.2
Release:	%mkrel 2
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
URL:		http://pear.php.net/package/Date_Holidays/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Suggests:	php-pear-Date_Holidays_Austria
Suggests:	php-pear-Date_Holidays_Brazil
Suggests:	php-pear-Date_Holidays_Denmark
Suggests:	php-pear-Date_Holidays_Discordian
Suggests:	php-pear-Date_Holidays_EnglandWales
Suggests:	php-pear-Date_Holidays_Germany
Suggests:	php-pear-Date_Holidays_Iceland
Suggests:	php-pear-Date_Holidays_Ireland
Suggests:	php-pear-Date_Holidays_Italy
Suggests:	php-pear-Date_Holidays_Japan
Suggests:	php-pear-Date_Holidays_Netherlands
Suggests:	php-pear-Date_Holidays_Norway
Suggests:	php-pear-Date_Holidays_PHPdotNet
Suggests:	php-pear-Date_Holidays_Romania
Suggests:	php-pear-Date_Holidays_Slovenia
Suggests:	php-pear-Date_Holidays_Sweden
Suggests:	php-pear-Date_Holidays_Ukraine
Suggests:	php-pear-Date_Holidays_UNO
Suggests:	php-pear-Date_Holidays_USA
BuildArch:	noarch
BuildRequires:  php-pear
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
cp package.xml %{_pearname}-%{version}

%install
rm -rf %{buildroot}

cd %{_pearname}-%{version}
%{_bindir}/pear install --nodeps --packagingroot %{buildroot} package.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

install -d -m 755 %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/pear/docs %{buildroot}%{_docdir}/%{name}

rm -rf %{buildroot}%{_datadir}/pear/tests

install -d -m 755 %{buildroot}%{_datadir}/pear/packages
install -m 644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

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
%defattr(-,root,root)
%doc %{_docdir}/%{name}
%{_bindir}/pear-dh-*
%{_datadir}/pear/data/Date_Holidays
%{_datadir}/pear/packages/%{_pearname}.xml
%{_datadir}/pear/Date/Holidays*
