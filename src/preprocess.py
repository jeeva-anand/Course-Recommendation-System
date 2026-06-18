import neattext.functions as nfx


def clean_titles(df):

    df = df.copy()

    df["clean_title"] = (
        df["course_title"]
        .apply(nfx.remove_stopwords)
        .apply(nfx.remove_special_characters)
        .str.lower()
    )

    return df
