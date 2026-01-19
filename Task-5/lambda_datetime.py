# Lambda function to extract date from datetime object
from datetime import datetime
datetime_obj = datetime(2026, 1, 15, 2, 30, 45)
extract_date = lambda dt: dt.date()
print("Extracted Date:", extract_date(datetime_obj))

