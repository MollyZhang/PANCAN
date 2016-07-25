SNV = "data/snv.tsv"
SNV_TP53 = "data/snv_TP53.tsv"

def main():
    extract_TP53_from_snv()

def extract_TP53_from_snv():
    f = open(SNV, "r")
    f_out = open(SNV_TP53, "w")
    for index, line in enumerate(f):
        if index%100 == 0:
            print index
        gene = line.strip().split("\t")[60]
        if gene == "TP53":
            f_out.write(line)
    f.close()
    f_out.close()


if __name__ == '__main__':
    main()