from datasets import load_dataset, get_dataset_config_names
import os

def download_and_save_dataset(dataset_name, save_dir, config_name=None):
    """
    Download the dataset from Hugging Face and save it to the specified directory.
    
    Args:
        dataset_name (str): The name of the dataset to download.
        save_dir (str): The directory where the dataset should be saved.
        config_name (str, optional): The configuration name of the dataset, if applicable.
    """
    # Ensure the save directory exists
    os.makedirs(save_dir, exist_ok=True)
    
    # Fetch available configurations
    available_configs = get_dataset_config_names(dataset_name)
    
    if config_name and config_name not in available_configs:
        raise ValueError(f"Config '{config_name}' not found. Available configs are: {available_configs}")
    
    # Load the dataset
    if config_name:
        dataset = load_dataset(dataset_name, config_name=config_name, trust_remote_code=True)
    else:
        dataset = load_dataset(dataset_name, trust_remote_code=True)
    
    # Save each split of the dataset
    for split in dataset:
        split_dataset = dataset[split]
        file_path = os.path.join(save_dir, f"{split}.json")
        split_dataset.to_json(file_path)
        print(f"Saved {split} dataset to {file_path}")

if __name__ == "__main__":
    dataset_name = "McAuley-Lab/Amazon-Reviews-2023"
    config_name = "raw_meta_All_Beauty"  # Set this to a config name if needed
    save_dir = os.path.join(os.getcwd(), "Sentiment-Analysis/data/amazon_reviews_2023")
    
    download_and_save_dataset(dataset_name, save_dir, config_name)
