# bmi_calculator_tracer.py
# This script generates a Markdown file with truth tables for the two BMI calculator loops.

def write_markdown_truth_table(
    counter=None,
    counter_data=None,
    sentinel_data=None,
    filename="bmi_loops_truth_table.md"
):
    with open(filename, "w") as f:
        f.write("# BMI Loops Truth Table\n\n")

        # Counter-Controlled Loop Table
        f.write("## Counter-Controlled Loop\n\n")
        f.write("| Iteration (i) | Condition (i <= counter) | Notes     | Weight (kg) | Height (m) | BMI | Classification |\n")
        f.write("|:-------------:|:-----------------------:|:----------|:-----------:|:----------:|:---:|:---------------|\n")
        if counter is not None and counter_data is not None:
            for i, entry in enumerate(counter_data, 1):
                weight, height, bmi, classification = entry
                f.write(f"| {i} | True | i = {i} | {weight} | {height} | {bmi:.2f} | {classification} |\n")
            # Add the row where the loop ends
            f.write(f"| {counter+1} | False | Loop ends | - | - | - | - |\n")
        else:
            f.write("| (no data) | (no data) | (no data) | (no data) | (no data) | (no data) | (no data) |\n")
        f.write("\n---\n\n")

        # Sentinel-Controlled Loop Table
        f.write("## Sentinel-Controlled Loop\n\n")
        f.write("| Iteration | Condition (weight != 0) | Notes         | Weight (kg) | Height (m) | BMI | Classification |\n")
        f.write("|:---------:|:----------------------:|:--------------|:-----------:|:----------:|:---:|:---------------|\n")
        if sentinel_data is not None:
            for idx, entry in enumerate(sentinel_data, 1):
                weight, height, bmi, classification = entry
                if weight == 0:
                    f.write(f"| {idx} | False | Loop ends | 0 | - | - | - |\n")
                else:
                    f.write(f"| {idx} | True | Continue loop | {weight} | {height} | {bmi:.2f} | {classification} |\n")
        else:
            f.write("| (no data) | (no data) | (no data) | (no data) | (no data) | (no data) | (no data) |\n")

if __name__ == "__main__":
    # Example usage for standalone run
    write_markdown_truth_table(
        counter=3,
        counter_data=[(70, 1.75, 22.86, "Normal weight"), (80, 1.8, 24.69, "Normal weight"), (90, 1.7, 31.14, "Obese")],
        sentinel_data=[(100, 1.8, 30.86, "Obese"), (50, 1.6, 19.53, "Normal weight"), (0, None, None, None)]
    )
