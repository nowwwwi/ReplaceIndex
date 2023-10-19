import textfile
import glob
import json


def replace(directory_path, search_string, replace_string):
    files = glob.glob(directory_path)
    for file in files:
        textfile.replace(file, search_string, replace_string)
        print('Replace complete:', file)


def main():
    appsetting = json.load(open('settings.json', 'r'))

    # build直下の.htmlファイル書換
    replace(
        appsetting['directory_path'],
        appsetting['search_in_dir'],
        appsetting['replace_in_dir'])

    replace(
        appsetting['directory_path'],
        appsetting['searh_header_in_dir'],
        appsetting['replace_header_in_dir'])

    # build/**/の.htmlファイル書換
    replace(
        appsetting['subdirectory_path'],
        appsetting['search_in_subdir'],
        appsetting['replace_in_subdir'])

    replace(
        appsetting['subdirectory_path'],
        appsetting['search_header_in_subdir'],
        appsetting['replace_header_in_subdir'])


if __name__ == "__main__":
    main()
