import argparse
import datetime
from os.path import join

from config_handler import read_config
from pdf_handler import add_keywords_to_pdf_resume
from keywords_handler import read_keywords_from_file

def get_command_line_arguments():
    parser = argparse.ArgumentParser(description='Modify PDF resume with keywords.')
    parser.add_argument('-p', '--postfix', type=str, help='Optional postfix for the output filename', default='')
    return parser.parse_args()

if __name__ == "__main__":
    args = get_command_line_arguments()
    
    config = read_config("config/config.json")
    
    resume_file = config["resume_path"]
    keywords_file = config["keywords_file"]
    output_path = config["output_path"]
    
    # Append the postfix to the output filename if provided
    output_name_part, extension = output_path.rsplit('.', 1)
    
    if args.postfix:
        output_name_part_postfix =  f"_{args.postfix}.{extension}"
    else:
        date_time_postfix = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_name_part_postfix =  f"_{date_time_postfix}.{extension}"

    output_path = output_name_part + output_name_part_postfix
    
    # Assuming functions to read keywords and modify the PDF are implemented
    keywords = read_keywords_from_file(keywords_file)
    add_keywords_to_pdf_resume(resume_file, keywords, output_path)