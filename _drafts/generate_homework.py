import csv

hw_markup = open('homework.md', 'w')
assignments = list(csv.reader(open('homework.csv', 'rU')))

hw_markup.write('---\nlayout: post\ntitle: "Homework Problems"\n')
hw_markup.write('categories: [syllabus]\ntags: [syllabus]\n')
hw_markup.write('description: MC-MATH-141\n---\n\n')

for hw in assignments[1:]:
	section = '* Section ' + str(hw[0]) + ' homework:\n'
	practice = '    * practice problems: '     + str(hw[1]) + '\n'
	easy     = '    * easy problems: '         + str(hw[2]) + '\n'
	hard     = '    * hard problems: '         + str(hw[3]) + '\n'
	xcr      = '    * extra credit problems: ' + str(hw[4]) + '\n'
	hw_markup.write(section + practice + easy + hard + xcr)