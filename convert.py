from glob import glob
from shutil import copytree, ignore_patterns, rmtree

path = input("Please enter the full path designated for conversion.\nPath:   ")
path_utf8 = path+"_utf8"
try:
    copytree(path, path_utf8, ignore = ignore_patterns('*.html', '*.php', '*.txt'), dirs_exist_ok=True)
    print("SUCCESS: Folder structure copied successfully.")
except:
    print("FAIL: Failed to copy folder structure.\nProbable cause of error: not valid or parial path entered.")
else:
    try:
        files = (glob(path+"/**/*.*", recursive = True))
        print("SUCCESS: Files designated for conversion have been found:")
        for f in files:
            print(f)
    except:
        print("FAIL: Failed to find files designated for conversion.\nProbable cause of error: path does not contain files of the currently supported extensions:\n.html, .php, .txt")
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
    finally:
        try:
            print("Cleaning up:")
            rmtree(path_utf8, ignore_errors=False, onerror=None)
            print("SUCCESS: Cleaned up succesfully.")
            print("ATTENTION: File conversion has not taken place.")
        except:
            print("FAIL: Failed to clean up copied directory structure. Sorry for the inconveinience.")