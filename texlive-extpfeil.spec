%global tl_name extpfeil
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4
Release:	%{tl_revision}.1
Summary:	Extensible arrows in mathematics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/extpfeil
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/extpfeil.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/extpfeil.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/extpfeil.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides some more extensible arrows (usable in the same way
as \xleftarrow from amsmath), and a simple command to create new ones.

