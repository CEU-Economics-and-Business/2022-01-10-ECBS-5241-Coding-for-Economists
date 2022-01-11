---
layout: page
title: Class 2
permalink: /class2/index.html
---
# Working with files
```
  115  pwd
  116  cd data/raw/worldbank/
  117  ls -lF
  118  ls -lFh
  119  ls -lFh ../
  120  ls -lFh ../cepii/
  121  ls -lFh 
  122  ls -lFh WDIData.csv
  123  ls -lFh *.csv
  124  ls -lFh WDI*
  125  ls WDICountry*
  126  ls -l WDICountry*
  127  ls -l WDICountry*
  128  ls WDICountry*
  129  ls WDISeries*
  130  ls WDI*.csv
  131  ls -l WDI*.csv
  132  ls -l *Data*
  133  ls -l ../cepii/*.csv
  134  ls -l ../cepii/*.dta
  135  cd ..
  136  cd ..
  137  ls
  138  ls -l
  139  cd derived/
  140  ls -l
  141  pwd
  142  ls gdp????.dta
  143  ls -l gdp????.dta
  144  ls -l gdp201?.dta
  145  ls -l /usr/bin/c*
  146  pwd
  147  ls usr/bin
  148  ls /usr/bin/c*.exe
  149  cd /usr/bin
  150  ls c*
  151  cd
  152  pwd
  153  ls *a*
  154  ls /usr/bin/*a*
  155  ls /usr/bin/*o
  156  pwd
  157  cd
  158  cd data/raw/worldbank/
  159  ls -l *.csv
  160  cat WDIData.csv
  161  less WDIData.csv 
  162  less WDIData.csv 
  163  less WDIData.csv 
  164  less WDIFootNote.csv 
  165  head WDIData.csv 
  166  head -n1 WDIData.csv 
  167  head -n100 WDIData.csv 
  168  head -n100 WDIData.csv 
  169  man head
  170  man head
  171  head --help
  172  head --lines 1 WDIFootNote.csv 
  173  ls --help
  174  cd --help
  175  pwd --help
  176  cd --help
  177  head --help
  178  hwad -h
  179  head -h
  180  pwd
  181  ls -l *.csv
  182  cp WDICountry.csv WDICountry-backup.csv
  183  ls -l
  184  cp --help
  185  mkdir backup
  186  ls -l
  187  ls -lF
  188  cp WDICountry.csv backup/
  189  ls -lF
  190  ls -l backup/
  191  cp *.csv backup/
  192  cp *.csv *-backup.csv
  193  ls -l backup/
  194  mkdir backup-2022-01-11
  195  cp *.csv backup-2022-01-11/
  196  mkdir backup-2022-01-12/
  197  ls -lF
  198  mv backup-2022-01-11/WDIFootNote.csv backup-2022-01-12/
  199  mv --help
  200  ls backup-2022-01-11/ -l
  201  ls backup-2022-01-12/ -l
  202  cd backup-2022-01-11/
  203  ls -lF
  204  mv WDIData.csv WDIData-all.csv 
  205  ls -l
  206  cp WDISeries.csv WDISeries-Time.csv 
  207  cd ..
  208  ls -lF
  209  ls -lF *.
  210  ls --help
  211  ls -lF */
  212  ls -lF */
  213  ls --help
  214  ls -d 
  215  ls -lF
  216  cd backup
  217  ls -l
  218  rm WDIData.csv 
  219  rm --help
  220  rm -i *.csv
  221  rm *.csv
  222  ls -lF
  223  cd ..
  224  ls -lF backup-2022-01-11/
```