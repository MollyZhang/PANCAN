import pandas as pd


SNV = "data/snv.tsv"
SNV_TP53 = "data/snv_TP53.tsv"
CNV_TP53 = "data/cnv_TP53.tsv"
RNASEQ = "data/RNASeq.tsv"
RNASEQ_BRCA = "data/by_tissue_RNASeq/RNASeq_BRCA.tsv"


def main():
    extract_TP53_from_snv()

def create_label():
    """add a TP53 + or - label to RNASeq data"""
    brca_df = pd.read_csv(RNASEQ_BRCA, sep="\t")
    snv_df = pd.read_csv(SNV_TP53, sep="\t")
    print snv_df["Variant_Classification"]


def extract_TP53_from_snv():
    f = open(SNV, "r")
    f_out = open(SNV_TP53, "w")
    for index, line in enumerate(f):
        if index == 0:
            f_out.write(line.strip() + "\tshort_barcode\n")
        if index%1000 == 0:
            print "line", index
        gene = line.strip().split("\t")[60]
        if gene == "TP53":
            barcode = line.strip().split("\t")[16]
            f_out.write(line.strip() + "\t{0}\n".format(barcode[:12]))
    f.close()
    f_out.close()

def cnv_TP53_tranposition():
    df = pd.read_csv(CNV_TP53, sep="\t", index_col = None)
    df = df[df.columns[3:]]

    df = df.transpose()
    df.columns = ["cnv"]
    df["sample_barcode"] = df.index
    df["short_barcode"] = [i[:12] for i in df.sample_barcode]
    new_cols = list(df.columns[1:]) + [df.columns[0]]
    df = df[new_cols]
    df.to_csv("data/cnv_TP53_transposed.tsv", index=None, sep="\t")


if __name__ == '__main__':
    main()