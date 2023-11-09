import textfile
import glob


dir_path = './build/*.html'
search_in_dir = '<a href="./" class="list-group-item ">'
replace_in_dir = '<a href="./index.html" class="list-group-item ">'

subdir_path = './build/**/*.html'
search_in_subdir = '<a href="../" class="list-group-item ">'
replace_in_subdir = '<a href="../index.html" class="list-group-item ">'

seach_header_in_dir = '<a href="." class="logo">'
replace_header_in_dir = '<a href="./index.html" class="logo">'

seach_header_in_subdir = '<a href=".." class="logo">'
replace_header_in_subdir = '<a href="../index.html" class="logo">'


def replace(directory_path, search_string, replace_string):
    files = glob.glob(directory_path)
    for file in files:
        textfile.replace(file, search_string, replace_string)
        print('Replace complete:', file)


# build直下の.htmlファイル書換
replace(dir_path, search_in_dir, replace_in_dir)
replace(dir_path, seach_header_in_dir, replace_header_in_dir)

# build/**/の.htmlファイル書換
replace(subdir_path, search_in_subdir, replace_in_subdir)
replace(subdir_path, seach_header_in_subdir, replace_header_in_subdir)
