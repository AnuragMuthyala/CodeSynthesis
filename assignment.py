def lookup(s):
	phe = ['uuu','uuc']
	leu = ['uua','uug','cuu','cuc','cua','cug']
	ile = ['auu','auc','aua']
	val = ['guu','guc','gua','gug']
	ser = ['ucu','ucc','uca','ucg','agu','agc']
	pro = ['ccu','ccc','cca','ccg']
	thr = ['acu','acc','aca','acg']
	ala = ['gcu','gcc','gca','gcg']
	tyr = ['uau','uac']
	his = ['cau','cac']
	gln = ['caa','cag']
	asn = ['aau','aac']
	lys = ['aaa','aag']
	asp = ['gau','gac']
	glu = ['gaa','gag']
	cys = ['ugu','ugc']
	arg = ['cgu','cgc','cga','cgg','aga','agg']
	gly = ['ggu','ggc','gga','ggg']
	met = ['aug']

	if s in phe:
		return 'phenylalanine'
	if s in leu:
		return 'leucine'
	if s in ile:
		return 'isoleucine'
	if s in val:
		return 'valine'
	if s in ser:
		return 'serine'
	if s in pro:
		return 'proline'
	if s in thr:
		return 'threonine'
	if s in ala:
		return 'alanine'
	if s in tyr:
		return 'tryptophan'
	if s in his:
		return 'histidine'
	if s in gln:
		return 'glycine'
	if s in asn:
		return 'asparagine'
	if s in lys:
		return 'lysine'
	if s in asp:
		return 'aspartic acid'
	if s in glu:
		return 'glutamic acid'
	if s in cys:
		return 'cysteine'
	if s in arg:
		return 'arginine'
	if s in gly:
		return 'glutamine'
	if s in met:
		return 'methionine'

def generate(s):
	stop = ['uaa','uag','uga']
	start = ['aug']
	p = []
	i = 0

	while i < len(s):
		if s[i:i+3] in start:
			prot = ['methionine']
			i = i + 3
			while s[i:i + 3] not in stop and i < len(s):
				prot.append(lookup(s[i:i + 3]))
				i = i + 3
			if None not in prot:
				p.append(prot)
			i = i + 3

		i = i + 1
	return p

def printer(lst):
	for i in range(len(lst)):
		if None not in lst[i]:
			print('Protein ' + str(i + 1))
			s = '|'.join(lst[i])
			print(s)
			

with open('DNA.txt','r') as o:
	l = o.read()

s = ''
l = l[::-1]
l = l.split('\n')

for i in range(len(l)):
	l[i] = list(l[i])

#print(l)
for i in l:
	for j in range(len(i)):
		if i[j] == 'a':
			i[j] = 'u'
		elif i[j] == 'c':
			i[j] = 'g'
		elif i[j] == 'g':
			i[j] = 'c'
		else:
			i[j] = 'a'
for i in l:
	s = s + ''.join(i)

print('RNA Code')
print(s+'\n')
prot = generate(s)

printer(prot)


