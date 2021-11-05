Name:		__NAME__
Version:	__SOFTWARE_VERSION__
Release:	__RELEASE_VERSION__
Summary:	__DESC__

License:	__LICENSE__

Requires:	bash, python

##############################################################################
# description macro to include information in the RPM header
##############################################################################
%description
__DESC__


##############################################################################
# install macro to prepare packaged files in the %{buildroot} directory
##############################################################################
%install

echo "Laying out the package's files and directories.. "
mkdir -p %{buildroot}
cp -rf %{package_files}/* %{buildroot}


##############################################################################
# pre macro to run before the install scripts run
##############################################################################
%pre

echo "Executing Pre-Installation macro.. "


##############################################################################
# post macro to execute after installation
##############################################################################
%post

echo "Executing Post-Installation macro.. "


##############################################################################
# preun macro to run prior to uninstallation
##############################################################################
%preun

echo "Executing Pre-Uninstallation macro.. "


##############################################################################
# postun to execute after uninstallation 
##############################################################################
%postun

echo "Executing Post-Uninstallation macro.. "


##############################################################################
# files macro defines what are the contents of the package
# 
# The files will be installed as the below structure on the target system
##############################################################################
%files
%defattr(755,root,root)
%doc

/opt/zlig/hello.sh


##############################################################################
# changelog macro to comment on package revisions (date format important)
##############################################################################
%changelog
* Fri Nov 5 2021 zlig <noreply@gdevnet.com>
- Initial build
