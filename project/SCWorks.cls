\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{SCWorks}[2024/01/01 Custom class for course works]

\LoadClass[a4paper,12pt]{article}

\RequirePackage[utf8]{inputenc}
\RequirePackage[russian]{babel}
\RequirePackage{graphicx}
\RequirePackage{float}
\RequirePackage{amsmath}
\RequirePackage{amssymb}
\RequirePackage{geometry}
\RequirePackage{hyperref}
\RequirePackage{booktabs}
\RequirePackage{caption}
\RequirePackage{enumitem}
\RequirePackage{csquotes}
\RequirePackage[backend=biber, style=authoryear, sorting=nty]{biblatex}
\RequirePackage{minted}

\geometry{top=2cm,bottom=2cm,left=2.5cm,right=2.5cm}

\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    urlcolor=blue,
    citecolor=green!50!black,
}

\setminted{
    frame=lines,
    framesep=5mm,
    baselinestretch=1.2,
    fontsize=\small,
    linenos,
    breaklines=true,
    breakautoindent=false,
}

\renewcommand{\thesection}{\arabic{section}}
\renewcommand{\thesubsection}{\arabic{section}.\arabic{subsection}}
\renewcommand{\thesubsubsection}{\arabic{section}.\arabic{subsection}.\arabic{subsubsection}}

\captionsetup{justification=centering}

\setlist{nosep, left=0pt}

\endinput