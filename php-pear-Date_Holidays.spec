%define		_class		Date
%define		_subclass	Holidays
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.21.5
Release:	%mkrel 4
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

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/examples
%{_bindir}/pear-dh-*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.21.5-3mdv2012.0
+ Revision: 741754
- fix major breakage by careless packager

* Wed Dec 14 2011 Oden Eriksson <oeriksson@mandriva.com> 0.21.5-2
+ Revision: 741011
- make it backportable

* Mon Nov 28 2011 Oden Eriksson <oeriksson@mandriva.com> 0.21.5-1
+ Revision: 735161
- new version

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.21.2-5
+ Revision: 667494
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.21.2-4mdv2011.0
+ Revision: 607096
- rebuild

* Wed Dec 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.21.2-3mdv2010.1
+ Revision: 479265
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.21.2-2mdv2010.0
+ Revision: 446964
- use pear installer
- spec cleanup

* Mon Apr 20 2009 Raphaël Gertz <rapsys@mandriva.org> 0.21.2-1mdv2009.1
+ Revision: 368156
- Update to 0.21.2 version

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 0.17.1-4mdv2009.1
+ Revision: 321809
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.17.1-3mdv2009.0
+ Revision: 224705
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.17.1-2mdv2008.1
+ Revision: 178506
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 23 2007 Oden Eriksson <oeriksson@mandriva.com> 0.17.1-1mdv2008.0
+ Revision: 54558
- 0.17.1

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.17.0-1mdv2008.0
+ Revision: 15535
- 0.17.0


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.16.0-1mdv2007.0
+ Revision: 81086
- Import php-pear-Date_Holidays

* Sat Apr 08 2006 Oden Eriksson <oeriksson@mandriva.com> 0.16.0-1mdk
- 0.16.0

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.15.1-1mdk
- 0.15.1
- new group (Development/PHP)

* Sun Nov 06 2005 Oden Eriksson <oeriksson@mandriva.com> 0.14.0-1mdk
- 0.14.0

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.13.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.13.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.13.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.13.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.13.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.13.0-1mdk
- initial Mandriva package (PLD import)

