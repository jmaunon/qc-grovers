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

rm *.pdf

pdflatex -synctex=1 -interaction=nonstopmode  "main".tex 
pdflatex -synctex=1 -interaction=nonstopmode  "main".tex

cp main.pdf qc-grovers_v$VERSION.pdf

rm *.vrb
rm *.snm
rm *.aux
rm *.out
rm *.toc
rm *.nav
rm *.gz
rm *.log

