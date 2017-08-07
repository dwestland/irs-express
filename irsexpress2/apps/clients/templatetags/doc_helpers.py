
from django import template

register = template.Library()


@register.filter
def doc_icon_class(filenameext):
    # translate file name/extension to the class of FontAwesome icon
    unknownfileclass = "fa fa-file-o"
    ext = filenameext.split('.')[-1].lower()
    filetypes = {
        'pdf': 'fa fa-file-pdf-o',
        'xls': 'fa fa-file-excel-o', 'xlsx': 'fa fa-file-excel-o', 'csv': 'fa fa-file-excel-o',
        'doc': 'fa fa-file-word-o', 'docx': 'fa fa-file-word-o',
        'txt': 'fa fa-file-text',
        'jpg': 'fa fa-file-image-o', 'jpeg': 'fa fa-file-image-o',
        'bmp': 'fa fa-file-image-o', 'gif': 'fa fa-file-image-o',
        'png': 'fa fa-file-image-o', 'tiff': 'fa fa-file-image-o', 'tif': 'fa fa-file-image-o',
        'zip': 'fa fa-archive-o', 'rar': 'fa fa-archive-o',
        'mp3': 'fa fa-file-sound-o', 'wav': 'fa fa-file-sound-o',
        'mp4': 'fa fa-file-video-o', 'avi': 'fa fa-file-video-o',
    }
    return filetypes.get(ext) or unknownfileclass
