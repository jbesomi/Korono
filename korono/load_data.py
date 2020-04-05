import pandas as pd
from pathlib import PurePath


def get_metadata_df():
    """
    Return metadata Pandas DataFrame
    """

    input_dir = PurePath("../data/")
    metadata_path = input_dir / "metadata.csv.zip"
    metadata_df = pd.read_csv(
        metadata_path, dtype={"Microsoft Academic Paper ID": str, "pubmed_id": str}
    )
    metadata_df = metadata_df.dropna(subset=["abstract", "title"]).reset_index(
        drop=True
    )
    return metadata_df


def get_df():
    """
    Return the underline database
    """

    return get_metadata_df()
