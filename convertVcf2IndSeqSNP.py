import sys

inputFileName = sys.argv[1]
popmapFileName = sys.argv[2]
outputFileName = sys.argv[3]
#inputFileName = "allium.vcf"

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
			#print(samplesHeader)
			header = False
	
	outputfile = open(outputFileName+".snp","w")
	outputfile.write("<NM=1.0NF> <MAF=hudson>\n")
	outputfile.write("IND SEX POP")

	#genosets=set()
	genodata=[]
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
		genodata.append(genotypes)
		#print("RESULTS!")
		#print(genotypes)
		#count+=1
		#if count == 5:
	#		break
popmap={}
with open(popmapFileName) as popmapFile:
	for line in popmapFile:
		indv, pop = line.rstrip().split("\t")
		popmap[indv]=pop
#print(popmap)


snps=""
for nr in list(range(1,len(genodata)+1)):
	snps=snps+" A"+str(nr)
snps=snps+"\n"
outputfile.write(snps)

gene=0
indv=0
#print(len(genodata))
while indv < len(genodata[0]):
	outputfile.write(samplesHeader[indv] + " 9 " + popmap.get(samplesHeader[indv]))
	gene=0
	while gene < len(genodata):
		#print("gene: " + str(gene) + " indv: " + str(indv))
		outputfile.write(" " + str(genodata[gene][indv]))
		gene+=1
	outputfile.write("\n")
	indv+=1

#print(genosets)