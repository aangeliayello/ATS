# PDF Resume Keyword Adder
This Python script allows you to dynamically add keywords to a PDF resume. It supports reading keywords from a `.txt` file and paths from a `config.json` file. An optional command-line argument can be provided to append a user-defined postfix to the output filename, along with an automatic date-time stamp for version control.

## Features
- **Reads Resume and Keywords:** Automatically reads your resume in PDF format and a list of keywords from a text file.
- **Configurable Paths:** Utilizes a config.json file to easily configure the paths for input and output files.
- **Automatic Versioning:** Appends the current date and time to the output filename for easy version tracking, with an option for an additional custom postfix.

## Installation
First, ensure you have Python installed on your system. Then, install the required PyMuPDF package using pip:

`pip install -r /path/to/requirements.txt`

## Configuration
Before running the script, configure the `config.json` file in the `config` directory with the correct paths:

```json
{
    "resume_path": "path/to/your_resume.pdf",
    "keywords_file": "path/to/keywords.txt",
    "output_path": "desired_output_filename.pdf"
}
```

Place your resume in the specified location and list your keywords, one per line, in the `keywords.txt` file.

## Usage
Run the script from the command line, optionally specifying a postfix for the output filename:

```python src/main.py [--postfix POSTFIX]```

- **`--postfix POSTFIX`**: (Optional) Appends a custom postfix to the output filename before the date-time stamp.

The script will generate a new PDF file with the specified keywords added in white color (invisible to the eye but present in the document), stored in the `modified_resumes` directory, with the filename format `[original_name]_[postfix]_[datetime].pdf`.

## Contributing
Contributions to this project are welcome! Please fork the repository, make your changes, and submit a pull request. 
Or, ping me if you have good info about the inner workings of the ATS's.
