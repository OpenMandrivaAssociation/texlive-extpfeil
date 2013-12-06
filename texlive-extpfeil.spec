# revision 16243
# category Package
# catalog-ctan /macros/latex/contrib/extpfeil
# catalog-date 2009-10-31 20:51:21 +0100
# catalog-license lppl1.3
# catalog-version 0.4
Name:		texlive-extpfeil
Version:	0.4
Release:	3
Summary:	Extensible arrows in mathematics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/extpfeil
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/extpfeil.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/extpfeil.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/extpfeil.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4-2
+ Revision: 751748
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.4-1
+ Revision: 718405
- texlive-extpfeil
- texlive-extpfeil
- texlive-extpfeil
- texlive-extpfeil

