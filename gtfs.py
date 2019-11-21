import sys
import re
import subprocess
import testcases
import os

def feedvalidator(gtfs_dir, html_out, temp_out):
    try:
        os.unlink(html_out)
        os.unlink(temp_out)
    except:
        pass
    
    with open(temp_out, 'w') as infile:
        infile.write('{}\n'.format(gtfs_dir))
        
    with open(temp_out, 'r') as infile:
        s = subprocess.Popen(['sh', '-c', 'python transitfeed-1.2.16/feedvalidator.py -o {}'.format(html_out)], 
            stdin=infile, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = s.communicate()

    with open(html_out) as f:
        t = f.read()
        warnings = re.findall(r'<tr><td>(\d+)</td><td><a href="#Warning(.*?)">', t, re.MULTILINE)
        return warnings
            
