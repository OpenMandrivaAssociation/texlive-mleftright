%global tl_name mleftright
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Variants of delimiters that act as maths open/close
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mleftright
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mleftright.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mleftright.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mleftright.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines variants \mleft and \mright of \left and \right,
that make the delimiters act as \mathopen and \mathclose. These commands
address spacing difficulties in subformulas.

