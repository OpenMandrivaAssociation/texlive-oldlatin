# revision 17932
# category Package
# catalog-ctan /fonts/gothic/oldlatin
# catalog-date 2010-04-29 07:59:03 +0200
# catalog-license lppl
# catalog-version 1.00
Name:		texlive-oldlatin
Version:	1.00
Release:	6
Summary:	Compute Modern like font with long s
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/gothic/oldlatin
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oldlatin.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oldlatin.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Metafont sources modified from Computer Modern in order to
generate "long s" which was used in old text.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/oldlatin/olb10.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olbx10.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olbx12.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olbx5.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olbx6.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olbx7.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olbx8.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olbx9.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olbxsl10.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/oldunh10.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olff10.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olfib8.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olr10.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olr10s.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olr12.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olr17.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olr5.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olr6.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olr7.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olr8.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olr9.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olsl10.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olsl12.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olsl8.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olsl9.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olsltt10.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olss10.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olss12.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olss17.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olss8.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olss9.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olssbx10.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olssdc10.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olssi10.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olssi12.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olssi17.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olssi8.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olssi9.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olssq8.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olssqi8.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/oltt10.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/oltt12.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/oltt8.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/oltt9.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/olvtt10.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/oroman.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/oromanl.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/oromlig.mf
%{_texmfdistdir}/fonts/source/public/oldlatin/oromligs.mf
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olb10.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olbx12.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olbx5.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olbx6.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olbx7.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olbx8.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olbx9.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olbxsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/oldunh10.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olff10.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olfib8.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olr10.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olr12.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olr17.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olr5.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olr6.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olr7.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olr8.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olr9.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olsl12.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olsl8.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olsl9.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olsltt10.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olss10.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olss12.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olss17.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olss8.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olss9.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olssbx10.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olssdc10.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olssi10.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olssi12.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olssi17.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olssi8.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olssi9.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olssq8.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olssqi8.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/oltt10.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/oltt12.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/oltt8.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/oltt9.tfm
%{_texmfdistdir}/fonts/tfm/public/oldlatin/olvtt10.tfm
%doc %{_texmfdistdir}/doc/fonts/oldlatin/README
%doc %{_texmfdistdir}/doc/fonts/oldlatin/oldlatin.pdf
%doc %{_texmfdistdir}/doc/fonts/oldlatin/oldlatin.tex
%doc %{_texmfdistdir}/doc/fonts/oldlatin/test_alphabet.tex
%doc %{_texmfdistdir}/doc/fonts/oldlatin/test_ol_all.pdf
%doc %{_texmfdistdir}/doc/fonts/oldlatin/test_ol_all.tex
%doc %{_texmfdistdir}/doc/fonts/oldlatin/test_ol_bf.pdf
%doc %{_texmfdistdir}/doc/fonts/oldlatin/test_ol_bf.tex
%doc %{_texmfdistdir}/doc/fonts/oldlatin/test_ol_rm.pdf
%doc %{_texmfdistdir}/doc/fonts/oldlatin/test_ol_rm.tex
%doc %{_texmfdistdir}/doc/fonts/oldlatin/test_ol_sl.pdf
%doc %{_texmfdistdir}/doc/fonts/oldlatin/test_ol_sl.tex
%doc %{_texmfdistdir}/doc/fonts/oldlatin/test_ol_ss.pdf
%doc %{_texmfdistdir}/doc/fonts/oldlatin/test_ol_ss.tex
%doc %{_texmfdistdir}/doc/fonts/oldlatin/test_ol_tt.pdf
%doc %{_texmfdistdir}/doc/fonts/oldlatin/test_ol_tt.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.00-2
+ Revision: 754508
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.00-1
+ Revision: 719157
- texlive-oldlatin
- texlive-oldlatin
- texlive-oldlatin
- texlive-oldlatin

