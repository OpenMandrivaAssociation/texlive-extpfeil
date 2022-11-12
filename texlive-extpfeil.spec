Name:		texlive-extpfeil
Version:	16243
Release:	1
Summary:	Extensible arrows in mathematics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/extpfeil
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/extpfeil.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/extpfeil.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/extpfeil.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The exptfeil package provides some more extensible arrows
(usable in the same way as \xleftarrow from amsmath), and a
command to simply create new ones.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/extpfeil/extpfeil.sty
%doc %{_texmfdistdir}/doc/latex/extpfeil/README
%doc %{_texmfdistdir}/doc/latex/extpfeil/extpfeil.pdf
#- source
%doc %{_texmfdistdir}/source/latex/extpfeil/extpfeil.dtx
%doc %{_texmfdistdir}/source/latex/extpfeil/extpfeil.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
