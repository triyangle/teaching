import sys
import json
import os
import re

arguments = sys.argv

category = arguments[1]
number = arguments[2]
base_dir = 'src/%s' % category

title = '%s%s' % (category, number)

# Grab base tex
with open(os.path.join(base_dir, '%s.base.tex' % title)) as f:
    base_latex = f.read()

# Grab raw tex
questions = []
filenames = []
delimiters = ('\\begin{solution}', '\end{solution}')
regex = '|'.join(map(re.escape, delimiters))
for input_ in base_latex.splitlines():
    if not input_:
        continue
    filename = 'src/problems/%s' % input_.replace('\input{', '')[:-1]
    filenames.append(filename)
    tex = open(filename).read()
    pieces = re.split(regex, tex)
    raw_tex = ''.join(pieces[::2])
    questions.append(raw_tex)

with open(os.path.join(base_dir, '%s-raw.tex' % title), 'w') as f:
    f.write('\n'.join(questions))

generated_files = [
    {'template': 'template.tex', 'out': '%s.tex'},
    {'template': 'template-sol.tex', 'out': '%s-sol.tex'}
]

base_latex = base_latex.replace('\input{', '\input{src/problems/')

for data in generated_files:
    with open(os.path.join(base_dir, data['template'])) as f:
        latex = f.read().replace('<<title>>', title) \
                        .replace('<<base>>', base_latex)
    with open(os.path.join(base_dir, data['out'] % title), 'w') as f:
        f.write(latex)

# Generate images
template_img_path = os.path.join(base_dir, 'template-img.tex')
if os.path.exists(template_img_path):
    with open(template_img_path) as f:
        template = f.read()

    for i, filename in enumerate(filenames):
        with open(os.path.join(base_dir, '%s-img-%d.tex' % (title, i)), 'w') as f:
            f.write(template.replace('<<question>>', filename))
