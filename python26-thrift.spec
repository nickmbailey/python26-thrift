Name:		python26-thrift
Version:	0.7.0
Release:	2
Summary:	Python bindings for the Apache Thrift RPC system

Group:		Development/Libraries
License:	ASL 2.0
Url:		http://thrift.apache.org
Source0:	http://www.apache.org/dist/thrift/%{version}/thrift-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	%{_libdir}/libpython2.6.so
Requires:	/usr/bin/python2.6

%global __python python2.6
%global python26_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(True))")

# Turn off the brp-python-bytecompile script, cause in RHEL 5 it only believes in python2.4
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

%description
Thrift is a software framework for the development of reliable and
performant communication and data serialization. It combines a software
stack with a code generation engine to build services that operate
seamlessly across a number of different development languages.

This package provides the Python bindings for Thrift.

%prep
%setup -q -n thrift-%{version}

%build
cd lib/py && %{__python} setup.py build

%install
rm -rf %{buildroot}

cd lib/py && %{__python} setup.py install -c -O1 --skip-build --root=%{buildroot}
#strip %{buildroot}%{python26_sitelib}/thrift/protocol/*.so

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README LICENSE
%{python26_sitelib}/thrift/
%{python26_sitelib}/Thrift*.egg-info
