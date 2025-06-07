#
# Conditional build:
%bcond_with	tests	# unit tests (only with package already installed)
%bcond_with	python2 # CPython 2.x module (lal module obsolete)
%bcond_without	python3 # CPython 3.x module

Summary:	Python LIGO Light-Weight XML I/O Library
Summary(pl.UTF-8):	Pythonowa lekka biblioteka we/wy LILO Light-Weight XML
Name:		python3-ligolw
Version:	1.8.3
Release:	3
License:	GPL v2+
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ligo-lw/
Source0:	https://files.pythonhosted.org/packages/source/i/igwn-ligolw/gwn-ligolw-%{version}.tar.gz
# Source0-md5:	ce0192d292fe666c705a3cf4e8bfc4f3
Patch0:		%{name}-setuptools.patch
URL:		https://pypi.org/project/ligo-lw/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-PyYAML
BuildRequires:	python-dateutil
BuildRequires:	python-lal
BuildRequires:	python-ligo-segments
BuildRequires:	python-lscsoft-glue
BuildRequires:	python-numpy
BuildRequires:	python-six
BuildRequires:	python-tqdm
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-PyYAML
BuildRequires:	python3-dateutil
BuildRequires:	python3-lal
BuildRequires:	python3-ligo-segments
BuildRequires:	python3-lscsoft-glue
BuildRequires:	python3-numpy
BuildRequires:	python3-six
BuildRequires:	python3-tqdm
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The LIGO Light-Weight XML format is used extensively by compact object
detection pipeline and associated tool sets. This package provides a
Python I/O library for reading, writing, and interacting with
documents in this format.

%description -l pl.UTF-8
Format LIGO Light-Weight XML jest używany intensywnie przez potok
wykrywania obiektów i powiązane z nim narzędzia. Ten pakiet dostarcza
bibliotekę we/wy Pythona do odczytu, zapisu i operacji na dokumentach
w tym formacie.

%package -n python3-ligo-lw
Summary:	Python LIGO Light-Weight XML I/O Library
Summary(pl.UTF-8):	Pythonowa lekka biblioteka we/wy XML LIGO
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-ligo-lw
The LIGO Light-Weight XML format is used extensively by compact object
detection pipeline and associated tool sets. This package provides a
Python I/O library for reading, writing, and interacting with
documents in this format.

%description -n python3-ligo-lw -l pl.UTF-8
Format LIGO Light-Weight XML jest używany intensywnie przez potok
wykrywania obiektów i powiązane z nim narzędzia. Ten pakiet dostarcza
bibliotekę we/wy Pythona do odczytu, zapisu i operacji na dokumentach
w tym formacie.

%prep
%setup -q
%patch -P 0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
PATH=$(readlink -f build-2/scripts-*):$PATH \
PYTHONPATH=$(readlink -f build-2/lib.*) \
%{__make} -C test check \
	PYTHON=%{__python}
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PATH=$(readlink -f build-3/scripts-*):$PATH \
PYTHONPATH=$(readlink -f build-3/lib.*) \
%{__make} -C test check \
	PYTHON=%{__python3}
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

for f in $RPM_BUILD_ROOT%{_bindir}/* ; do
	%{__mv} "$f" "${f}-2"
done

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ligolw_add-2
%attr(755,root,root) %{_bindir}/ligolw_cut-2
%attr(755,root,root) %{_bindir}/ligolw_no_ilwdchar-2
%attr(755,root,root) %{_bindir}/ligolw_print-2
%attr(755,root,root) %{_bindir}/ligolw_run_sqlite-2
%attr(755,root,root) %{_bindir}/ligolw_segments-2
%attr(755,root,root) %{_bindir}/ligolw_sqlite-2
%dir %{py_sitedir}/ligo
%dir %{py_sitedir}/ligo/lw
%attr(755,root,root) %{py_sitedir}/ligo/lw/*.so
%{py_sitedir}/ligo/lw/*.py[co]
%dir %{py_sitedir}/ligo/lw/utils
%{py_sitedir}/ligo/lw/utils/*.py[co]
%{py_sitedir}/python_ligo_lw-%{version}-py*.egg-info
%{py_sitedir}/python_ligo_lw-%{version}-py*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-ligo-lw
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ligolw_add
%attr(755,root,root) %{_bindir}/ligolw_cut
%attr(755,root,root) %{_bindir}/ligolw_no_ilwdchar
%attr(755,root,root) %{_bindir}/ligolw_print
%attr(755,root,root) %{_bindir}/ligolw_run_sqlite
%attr(755,root,root) %{_bindir}/ligolw_segments
%attr(755,root,root) %{_bindir}/ligolw_sqlite
%dir %{py3_sitedir}/ligo
%dir %{py3_sitedir}/ligo/lw
%attr(755,root,root) %{py3_sitedir}/ligo/lw/*.so
%{py3_sitedir}/ligo/lw/*.py
%{py3_sitedir}/ligo/lw/__pycache__
%dir %{py3_sitedir}/ligo/lw/utils
%{py3_sitedir}/ligo/lw/utils/*.py
%{py3_sitedir}/ligo/lw/utils/__pycache__
%{py3_sitedir}/python_ligo_lw-%{version}-py*.egg-info
%{py3_sitedir}/python_ligo_lw-%{version}-py*-nspkg.pth
%endif
