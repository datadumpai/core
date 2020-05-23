'''
Base class for processing a file.
Can set a list of file extensions
check extension/ or maybe just process file
- do we take in stream or file or both

invokes implementation class to process file

-target implementations image, text, doc , audio , video
text, audio and video are pass throughs to extractors
'''


class Preprocessor:
    _file_extensions=set()

    def register_file_extension(self, ext):
        if type(ext) is not list : ext = [ext]
        for e in ext:
            self._file_extensions.add(e)

    def check_extension(self, ext):
        return ext in self._file_extensions

    _tmp_directory='tmp/'

    def set_temp_dir(self, tmp):
        self._tmp_directory = tmp

    #TODO write results to temp file
    '''
    returns list of file paths
    '''
    def process_file(self, paths):
        pass
        # should write out temp files