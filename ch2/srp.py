class Report:
    def __init__(self, content: str):
        self.content: str = content

    def generate(self):
        print(f"Report content: {self.content}")


class ReportSaver:
    def __init__(self, report: Report):
        self.report: Report = report

    def save_to_file(self, filename: str):
        with open(filename, "w") as file:
            file.write(self.report.content)


if __name__ == "__main__":
    report_content = "This is the content."
    report = Report(report_content)

    report.generate()

    report_saver = ReportSaver(report)
    report_saver.save_to_file("report.txt")
