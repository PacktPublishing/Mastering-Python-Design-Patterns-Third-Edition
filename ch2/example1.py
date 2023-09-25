class Report:
    def __init__(self, content):
        self.content = content

    def generate(self):
        print(f"Report content: {self.content}")


class ReportSaver:
    def __init__(self, report):
        self.report = report

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(self.report.content)


if __name__ == "__main__":
    # Create a Report object
    report_content = "This is the content of the report."
    report = Report(report_content)

    # Generate the report
    report.generate()

    # Save the report to a file
    report_saver = ReportSaver(report)
    report_saver.save_to_file("report.txt")
