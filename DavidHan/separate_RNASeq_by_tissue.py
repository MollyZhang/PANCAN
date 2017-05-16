import pandas as pd


CLIN = "data/clinical.tsv"
RNASEQ = "data/RNASeq.tsv"
RNASEQ_TRANSPOSED = "data/RNASeq_transposed.tsv"
TISSUE_SEPARATED = "data/by_tissue_RNASeq"


def main():
    clinical_df = pd.read_csv(CLIN, sep="\t", low_memory=False)#, index_col="bcr_patient_uuid")
    old_rnaseq_df = pd.read_csv(RNASEQ, sep="\t", index_col="gene_id")
    rnaseq_df_transposed = old_rnaseq_df.transpose()
    rnaseq_df_transposed.to_csv(RNASEQ_TRANSPOSED, sep="\t", index_label="sample_barcode")
    new_df = pd.read_csv(RNASEQ_TRANSPOSED, sep="\t")
    short_barcode = [i[:12] for i in new_df['sample_barcode']]
    new_df['short_barcode'] = short_barcode
    # reorder rnaseq columns so that sample_barcode and short_barcode are first two columns
    cols = list(new_df.columns)
    new_cols = [cols[0]] + [cols[-1]] + cols[1:-1]
    new_df = new_df[new_cols]

    #print clinical_df['acronym'].value_counts()
    tissues = clinical_df['acronym'].unique()
    for tissue in tissues:
        barcodes = list(clinical_df[clinical_df['acronym'] == tissue].bcr_patient_barcode)
        print tissue, len(barcodes)
        tissue_df = new_df[new_df['short_barcode'].isin(barcodes)].copy(deep=True)
        #tissue_df.drop('short_barcode', axis=1, inplace=True)
        tissue_df.to_csv(TISSUE_SEPARATED + "/RNASeq_{0}.tsv".format(tissue), sep="\t", index=False)


if __name__ == '__main__':
    main()
