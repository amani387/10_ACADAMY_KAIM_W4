import pandas as pd
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load datasets
logging.info("Loading datasets...")
train_data = pd.read_csv(r'C:\Users\kingsta\Desktop\week-\10_ACADAMY_KAIM_W4\task_1\data\train.csv')
store_data = pd.read_csv(r'C:\Users\kingsta\Desktop\week-\10_ACADAMY_KAIM_W4\task_1\data\store.csv')
test_data = pd.read_csv(r'C:\Users\kingsta\Desktop\week-\10_ACADAMY_KAIM_W4\task_1\data\test.csv')
sample_submission_data = pd.read_csv(r'C:\Users\kingsta\Desktop\week-\10_ACADAMY_KAIM_W4\task_1\data\sample_submission.csv')

# Inspect datasets
logging.info("Inspecting datasets...")
print(train_data.head())
print(store_data.head())
print(test_data.head())
print(sample_submission_data.head())

# Merge train_data with store_data
logging.info("Merging train data with store data...")
train_merged = pd.merge(train_data, store_data, on='Store', how='left')

# Merge test_data with store_data
logging.info("Merging test data with store data...")
test_merged = pd.merge(test_data, store_data, on='Store', how='left')

# Save merged datasets
train_merged.to_csv(r'C:\Users\kingsta\Desktop\week-\10_ACADAMY_KAIM_W4\task_1\data\train_merged.csv', index=False)
test_merged.to_csv(r'C:\Users\kingsta\Desktop\week-\10_ACADAMY_KAIM_W4\task_1\data\test_merged.csv', index=False)

logging.info("Merged datasets saved successfully.")
