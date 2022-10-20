import os

from fastapi.responses import JSONResponse

from apps import fapp
from config import WORK_DIR


@fapp.get('/api/meta')
def main():
    data = []
    for obj in os.listdir(WORK_DIR):
        filetype = 'file' if os.path.isfile(
            os.path.join(WORK_DIR, obj)
        ) else 'folder'
        creation_time = round(
            os.stat(
                os.path.join(WORK_DIR, obj)
            ).st_ctime
        )
        data.append({
            'name': obj,
            'type': filetype,
            'time': creation_time
        })
    return JSONResponse({'data': data})

