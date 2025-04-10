'''
原项目作者:https://github.com/lyz1810/edge-tts
'''
import logging
import os
import re
import sys
import uuid
import io
import uvicorn
from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,

)

voiceMap = {
    "xiaoxiao": "zh-CN-XiaoxiaoNeural",
    "xiaoyi": "zh-CN-XiaoyiNeural",
    "yunjian": "zh-CN-YunjianNeural",
    "yunxi": "zh-CN-YunxiNeural",
    "yunxia": "zh-CN-YunxiaNeural",
    "yunyang": "zh-CN-YunyangNeural",
    "xiaobei": "zh-CN-liaoning-XiaobeiNeural",
    "xiaoni": "zh-CN-shaanxi-XiaoniNeural",
    "hiugaai": "zh-HK-HiuGaaiNeural",
    "hiumaan": "zh-HK-HiuMaanNeural",
    "wanlung": "zh-HK-WanLungNeural",
    "hsiaochen": "zh-TW-HsiaoChenNeural",
    "hsioayu": "zh-TW-HsiaoYuNeural",
    "yunjhe": "zh-TW-YunJheNeural",
    "Charline": "fr-BE-CharlineNeural",
    "Gerard": "fr-BE-GerardNeural",
}


def getVoiceById(voiceId):
    return voiceMap.get(voiceId)


# 删除html标签
def remove_html(string):
    regex = re.compile(r'<[^>]+>')
    return regex.sub('', string)


def createAudio(text, file_name, voiceId):
    new_text = remove_html(text)
    print(f"Text without html tags: {new_text}")
    voice = getVoiceById(voiceId)
    if not voice:
        return "error params"

    pwdPath = os.getcwd()
    filePath = pwdPath + "/" + file_name
    dirPath = os.path.dirname(filePath)
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)
    if not os.path.exists(filePath):
        # 用open创建文件 兼容mac
        open(filePath, 'a').close()

    script = 'edge-tts --voice ' + voice + ' --text "' + new_text + '" --write-media ' + filePath
    os.system(script)
    return filePath  # 返回生成的音频文件路径




@app.get('/dealAudio')
async def dealAudio(text: str = Query(), voice: str = Query()):
    file_name = str(uuid.uuid4()) + ".mp3"
    audio_file_path = createAudio(text, file_name, voice)

    # 设置响应头,浏览器将直接播放音频文件
    with open(audio_file_path, 'rb') as f:
        audio_data = f.read()

    return StreamingResponse(
        io.BytesIO(audio_data),
        media_type="audio/mpeg",
        headers={
            "Content-Disposition": "inline; filename=audio.mp3"
        }
    )


@app.get('/')
def index():
    return 'tts!'

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=2020)