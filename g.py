from GF2 import one
 
def GF2_addLists(L1,L2): return [vx+ux for (vx,ux) in zip(L1,L2)]
 
def solve(u):
	#data
	
	data = { 
	 'a':[one,one,one,0,0,0,0]
	, 'b':[0,one,one,one,0,0,0]
	, 'c':[0,0,one,one,one,0,0]
	, 'd':[0,0,0,one,one,one,0]
	, 'e':[0,0,0,0,one,one,one]
	, 'f':[0,0,0,0,0,one,one]
	}
 	
	map = ['a','b','c','d','e','f']
 
	"""
	data = {
	'a' : [one,one,0,0,0,0,0]
	,'b' : [0,one,one,0,0,0,0]
	,'c' : [0,0,one,one,0,0,0]
	,'d' : [0,0,0,one,one,0,0]
	,'e' : [0,0,0,0,one,one,0]
	,'f' : [0,0,0,0,0,one,one]
	}
	"""
	#target
	#u = [0,0,one,0,0,one,0]
 
	answers = []
 
	# generate conditions
	di = [0,1]
	conditions =[[ax,bx,cx,dx,ex,fx] for ax in di for bx in di for cx in di for dx in di for ex in di for fx in di]
	
	for condition in conditions:
		sum = [0,0,0,0,0,0,0]
		solution = set()
		for (index,flag) in enumerate(condition):
			if flag == 1:
				sum = GF2_addLists(sum,data[map[index]])
				solution.add(map[index])
		
		if sum == u:
			answers.append(solution)
	
	return answers
