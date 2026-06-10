from src.extract import extract_data
from src.transform import clean_data
from src.load import load_to_mysql

# Extract
matches, deliveries = extract_data()

# Transform
matches, deliveries = clean_data(
    matches,
    deliveries
)

# Load
load_to_mysql(
    matches,
    deliveries
)