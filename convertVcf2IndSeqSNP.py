import sys

inputFileName = sys.argv[1]

def geno_switcher(argument):
	switcher = {
		'1/1': "0",
		'0/1': "1",
		'0/0': "2",
		'./.': "9"
	}
	return(switcher.get(argument, "Invalid genotype!"))


header=True
count=0
with open(inputFileName) as inputFile:
	while header == True:
		line = inputFile.readline()
		if "##" in line:
			continue
		elif "#CHROM" in line:
			samplesHeader = line.rstrip().split("\t")
			startSampleNames=0
			while samplesHeader[0] != "FORMAT":
				samplesHeader.pop(0)
				startSampleNames+=1
			samplesHeader.pop(0)
			startSampleNames+=1
			print(samplesHeader)
			header = False
	
	#genosets=set()
	for line in inputFile:
		lineAsList = line.rstrip().split("\t")
		genotypes = lineAsList[startSampleNames:-1]
		#print("ORIGINAL")
		#print(genotypes)
		for g in genotypes:
			idx = genotypes.index(g)
			geno = g.split(":")[0]
			#genosets.add(geno)
			geno = geno_switcher(geno)
			genotypes[idx] = geno
		#print("RESULTS!")
		#print(genotypes)
		#count+=1
		#if count == 5:
	#		break

#print(genosets)