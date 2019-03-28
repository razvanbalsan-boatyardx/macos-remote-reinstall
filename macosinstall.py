#/usr/bin/python

'''
macosinstall.py

A script to download an installable Install macOS application and to use it to either upgrade
or erase-install the device on which it is running.
'''


import os
import httplib


def mkdir_p(path):
    # https://stackoverflow.com/a/600612
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def save_installinstallmacos(work_dir):
    # put installinstallmacos.py in the working directory
    url = 'https://raw.githubusercontent.com/grahampugh/macadmin-scripts/master/installinstallmacos.py'
    installinstallmacospath = os.path.join(work_dir, 'installinstallmacos.py')

    # TODO - requests is no good here, so switch to httplib
    r = requests.get(url, allow_redirects=True)
    with open(installinstallmacospath, 'wb') as f:
        f.write(r.content)


def find_existing_installer():
    pass


def overwrite_existing_installer():
    pass


def move_to_applications_folder():
    pass


def download_installer():
    pass


def show_jamf_helper():
    pass


def kill_jamf_helper():
    pass


def upgrade():
    pass


def erase_install():
    pass


def parse_args():
    pass


def main():
    # make sure the working directory exists
    work_dir = '/Library/Management/macosinstall'
    mkdir_p(work_dir)
    # get installinstallmacos.py
    save_installinstallmacos(work_dir)


if __name__ == '__main__':
    main()




