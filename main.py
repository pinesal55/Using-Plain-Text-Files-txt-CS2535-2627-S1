input_filename = "checksum_sample.txt"
output_filename = "checksum_results.txt"

checksum = 0

with open(input_filename, "r") as input_file:
    with open(output_filename, "w") as output_file:
        for line in input_file:
            clean_line = line.strip()
            if clean_line == "":
                continue

            values = clean_line.split()
            numbers = [int(value) for value in values]

            largest = max(numbers)
            smallest = min(numbers)
            difference = largest - smallest

            checksum += difference
            output_file.write(f"{difference}\n")

        # This must be outside the for-loop
        output_file.write(f"Checksum: {checksum}\n")

print(f"Finished! Results written to {output_filename}")