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
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Additional hyphenation patterns for American and British English in
ASCII encoding. The American English patterns (usenglishmax) greatly
extend the standard patterns from Knuth to find many additional
hyphenation points. British English hyphenation is completely different
from US English, so has its own set of patterns.

