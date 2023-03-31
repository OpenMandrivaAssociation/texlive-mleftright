Name:		texlive-mleftright
Version:	53021
Release:	2
Summary:	Variants of delimiters that act as maths open/close
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mleftright
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mleftright.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mleftright.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mleftright.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines variants \mleft and \mright of \left and
\right, that make the delimiters act as \mathopen and
\mathclose. These commands address spacing difficulties in
subformulas.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/mleftright
%{_texmfdistdir}/tex/generic/mleftright
%doc %{_texmfdistdir}/doc/latex/mleftright

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
