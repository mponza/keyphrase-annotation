# Code from http://stackoverflow.com/questions/11930515/unzip-nested-zip-files-in-python/17415163#17415163

import os
import zipfile

from StringIO import StringIO


def extract_nested_zipfile(path, parent_zip=None):
    """
    Returns a ZipFile specified by path, even if the path contains
    intermediary ZipFiles.  For example, /root/gparent.zip/parent.zip/child.zip
    will return a ZipFile that represents child.zip
    """
    
    def extract_inner_zipfile(parent_zip, child_zip_path):
        """Returns a ZipFile specified by child_zip_path that exists inside
        parent_zip.
        """
        memory_zip = StringIO()
        memory_zip.write(parent_zip.open(child_zip_path).read())
        return zipfile.ZipFile(memory_zip)

    if ('.zip' + os.sep) in path:
        (parent_zip_path, child_zip_path) = os.path.relpath(path).split(
            '.zip' + os.sep, 1)
        parent_zip_path += '.zip'

        if not parent_zip:
            # This is the top-level, so read from disk
            parent_zip = zipfile.ZipFile(parent_zip_path)
        else:
            # We're already in a zip, so pull it out and recurse
            parent_zip = extract_inner_zipfile(parent_zip, parent_zip_path)

        return extract_nested_zipfile(child_zip_path, parent_zip)
    else:
        if parent_zip:
            return extract_inner_zipfile(parent_zip, path)
        else:
            # If there is no nesting, it's easy!
            return zipfile.ZipFile(path)
