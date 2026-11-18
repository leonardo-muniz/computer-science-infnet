from pathlib import Path

DATASET = Path(__file__).resolve().parent.parent / "data" / "file_list.txt"


def load_dataset(max_records=None):
    """Load the dataset, optionally limiting the number of records."""
    with open(DATASET, "r", encoding="utf-8") as file:
        dataset = [line.strip() for line in file if line.strip()]

    if not dataset:
        raise ValueError(f"Dataset is empty: {DATASET}")

    if max_records is not None:
        if max_records <= 0:
            raise ValueError("max_records must be greater than zero")
        dataset = dataset[:max_records]

    return dataset