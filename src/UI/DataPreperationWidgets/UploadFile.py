from ipyfilechooser import FileChooser
from ipywidgets import AppLayout, Label


class UploadFile(AppLayout):
    def __init__(self, **kwargs):

        self.header = Label(value="Please, select your data file:")
        self.uploader = FileChooser(
            path="db/Datasets", sandbox_path="db", filter_pattern="*.txt"
        )

        super().__init__(
            header=self.header,
            center=self.uploader,
            justify_items="center",
            align_items="center",
            **kwargs
        )
