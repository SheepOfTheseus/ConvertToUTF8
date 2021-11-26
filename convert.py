from glob import glob
from shutil import copytree, ignore_patterns, rmtree
import os.path

def convert(path) -> None:
    path_utf8 = path+"_utf8"
    failed = False
    not_all_converted = False
    try:
        copytree(path, path_utf8, ignore = ignore_patterns('*.html', '*.php', '*.txt'), dirs_exist_ok=True)
        print("SUCCESS: Folder structure copied successfully.")
    except:
        print("FAIL: Failed to copy folder structure.")
        failed = True
    else:
        try:
            files = (glob(path+"/**/*.*", recursive = True))
            print("SUCCESS: Files designated for conversion have been found:")
            for f in files:
                print(f)
        except:
            print("FAIL: Failed to find files designated for conversion.\nProbable cause of error: path does not contain files of the currently supported extensions:\n.html, .php, .txt")
            failed = True
        else:
            for f_unc in files:
                try:
                    f_cvt = path+"_utf8"+f_unc[len(path): len(f_unc)]
                    with open(f_unc, encoding='cp1251') as fobj_unc:
                        with open(f_cvt, "w", encoding='utf8') as fobj_cvt:
                            fobj_cvt.write(fobj_unc.read().encode('cp1251').decode('cp1251'))
                            print("SUCCESS: Converted   "+f_unc)
                except:
                    print("FAIL: Failed to convert   "+f_unc)
                    not_all_converted = True

        finally:
            if failed:
                try:
                    print("Cleaning up:")
                    rmtree(path_utf8, ignore_errors=False, onerror=None)
                    print("SUCCESS: Cleaned up succesfully.")
                    print("ATTENTION: File conversion has not taken place.")
                except:
                    print("FAIL: Failed to clean up copied directory structure. Sorry for the inconveinience.")
            if not_all_converted:
                print("ATTENTION: Some files have not been converted succesfully.")

p = input("Please enter path to the directory designated for conversion.\nPath:   ")
if os.path.exists(p):
    convert(p)
else:
    p = os.path.expanduser("~/"+p)
    if os.path.exists(p):
        convert(p)
    else:
        print("Not a valid path.")
