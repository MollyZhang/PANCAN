import pandas as pd


CLIN = "data/clinical.tsv"

def main():
    df = pd.read_csv(CLIN, sep="\t", low_memory=False)#, index_col="bcr_patient_uuid")
    #print df['acronym'].value_counts()
    tissues = df['acronym'].unique()
    for tissue in tissues:
        tissue_df = df[df['acronym'] == tissue]
        tissue_df.to_csv("data/by_tissue_Clinical/clinical_{0}.tsv".format(tissue), sep="\t", index=False)


if __name__ == '__main__':
    main()