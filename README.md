# Unclean Data Generator

A synthetic dataset generator designed to produce **realistic but intentionally dirty datasets** for testing data pipelines, data quality tools, and AI/agent systems.

The generator creates structured automotive sales data and injects multiple types of **data quality issues** such as duplicates, typos, nulls, logical inconsistencies, and outliers.

This is useful for testing:

* Data cleaning pipelines
* Data quality validation systems
* AI agents that must reason over imperfect data
* ETL pipelines and analytics systems

---

## Features

Generates a dataset with:

### Structured data

* Customer information
* Dealer information
* Vehicle specifications
* Sales transactions
* Vehicle sensor data

### Injected data quality issues

The dataset intentionally includes realistic problems:

| Type                     | Example                                   |
| ------------------------ | ----------------------------------------- |
| Typographical errors     | `Rahul` → `Rahul` with swapped characters |
| Missing values           | Null emails, engine_cc                    |
| Logical inconsistencies  | Sale price not matching MSRP              |
| Temporal errors          | Delivery date before order date           |
| Key collisions           | Duplicate order numbers                   |
| Outliers                 | Unrealistic horsepower values             |
| Identity inconsistencies | Same person with multiple customer IDs    |
| Duplicate rows           | Random duplicated records                 |
| Corrupted strings        | VIN values prefixed with `ERR!`           |

This makes the dataset ideal for **data quality testing**.

---

## Tech Stack

* Python
* Pandas
* NumPy
* Faker
* Streamlit

---

## Installation

Clone the repository:

```bash
git clone https://github.com/rahulboby/Unclean-Data-Generator.git
cd Unclean-Data-Generator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the App

Launch the Streamlit application:

```bash
streamlit run app.py
```

The app allows you to:

1. Select the number of records
2. Click **Generate Data**
3. Download the generated dataset

---

## Example Output Columns

The dataset includes fields such as:

```
customer_id
customer_name
email
vehicle_model
variant_name
engine_cc
horsepower
msrp
sale_price
order_date
delivery_date
odometer_km
battery_voltage
tire_pressure_psi
```

and many more.

---

## Use Cases

* Testing **data cleaning algorithms**
* Building **data quality dashboards**
* Training **AI agents to handle messy data**
* Practicing **data engineering pipelines**
* Benchmarking **deduplication and record linkage models**

---

## Future Improvements

* Configurable corruption levels
* More industry datasets (finance, healthcare, IoT)
* Dataset schema customization
* Large-scale dataset generation

---

## License

MIT License
