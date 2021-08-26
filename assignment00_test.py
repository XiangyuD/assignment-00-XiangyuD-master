import assignment00

def test_assignment00():
	default_vals = dict(
	name = 'your name',
	username = 'your github username',
	level = 'freshman/sophomore/junior/senior/masters/PhD',
	major = 'your major',
	programming_exp = 'none/some/extensive',
	python_exp = 'none/some/extensive',
	git_exp = 'none/some/extensive',
	ml_exp = 'none/some/extensive',
	topics = 'topics you are excited to learn in this class',
	)
	out = assignment00.assignment00()
	for k,v in default_vals.items():
		assert default_vals[k] != out[k]




