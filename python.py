pages = [ 
		{
			"filename": "content/about.html",
			"output": "docs/about.html",
			"title": "About Me",
		},
		{
			"filename": "content/index.html",
			"output": "docs/index.html",
			"title": "Main",
		},
		{
			"filename": "content/resume.html",
			"output": "docs/resume.html",
			"title": "Resume",
		}
		]
			
			
def main ():
    for page in pages:
        top_html = open('./templates/top.html').read()
        bottom_html = open('./templates/bottom.html').read()
        input_filecontents = page['filename']
        content = open(input_filecontents).read()

# Give this a try: "w+" can be used to overwrite a file if it exists or create a new file if it doesn't.
        if input_filecontents == "./content/about.html":
            about_html = top_html + content + bottom_html            
            open('./docs/about.html', 'w+').write(about_html)
        
        if input_filecontents == "./content/index.html":
            index_html = top_html + content + bottom_html
            open('./docs/index.html', 'w+').write(index_html)
        
        if input_filecontents == "./content/resume.html":
            resume_html = top_html + content + bottom_html
            open('./docs/resume.html', 'w+').write(resume_html)
            
           
for page in pages:
    page_title = page['title']
    main ()
		
	




