%global tl_name hyphen-english
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	English hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-english
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-english.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Additional hyphenation patterns for American and British English in
ASCII encoding. The American English patterns (usenglishmax) greatly
extend the standard patterns from Knuth to find many additional
hyphenation points. British English hyphenation is completely different
from US English, so has its own set of patterns.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-english:
ukenglish loadhyph-en-gb.tex
=british
=UKenglish
usenglishmax loadhyph-en-us.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-english:
\addlanguage{ukenglish}{loadhyph-en-gb.tex}{}{2}{3}
\addlanguage{british}{loadhyph-en-gb.tex}{}{2}{3}
\addlanguage{UKenglish}{loadhyph-en-gb.tex}{}{2}{3}
\addlanguage{usenglishmax}{loadhyph-en-us.tex}{}{2}{3}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
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
TL_HYPHEN_EOF
