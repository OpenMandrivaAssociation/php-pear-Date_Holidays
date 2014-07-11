%define _class		Date
%define _subclass	Holidays
%define modname	%{_class}_%{_subclass}
%define pear_deps php-pear-Date_Holidays_Austria php-pear-Date_Holidays_Brazil php-pear-Date_Holidays_Denmark php-pear-Date_Holidays_Discordian php-pear-Date_Holidays_EnglandWales php-pear-Date_Holidays_Germany php-pear-Date_Holidays_Iceland php-pear-Date_Holidays_Ireland php-pear-Date_Holidays_Italy php-pear-Date_Holidays_Japan php-pear-Date_Holidays_Netherlands php-pear-Date_Holidays_Norway php-pear-Date_Holidays_PHPdotNet php-pear-Date_Holidays_Romania php-pear-Date_Holidays_Slovenia php-pear-Date_Holidays_Sweden php-pear-Date_Holidays_UNO php-pear-Date_Holidays_USA php-pear-Date_Holidays_Ukraine

Summary:	Driver based class to calculate holidays
Name:		php-pear-%{modname}
Version:	0.21.8
Release:	7
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/Date_Holidays/
Source0:	http://download.pear.php.net/package/Date_Holidays-%{version}.tgz
BuildArch:	noarch
BuildRequires:  php-pear
Requires(post,preun):	php-pear
Requires:	php-pear
Suggests:	%{pear_deps}

%description
Date_Holidays helps you calculating the dates and titles of
holidays and other special celebrations. The calculation is
driver-based so it is easy to add new drivers that calculate
a country's holidays. The methods of the class can be used
to get a holiday's date and title in various languages.

%prep
%setup -qc
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{modname}-%{version}/examples
%{_bindir}/pear-dh-*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{modname}
%{_datadir}/pear/packages/%{modname}.xml

