import os

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from config import WORK_DIR


app = FastAPI()


@app.get('/api/meta')
def main():
    data = []
    for obj in os.listdir(WORK_DIR):
        try:
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
        except:
            print('Ошибка доступа к директории')
    return JSONResponse({'data': data})

