import json
import os
import odf.opendocument as odt

def append_md_file(loc_dir, filename, write_file):
    print('Reading from ' + str(filename))
    readfile = open(os.path.join(loc_dir, filename), 'r')
    file_contents = readfile.read()
    readfile.close()
    write_file.write(file_contents)
    write_file.write("\n")
    return write_file

def ref_text2list(text, marker='\\[', marker_e='\\]'):
    index = 0
    count = 0
    prev_index = 0
    ref_list = ''
    while index < len(text):
        index = text.find(marker, index)
        ref_list += text[prev_index:index]
        if index == -1:
            ref_list += "\n"
            break
        count += 1
        ref_list += str(count) + '.'
        index_e = text.find(marker_e,index)+len(marker_e)
        print('reference ' + str(count) + ' found at: ' + str(index) + ' to ' + str(index_e))
        index += len(marker)
        prev_index = index_e
    print(ref_list)
    return ref_list

build_config = 0

loc_dir = 'D:\Projects\AdvNetCREW\doc'
work_dir = 'D:\Projects\AdvNetCREW\doc\\build'

ref_source = "=-/=-/=-/REF-SOURCE\n"
ref_location = "=-/=-/=-/REF-LOCATION\n"

os.chdir(loc_dir)

if build_config:
    print('Building config file')
    Chapters = {1:'Introduction.md',2:'Literature Study.md',3:'Methods.md',4:'Results.md',5:'Discussion.md',6:'Conclusion.md',7:'References.md'}
    Appendix = {'A':'AppendixA.md'}


    config = {'Title':'Titlepage.md','Abstract':'Summary.md','Abbrv':1,'TOC':1,'Structure':Chapters,'Ref':1,'App':Appendix}

    with open('config.json','w') as outfile:
        json.dump(config, outfile, indent=4)
    print('Done')
else:
    print('Building document')
    with open('config.json','r') as infile:
        config = json.load(infile)

    print(json.dumps(config, indent=4, separators=(',', ': ')))

    write_file_name = os.path.join(work_dir,'abbrv_gen_file.md')
    write_file = open(write_file_name,'w')

    # Build first file to automatically generate abbreviations list
    write_file = append_md_file(loc_dir,config['Title'],write_file)
    write_file = append_md_file(loc_dir, config['Abstract'], write_file)

    for chapter in config['Structure']:
        write_file = append_md_file(loc_dir,config['Structure'][str(chapter)], write_file)

    if config['Ref']:
        write_file.write(ref_location)
        write_file.write("\n")

    for appendix in config['App']:
        write_file = append_md_file(loc_dir, config['App'][appendix], write_file)

    write_file.write(ref_source)

    write_file.close()
    # TODO: Code that builds Abbreviations list comes here

    # Build document



    print('Building intermediate output files with pandoc')
    # pandoc command to convert file
    os.system("pandoc \"" + write_file_name + "\" -f markdown -t odt -s -o build\\buildfile.odt --bibliography=bib\zotero_bibliography_export.bib --csl=bib\ieee.csl")
    os.system("pandoc build\\buildfile.odt -f odt -t markdown -s -o build\\buildfile.md")

    # Placing references in correct location
    print(os.path.join(work_dir, 'buildfile.md'))
    readfile = open(os.path.join(work_dir, 'buildfile.md'), 'r', encoding="utf8")

    text = readfile.read()
    readfile.close()
    loc = text.find(ref_source)
    refs = text[(loc+len(ref_source))::]

    print(refs)
    refs = ref_text2list(refs)

    write_file = open(os.path.join(work_dir, 'references_built.md'), 'w', encoding="utf8")
    write_file.write(refs)
    write_file.close()

    os.system("pandoc build\\references_built.md -f markdown -t odt -s --reference-odt=thesis-reference.odt --template=thesis.opendocument -o build\\references_built.odt")

    before_ref = text.find(ref_location)
    after_ref = before_ref+len(ref_location)

    new_text = text[:before_ref] + refs + text[after_ref:loc]

    write_file = open(os.path.join(work_dir, 'buildfile2.md'),'w', encoding="utf8")
    write_file.write(new_text)
    write_file.close()

    os.system("pandoc build\\buildfile2.md -f markdown -t odt -s --reference-odt=thesis-reference.odt --template=thesis.opendocument -o build\\buildfile2.odt")

    doc = odt.load("build\\buildfile2.odt")


    doc.save("build\\buildfile3.odt")
    print('Done')

    # command that succesfully built a document with a complex template and table of contents
    # pandoc empty.md newtree.yaml -s -o thesis-test.odt --reference-odt=thesis-template.odt --template=thesis-template.opendocument
