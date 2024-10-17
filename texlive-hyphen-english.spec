Name:		texlive-hyphen-english
Version:	58609
Release:	2
Summary:	English hyphenation patterns
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-english.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Additional hyphenation patterns for American and British
English in ASCII encoding.  The American English patterns
(usenglishmax) greatly extend the standard patterns from Knuth
to find many additional hyphenation points.  British English
hyphenation is completely different from US English, so has its
own set of patterns.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/hyph-utf8/loadhyph/*
%{_texmfdistdir}/tex/generic/hyph-utf8/patterns/*/*
%_texmf_language_dat_d/hyphen-english
%_texmf_language_def_d/hyphen-english
%_texmf_language_lua_d/hyphen-english

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}

mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-english <<EOF
\%% from hyphen-english:
ukenglish loadhyph-en-gb.tex
=british
=UKenglish
usenglishmax loadhyph-en-us.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-english
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-english <<EOF
\%% from hyphen-english:
\addlanguage{ukenglish}{loadhyph-en-gb.tex}{}{2}{3}
\addlanguage{british}{loadhyph-en-gb.tex}{}{2}{3}
\addlanguage{UKenglish}{loadhyph-en-gb.tex}{}{2}{3}
\addlanguage{usenglishmax}{loadhyph-en-us.tex}{}{2}{3}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-english
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-english <<EOF
-- from hyphen-english:
	['ukenglish'] = {
		loader = 'loadhyph-en-gb.tex',
		lefthyphenmin = 2,
		righthyphenmin = 3,
		synonyms = { 'british', 'UKenglish' },
		patterns = 'hyph-en-gb.pat.txt',
		hyphenation = 'hyph-en-gb.hyp.txt',
	},
	['usenglishmax'] = {
		loader = 'loadhyph-en-us.tex',
		lefthyphenmin = 2,
		righthyphenmin = 3,
		synonyms = {  },
		patterns = 'hyph-en-us.pat.txt',
		hyphenation = 'hyph-en-us.hyp.txt',
	},
EOF
