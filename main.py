#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AI.  @by PyCharm
# @File         : app.py
# @Time         : 2023/12/15 15:13
# @Author       : betterme
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  :

from meutils.serving.fastapi import App
from free_api.routers import chat_yuanbao, polling_openai_api_keys
from free_api.routers import chat_suno
from free_api.routers import files

app = App()

app.include_router(files.router, '/files-extraction/v1')

app.include_router(chat_yuanbao.router, '/yuanbao/v1')
app.include_router(polling_openai_api_keys.router, '/polling/v1')
app.include_router(chat_suno.router, '/suno/v1')

if __name__ == '__main__':
    app.run()

# python3 -m meutils.clis.server gunicorn-run smooth_app:app --pythonpath python3 --port 39006
