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
        input_filecontents = page['filename'] 
        output_filename = page['output']
        title_name = page['title']
        content = open(input_filecontents).read()  
        template_data = open_template()
        finished_index_page = template_data.replace("{{content}}", content). replace("{{title}}", title_name) 
        write_output(output_filename, finished_index_page)
                
def open_template():
	template = open('./templates/base.html').read()
	return template
     	
def write_output(output_filename, finished_index_page):
    open(output_filename, "w+").write(finished_index_page)
            
                          
for page in pages:
    page_title = page['title']
    main ()
	





