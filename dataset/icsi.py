import os

from base import BaseDataset
from document import Document

from utils.zipping import extract_nested_zipfile


class ICSIDataset(BaseDataset):
    """
    Abstract Class for managing ICSI dataset.
    """

    def _data_files(self, zippath):
        """
        Iterates over the files in /keyphrase_data/ICSI.zip.
        """
        duczip = '/keyphrase_data/ICSI.zip'
        z = extract_nested_zipfile(zippath.rstrip('\/') + duczip)

        for filename in z.namelist():
            if self._valid_file(filename):
                with z.open(filename) as f:
                    yield f

    def _valid_file(self, filename):
        """
        Returns True if the file has to be taken
        into account.
        """
        raise Exception('_build_document function not implemented in ICSIDataset abstract class.')


    def _build_document(self, f):
        name = os.path.basename(f.name).decode('utf-8')
        return Document(name, f.read().decode('utf-8'))


class ICSIASRDataset(ICSIDataset):
    """
    Class for managing ICSI ASR_Output dataset.
    """

    def _valid_file(self, filename):
        return 'ASR_Output' in filename and \
            os.path.basename(filename)[0:3] in {'Bed', 'Bmr', 'Bro'}


class ICSIHumanTranscriptDataset(ICSIDataset):
    """
    Class for managing ICSI Human_Transcript dataset.
    """

    def _valid_file(self, filename):
        return 'Human_Transcript' in filename and \
            os.path.basename(filename)[0:3] in {'Bed', 'Bmr', 'Bro'}
