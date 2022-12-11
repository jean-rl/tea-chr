import pandas as pd

def main():
    # Load json file
    data = pd.read_json("../../data/arxiv-metadata-oai-snapshot.json", lines=True)

    # Save the id and abstract columns to a csv file
    data[["id", "abstract"]].to_csv("arxiv.csv", index=False)

    print('Done!')

if __name__ == "__main__":
    main()