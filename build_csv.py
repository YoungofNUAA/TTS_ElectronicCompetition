import csv
import os

in_dir = '.'
with open(os.path.join(in_dir, 'metadata.csv'), 'w', newline='') as out:
    csv_write = csv.writer(out, dialect='excel')
    path = os.path.join(in_dir, 'data')
    files = os.listdir(path)
    for fname in files:
        print(fname)
        fpath = os.path.join(path, fname)
        if os.path.isdir(fpath) or not fname.endswith('.trn'):
            continue
        with open(fpath, 'r', encoding='UTF-8') as trn:
            content = trn.readlines()[1].rstrip('\n')
            print(content)
        csv_head = ["%s|%s|%s" % (fname.split('.')[0], content, content)]
        csv_write.writerow(csv_head)