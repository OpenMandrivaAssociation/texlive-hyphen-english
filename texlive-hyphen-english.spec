Name:		texlive-hyphen-english
Version:	20111102
Release:	1
Summary:	English hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-english.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-hyphen-base
Requires:	texlive-hyph-utf8
Conflicts:	texlive-texmf <= 20110705-3
Requires(post):	texlive-hyphen-base

%description
Additional hyphenation patterns for American and British
English in ASCII encoding.  The American English patterns
(usenglishmax) greatly extend the standard patterns from Knuth
to find many additional hyphenation points.  British English
hyphenation is completely different from US English, so has its
own set of patterns.

%pre
    %_texmf_language_dat_pre
    %_texmf_language_def_pre
    %_texmf_language_lua_pre

%post
    %_texmf_language_dat_post
    %_texmf_language_def_post
    %_texmf_language_lua_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_language_dat_pre
	%_texmf_language_def_pre
	%_texmf_language_lua_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_language_dat_post
	%_texmf_language_def_post
	%_texmf_language_lua_post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-english
%_texmf_language_def_d/hyphen-english
%_texmf_language_lua_d/hyphen-english

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-english <<EOF
%% from hyphen-english:
ukenglish loadhyph-en-gb.tex
=british
=UKenglish
usenglishmax loadhyph-en-us.tex
EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-english <<EOF
%% from hyphen-english:
\addlanguage{ukenglish}{loadhyph-en-gb.tex}{}{2}{3}
\addlanguage{british}{loadhyph-en-gb.tex}{}{2}{3}
\addlanguage{UKenglish}{loadhyph-en-gb.tex}{}{2}{3}
\addlanguage{usenglishmax}{loadhyph-en-us.tex}{}{2}{3}
EOF
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
