import yaml

# yaml_text = \
#     "title: Sample document \n\
# author: \n\
# - name: Andrew Heiss \n\
#   affiliation: Duke University \n\
#   email: andrew.heiss@duke.edu \n\
# - name: Someone else \n\
#   affiliation: Duke University \n\
#   email: andrew.heiss@duke.edu \n\
# date: September 9, 2014 \n\
# published: Incomplete *Draft*. Please do not cite without permission. \n\
# abstract: Lorem ipsum *dolor* sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. \n\
# blinded: False \n"
#
# dataMap = yaml.safe_load(yaml_text)
# print(dataMap)

dataMap = {'title':'Thesis title',
           'front_page':'Her governor nests! The disastrous resident pauses outside a wound. The workshop chews within the piano. The parent groans. The lung responds to a rattling muck.',
           'summary':'His resource designates the censor behind the dark biscuit. The each stomach rules throughout a parody. The employed murderer attends after a debt. Should the porter intervene? An explosive cakes the pub. Why can''t the mutual narrative gear his demolished anecdote?',
           'intro':'The erroneous cylinder dresses within the touching patient. A toe rails! A subsequent heterosexual disables a guy. Why does the fluent intellect suppress the boundary? \
                    The stunt pools the checked correspondence. Why does his geared absolute eye the catastrophic sentient? The tuned seventh listens throughout a constraint. Will whatever higher goodbye dash in the driver? The library troops the urban trouser. \
                    The pole delays an extra groan beneath the editor. A sweet smoker scores. The justice vanishes behind the invalid welfare. A mundane commentary washes. A curriculum demolishes the trilogy.'}

f = open('newtree.yaml', "w")
f.write('---\n')
yaml.dump(dataMap,f)
f.write('...\n')
f.close()