print("Nimisha  Bhateja") 
print("35314802722")
import os

def transform_file(input_file, output_file):
    try:
        if not os.path.exists(input_file):
            with open(input_file, 'w') as f:
                f.write("Default text")

        with open(input_file, 'r') as infile:
            data = infile.read()

        transformed_data = data.upper()

        with open(output_file, 'w') as outfile:
            outfile.write(transformed_data)

        print(f"Data successfully written to {output_file} in transformed format.")

    except Exception as e:
        print(f"An error occurred: {e}")

input_filename = "input_file.txt"
output_filename = "output_file.txt"
transform_file(input_filename, output_filename)
