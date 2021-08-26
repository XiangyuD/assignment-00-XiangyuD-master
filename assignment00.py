def assignment00():

	''' Assignment 00
		Provide information on your background in programming, python, git, and machine learning. 
		Provide insight into what you are hoping to learn in this class this semester. 
	 	Submit your assignment as described in class by pushing to github. 
	''' 
	vals = dict(
	name = 'Xiangyu Deng',
	username = 'XiangyuD',
	level = 'masters',
	major = 'Electric and computer engineering',
	programming_exp = 'some',
	python_exp = 'some',
	git_exp = 'some',
	ml_exp = 'some',
	topics = 'training some model',
	)

	print(f'My name is: {vals["name"]}')
	print(f'My github username is: {vals["username"]}')
	print(f'I am a {vals["level"]} student')
	print(f'I am majoring in: {vals["major"]}')
	print(f'My level of programming experience in general is: {vals["programming_exp"]}')
	print(f'My python programming experience is: {vals["python_exp"]}')
	print(f'My git experience is: {vals["git_exp"]}')
	print(f'My experience in machine learning is: {vals["ml_exp"]}')
	print(f'I am excited to learn the following in this class: {vals["topics"]}')

	return vals

if __name__ == '__main__':
	assignment00()
