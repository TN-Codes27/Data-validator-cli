import argparse

parser = argparse.ArgumentParser(description="Data Validator CLI")
parser.add_argument("--input", required=True, help="messy_employee_data.csv file path")
parser.add_argument("--report", required=False, help="Path to output validation report")
args = parser.parse_args()


print(f"Input file path: {args.input}")
print(f"Report file path: {args.report}")


