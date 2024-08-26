from datasets import load_dataset, DatasetDict
import os

class HuggingFaceDatasetManager:
    def __init__(self):
        self.dataset = None
    
    def download_dataset(self, dataset_name, config_name = None, **kwargs):
        """
        Downloads and loads a Hugging Face dataset with optional configuration.

        Args:
            dataset_name (str): Name of the dataset to download.
            split (str): The split of the dataset to load (e.g., 'train', 'test', 'validation').
            config_name (str, optional): The configuration name of the dataset (if applicable).
            **kwargs: Additional arguments to pass to load_dataset.

        Returns:
            Dataset: The loaded dataset.
        """
        
        try:
            print(f"Loading dataset : {dataset_name} {"with "+config_name if config_name is not None else "default."}")
            self.dataset = load_dataset(dataset_name, config_name, trust_remote_code = True)
            print(f"Dataset '{dataset_name}'  '{"with config"+config_name if config_name else ''}' loaded successfully.")

        except Exception as e:
            print(f"An error occurred: {e}")

    def save_dataset(self, relative_path):
        """
        Saves the currently loaded dataset to the specified relative path.

        Args:
            relative_path (str): Relative path to the directory where the dataset should be saved.
        """
        if self.dataset is None:
            print("No dataset is currently loaded. Please load a dataset before saving.")
            return

        # Construct the absolute path based on the relative path
        absolute_path = os.path.abspath(relative_path)

        if not os.path.exists(absolute_path):
            os.makedirs(absolute_path)

        try:
            if isinstance(self.dataset, DatasetDict):
                self.dataset.save_to_disk(absolute_path)
            else:
                raise ValueError("Loaded dataset is not a DatasetDict. Unable to save.")
            print(f"Dataset saved to {absolute_path} successfully.")
        except Exception as e:
            print(f"An error occurred while saving the dataset: {e}")
            
    def get_dataset(self):
        """
        Returns the currently loaded dataset.

        Returns:
            Dataset: The currently loaded dataset.
        """
        if self.dataset is None:
            print("No dataset is currently loaded.")
        return self.dataset

if __name__ == "__main__":
    manager = HuggingFaceDatasetManager()
    manager.download_dataset("McAuley-Lab/Amazon-Reviews-2023", config_name="raw_review_All_Beauty")
    
    # Save the dataset to the 'data' directory within the project
    manager.save_dataset("nlp-nexus/Sentiment-Analysis/data/amazon_reviews_2023")
    
    # Verify saving
    dataset = manager.get_dataset()
    print(dataset)


