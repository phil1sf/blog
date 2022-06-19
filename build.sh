#combining files into index html to directory docs
cat templates/top.html content/index.html templates/bottom.html > docs/index.html

#combining files into about.html to directory docs
cat templates/top.html content/about.html templates/bottom.html > docs/about.html

#combining files into resume.html to directory docs
cat templates/top.html content/resume.html templates/bottom.html > docs/resume.html
