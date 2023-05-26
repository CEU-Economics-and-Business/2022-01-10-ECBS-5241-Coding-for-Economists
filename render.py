from jinja2 import Template
from docxtpl import DocxTemplate
from yaml import load, SafeLoader
from sys import stdin

doc = DocxTemplate('syllabus-template.docx')
md = Template(open('syllabus-template.md', 'rt').read())
context = load(stdin, Loader=SafeLoader)
file_name = '-'.join('{} {}'.format(context['code'], context['title']).split())

# save .md
with open('{}.md'.format(file_name), 'wt') as file:
	file.write(md.render(context))

# then .docx
doc.render(context)
doc.save('{}.docx'.format(file_name))