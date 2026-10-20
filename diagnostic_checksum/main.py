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
            numbers = []
            for value in values:
                numbers.append(int(value))

            largest = max(numbers)
            smallest = min(numbers)
            difference = largest - smallest

            checksum += difference
            output_file.write(str(difference) + "\n")

        output_file.write("Checksum: " + str(checksum) + "\n")

print("Finished! Results written to " + output_filename)