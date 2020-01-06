import os, shutil
from scrapy.cmdline import execute
from datetime import datetime

def clear_folder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def main():

    # Parameters for debbuging
    cur_datetime = datetime.now()
    output_folder = "../outputs"
    output_file = "output_{0}.json".format(cur_datetime.strftime("%d%m%Y_%H%M%S"))

    # Set working path
    realpath = os.path.realpath(__file__)
    os.chdir(os.path.dirname(realpath))

    # Clear and setup output folder
    if os.path.isdir(output_folder):
        clear_folder(output_folder)
    else:
        os.mkdir(output_folder)

    try:
        execute(
            [
                'scrapy',
                'crawl',
                'ratings',
                '-o', 
                os.path.join(output_folder,output_file),
            ]
        )
    except SystemExit:
        pass

if __name__ == "__main__":
    main()
