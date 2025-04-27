# bmi_calculator_tracer.py
# This script generates a Markdown file with truth tables for the two BMI calculator loops.

def write_markdown_truth_table(counter=None, sentinel_inputs=None, filename="bmi_loops_truth_table.md"):
    with open(filename, "w") as f:
        f.write("# BMI Loops Truth Table\n\n")

        # Counter-Controlled Loop Table
        f.write("## Counter-Controlled Loop\n\n")
        f.write("| Iteration (i) | Condition (i <= counter) | Notes     |\n")
        f.write("|:-------------:|:-----------------------:|:----------|\n")
        if counter is not None:
            for i in range(1, counter + 2):  # +2 to show the False condition
                if i <= counter:
                    f.write(f"| {i} | True  | i = {i} |\n")
                else:
                    f.write(f"| {i} | False | Loop ends |\n")
        else:
            f.write("| (no data) | (no data) | (no data) |\n")
        f.write("\n---\n\n")

        # Sentinel-Controlled Loop Table
        f.write("## Sentinel-Controlled Loop\n\n")
        f.write("| Iteration | Weight Input | Condition (weight != 0) | Notes         |\n")
        f.write("|:---------:|:------------:|:----------------------:|:--------------|\n")
        if sentinel_inputs is not None:
            for idx, weight in enumerate(sentinel_inputs, 1):
                condition = "True" if weight != 0 else "False"
                notes = "Continue loop" if weight != 0 else "Loop ends"
                f.write(f"| {idx} | {weight} | {condition} | {notes} |\n")
        else:
            f.write("| (no data) | (no data) | (no data) | (no data) |\n")

if __name__ == "__main__":
    # Example usage for standalone run
    write_markdown_truth_table(counter=3, sentinel_inputs=[70, 65, 0])
