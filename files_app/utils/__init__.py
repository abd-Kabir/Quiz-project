from files_app.models import Uploads
from quiz_4.settings import MEDIA_ROOT
from quiz_4.utils import unique_code, process_name, get_extension, media_path
from quiz_4.utils import join_path


def upload(file) -> Uploads:
    code = unique_code()
    new_name = process_name(code, get_extension(file.name))
    for chunk in file.chunks():
        with open(join_path(MEDIA_ROOT, 'uploads', new_name), mode="wb+") as write_file:
            write_file.write(chunk)

    instance = Uploads()
    instance.code = code
    instance.original_name = file.name
    instance.path = media_path(new_name)
    instance.size = file.size
    instance.content_type = file.content_type
    instance.new_name = new_name
    instance.save()
    return instance
