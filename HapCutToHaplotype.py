import argparse
parser = argparse.ArgumentParser()
parser.add_argument('file', help='load some file')
args = parser.parse_args()

sample = args.file.split('.')[0]
sampleOut = sample+".Haplotype.txt"
PI = sample+":PI"
PGAL = sample+":PG_al"

#print (sample, sampleOut, PI, PGAL)

with open(args.file) as file,\
        open(sampleOut, 'w') as output:

    phased_PI = ''
    output.write("\t".join(['CHROM', 'POS', 'all-alleles', PI, PGAL, '\n']))
    for line in file:
        line=line.strip('\n')
        if line.startswith("*") or line.startswith('BLOCK') or len(line)<2:
            phased_PI = ''
            continue
        else:
            print(line)
            new_line = line.split('\t')
            print(new_line)
            chrom_ = new_line[3]; posi = new_line[4];
            ref_allele = new_line[5]; alt_allele = new_line[6]
            all_alleles = [ref_allele, alt_allele]
            phased_GT = [int(x) for x in new_line[7].split('/')]
            phased_PG_al = "|".join([all_alleles[phased_GT[0]], all_alleles[phased_GT[1]]])
            all_alleles = ','.join(all_alleles)

            if phased_PI == '':
                phased_PI = chrom_ + '_' + posi

            output.write('\t'.join([chrom_, posi, all_alleles, phased_PI, phased_PG_al, '\n']))

