

#reads in the top html
top_html = open('./templates/top.html').read()

#reads in the bottom.html
bottom_html = open('./templates/bottom.html').read()

#reads in the middle index.html
middle_html = open('./content/index.html').read()

#combine top middle and bottom into single html 
combined_html = top_html + middle_html + bottom_html

#writes new html to a brand new file in another directory
open('./docs/index.html' , 'w+').write(combined_html)



#reads in the middle index.html
middle_html = open('./content/about.html').read()

#combine top middle and bottom into single html 
combined_html = top_html + middle_html + bottom_html

#writes new html to a brand new file in same directory
open('./docs/about.html' , 'w+').write(combined_html)



#reads in the middle index.html
middle_html = open('./content/resume.html').read()

#combine top middle and bottom into single html 
combined_html = top_html + middle_html + bottom_html

#writes new html to a brand new file in same directory
open('./docs/resume.html' , 'w+').write(combined_html)
