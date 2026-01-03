import random
from datetime import datetime, timedelta

def generate_nik():
    # Random Province/City/Subdistrict (using 31.01.01 as a base for Jakarta)
    area_code = f"31{random.randint(1, 75):02}{random.randint(1, 15):02}"
    
    # Random Birthday within the last 50 years
    start_date = datetime(1970, 1, 1)
    random_days = random.randint(0, 365 * 50)
    birth_date = start_date + timedelta(days=random_days)
    
    day = birth_date.day
    # 50% chance to be female (add 40 to the day)
    if random.choice([True, False]):
        day += 40
        
    date_str = f"{day:02}{birth_date.month:02}{str(birth_date.year)[2:]}"
    
    # Unique sequence
    sequence = f"{random.randint(1, 999):04}"
    
    return f"{area_code}{date_str}{sequence}"

# Generate 1000 rows
nik_list = [generate_nik() for _ in range(1000)]

# Save to file
with open("nik.training_text", "w") as f:
    f.write("\n".join(nik_list))

print("File 'nik.training_text' generated successfully with 1,000 rows.")
