Name: SMHI-titan-lib
Version: 0.2
Release: 0
Summary: Library of automatic quality control routines for weather observations
License: SMHI/MetNo
Group: Applications/System
Requires: swig, boost, gsl, netcdf, armadillo
Requires: python3, python3-scipy, python3-numpy, python3-six

%define AppOwner        gridpp
%define AppGroup        gridppg
%define AppOwnerTst     gridpp.t
%define AppGroupTst     gridppgt
%define AppOwnerUtv     gridpp.u
%define AppGroupUtv     gridppgu
%define INSTALLDIR %{_libdir}/python3.6/site-packages/smhi_titan_lib
%define _unpackaged_files_terminate_build 0

%description

Titanlib is a library of automatic quality control routines for weather observations. 
It emphases spatial checks and is suitable for use with dense observation networks, 
such as citizen weather observations. It is written in C++ and has bindings for python and R. 
The library consists of a set of functions that perform tests on data.

Titanlib is currently under active development and the current version is a prototype for testing. 
Feedback is welcome, either by using the issue tracker in Github, 
or by contacting Thomas Nipen (thomasn@met.no).

This is an SMHI's adaptation of MetNO's library

%build
mkdir ${RPM_SOURCE_DIR}/build
cd ${RPM_SOURCE_DIR}/build
cmake -BUILD_R=OFF ..
export CFLAGS="-I /usr/lib64/python3.6/site-packages/numpy/core/include $CFLAGS"
make

%install

mkdir -p $RPM_BUILD_ROOT%{INSTALLDIR}

cp ${RPM_SOURCE_DIR}/build/extras/SWIG/python/titanlib.py $RPM_BUILD_ROOT%{INSTALLDIR}
cp ${RPM_SOURCE_DIR}/build/extras/SWIG/python/_titanlib.so $RPM_BUILD_ROOT%{INSTALLDIR}

%postun

%clean

rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_SOURCE_DIR

%files
%{INSTALLDIR}/*.py
%{INSTALLDIR}/_titanlib.so
%{INSTALLDIR}/__pycache__/*.pyc

%defattr(755,root,root,755)
%attr(644,root,root) %{INSTALLDIR}/*.py

%changelog
* Wed Feb 02 2021 Aliaksandr Rahachou <aliaksandr.rahachou@hiq.se> - 0.2-0
- First variant, TitanLib 0.2.0