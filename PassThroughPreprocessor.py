from Preprocessor import Preprocessor

class PassThroughPreprocessor(Preprocessor):

    extension_map={}

    def __init__(self, extension_map):
        self.extension_map = extension_map

    def process_file(self, paths):
        results = {}
        for path in paths:
            for k,v in self.extension_map.items():
                if path.endswith(k):
                    results[path]=v

        return results