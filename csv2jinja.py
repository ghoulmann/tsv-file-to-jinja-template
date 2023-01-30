import tempfile
from jinja2 import Template

def parse_tsv(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    rows = [line.strip().split('\t') for line in lines]
    return rows

def render_template(template_string, data):
    template = Template(template_string)
    rendered = template.render(**data)
    return rendered

def save_to_tempfile(data):
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(data.encode())
    temp.close()
    return temp.name

def concat_tempfiles(tempfiles):
    with open('output.txt', 'w') as out:
        for tempfile in tempfiles:
            with open(tempfile, 'r') as f:
                out.write(f.read())

if __name__ == '__main__':
    # Change the file path to the location of your tsv file
    filepath = 'example.tsv'

    rows = parse_tsv(filepath)
    tempfiles = []

    # Change the template string to fit your needs
    template_string = '''
    Column 1: {{ column1 }}
    Column 2: {{ column2 }}
    Column 3: {{ column3 }}
    '''

    for row in rows:
        data = {
            'column1': row[0],
            'column2': row[1],
            'column3': row[2],
        }
        rendered = render_template(template_string, data)
        tempfile = save_to_tempfile(rendered)
        tempfiles.append(tempfile)

    concat_tempfiles(tempfiles)
