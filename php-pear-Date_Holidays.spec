%define		_class		Date
%define		_subclass	Holidays
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.21.5
Release:	%mkrel 2
Summary:	Driver based class to calculate holidays
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Date_Holidays/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
%define pear_deps php-pear-Date_Holidays_Austria php-pear-Date_Holidays_Brazil php-pear-Date_Holidays_Denmark php-pear-Date_Holidays_Discordian php-pear-Date_Holidays_EnglandWales php-pear-Date_Holidays_Germany php-pear-Date_Holidays_Iceland php-pear-Date_Holidays_Ireland php-pear-Date_Holidays_Italy php-pear-Date_Holidays_Japan php-pear-Date_Holidays_Netherlands php-pear-Date_Holidays_Norway php-pear-Date_Holidays_PHPdotNet php-pear-Date_Holidays_Romania php-pear-Date_Holidays_Slovenia php-pear-Date_Holidays_Sweden php-pear-Date_Holidays_UNO php-pear-Date_Holidays_USA php-pear-Date_Holidays_Ukraine
%if %mdkversion >= 200900
Suggests:	%{pear_deps}
%else
Requires:	%{pear_deps}
%endif
BuildArch:	noarch
BuildRequires:  php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Date_Holidays helps you calculating the dates and titles of
holidays and other special celebrations. The calculation is
driver-based so it is easy to add new drivers that calculate
a country's holidays. The methods of the class can be used
to get a holiday's date and title in various languages.


%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/examples
%{_bindir}/pear-dh-*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml
