from Preprocessor import Preprocessor
'''
a pass through file pre processor

txt -> text
jpg -> image
jpeg -> image
png -> image
bmp -> image
gif -> image
wav -> audio
mp3 -> audio
mp4 -> video

'''


class DefaultPreprocessor(Preprocessor):

    text_extensions = ['txt']
    image_extensions = ['jpg', 'jpeg', 'png', 'bmp', 'gif']
    audio_extensions = ['wav', 'mp3']
    video_extensions = ['mp4', 'mkv']

    def __init__(self):

        self.register_file_extension(self.text_extensions)
        self.register_file_extension(self.image_extensions)
        self.register_file_extension(self.audio_extensions)
        self.register_file_extension(self.video_extensions)

    '''
        returns dict of file paths
    '''

    def process_file(self, paths):
        results = {}
        for path in paths:
            for ext in self.text_extensions:
                if path.endswith(ext):
                    results[path]='text'

            for ext in self.image_extensions:
                if path.endswith(ext):
                    results[path]='image'

            for ext in self.audio_extensions:
                if path.endswith(ext):
                    results[path]='audio'

            for ext in self.video_extensions:
                if path.endswith(ext):
                    results[path]='video'

        return results
