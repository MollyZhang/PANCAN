import pandas as pd


CLIN = "data/clinical.tsv"
RNASEQ = "data/RNASeq_transposed.tsv"

def main():
    clinical_df = pd.read_csv(CLIN, sep="\t", low_memory=False)#, index_col="bcr_patient_uuid")
    rnaseq_df = pd.read_csv(RNASEQ, sep="\t")
    short_barcode = [i[:12] for i in rnaseq_df['sample_barcode']]
    rnaseq_df['short_barcode'] = short_barcode
    # reorder rnaseq columns so that sample_barcode and short_barcode are first two columns
    cols = list(rnaseq_df.columns)
    new_cols = [cols[0]] + [cols[-1]] + cols[1:-1]
    rnaseq_df = rnaseq_df[new_cols]

    #print clinical_df['acronym'].value_counts()
    tissues = clinical_df['acronym'].unique()
    for tissue in tissues:
        barcodes = list(clinical_df[clinical_df['acronym'] == tissue].bcr_patient_barcode)
        print tissue, len(barcodes)
        tissue_df = rnaseq_df[rnaseq_df['short_barcode'].isin(barcodes)].copy(deep=True)
        #tissue_df.drop('short_barcode', axis=1, inplace=True)
        tissue_df.to_csv("data/by_tissue_RNASeq/RNASeq_{0}.tsv".format(tissue), sep="\t", index=False)


if __name__ == '__main__':
    main()