import textfile
import glob
import settings


def replace(directory_path, search_string, replace_string):
    files = glob.glob(directory_path)
    for file in files:
        textfile.replace(file, search_string, replace_string)
        print('Replace complete:', file)


def main():
    # build直下の.htmlファイル書換
    replace(
        settings.DIR_PATH,
        settings.SEARCH_IN_DIR,
        settings.REPLACE_IN_DIR)

    replace(
        settings.DIR_PATH,
        settings.SEARCH_HEADER_IN_DIR,
        settings.REPLACE_HEADER_IN_DIR)

    # build/**/の.htmlファイル書換
    replace(
        settings.SUBDIR_PATH,
        settings.SEARCH_IN_SUBDIR,
        settings.REPLACE_IN_SUBDIR)

    replace(
        settings.SUBDIR_PATH,
        settings.SEARCH_HEADER_IN_SUBDIR,
        settings.REPLACE_HEADER_IN_SUBDIR)


if __name__ == '__main__':
    main()
