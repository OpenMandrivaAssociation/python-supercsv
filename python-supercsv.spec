%define	module	supercsv
%define name	python-%{module}
%define version 0.1
%define release 2

Summary:	Python module for handling Unicode CSV files
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz
License:	PSF
Group:		Development/Python
Url:		http://pypi.python.org/pypi/supercsv/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	python-devel

%description
Python module for handling Unicode CSV files. Taken from the Python docs.

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc LICENSE README.rst


%changelog
* Sun Feb 26 2012 Lev Givon <lev@mandriva.org> 0.1-1
+ Revision: 780845
- imported package python-supercsv

