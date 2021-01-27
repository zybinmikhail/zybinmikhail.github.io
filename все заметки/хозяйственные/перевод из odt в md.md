 You might want to look at Sublime Text or (if you’re willing to put in some time learning an unfamiliar interface) Vim or Emacs.
 
 pandoc test1.md -f markdown -t html -s -o test1.html
 
for name in *.odt 
do 
a=(echo ($name) | cut -d "." -f 1)
pandoc name -f odt -t markdown -s -o test1.html
done
