import great_expectations as gx

context = gx.get_context()
assert type(context).__name__ == "EphemeralDataContext" #code sets up a temp env for data validation

data_source = context.sources.add_pandas(name="messy_employee_data") 
data_asset = data_source.add_csv_asset(name="employee_data", filepath="messy_employee_data.csv")

batch_definition_name = "employee_data_batch"
batch_definition = data_asset.add_batch_definition(name=batch_definition_name)
assert batch_definition.name == batch_definition_name

batch_parameters = { "dataframe" : employee_data_df}
batch = batch_definition.get_batch(batch_parameters=batch_parameters) 

