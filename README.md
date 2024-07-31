TTS采用微软的edge-tts开源库

```
pip install edge-tts
```

终端运行：

```
edge-tts --voice zh-CN-XiaoyiNeural --text "你好啊，我是智能语音助手" --write-media hello_in_cn.mp3
```

若在当前目录成功生成音频，TTS即为成功

### eged-tts服务器部署

进入宝塔面板后台，/www目录下，上传全部文件(到/www/edge_tts目录下.

在宝塔内安装docker,进入终端，执行

```
cd /www/edge_tts
chmod +x dockerRun.sh
./dockerRun.sh
```

运行成功后直接输入你的服务器ip:2020 检查一下是否能访问，如果打不开，那么可能你的服务器的防火墙没有开放，这里还需要去控制台去开通服务器的防火墙，还有宝塔面板的防火墙都需要开启下。

配音角色配置如下，可自行添加：

```
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
```

通过在浏览器输入以下网址进行访问

```
服务器ip:2020/dealAudio?text=欢迎使用tts&voice=xiaoxiao
```

- **text 是你需要转换的文本**

- **voice 是配音员 上面自己选**

  

需要注意的是，生成的mp3文件在不会自动删除，在宝塔计划任务里添加下列命令，选择合适的时间每天删除生成的mp3文件

```
rm -rf /var/lib/docker/overlay2/450addab32dbf038ad000f54735f13b3bf0f1258220c8ec51fd991f533ff7d3a/merged/flask_project/*.mp3
```

