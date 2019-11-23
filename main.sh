#!/bin/sh

# How to run sh main.sh -v 1.0
# Parsing -v option. -v specifies the version of the document
while getopts ":v:" opt; do
  case $opt in
    v) VERSION=$OPTARG      ;;
  esac
done

if test -f "version.tex"; then
    echo "version.tex exist"
    rm version.tex
    echo $VERSION >> version.tex
else
   echo "version.tex does not exist"
   touch version.tex
   echo $VERSION >> version.tex
fi

rm -f *.pdf

echo "\n===== Build =====\n"

pdflatex -synctex=1 -interaction=nonstopmode --enable-write18 "main".tex 
pdflatex -synctex=1 -interaction=nonstopmode --enable-write18 "main".tex

cp main.pdf qc-grovers_v$VERSION.pdf

echo "\n===== Removing aux files ====\n"
sleep 30s

rm -f *.vrb
rm -f *.snm
rm -f *.aux
rm -f *.out
rm -f *.toc
rm -f *.nav
rm -f *.gz
rm -f *.log
rm -f *.fls
rm -f *.fdb_latexmk
rm -f *.pyg
rm -f *.bbl
rm -f *.blg
rm -f *.dvi
