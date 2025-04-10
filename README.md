# Edge TTS Docker 服务

这是一个基于Edge TTS的文本转语音Docker服务。

## 构建镜像

```bash
docker build -t edge-tts-service .
```

## 运行容器

```bash
docker run -d -p 2020:2020 --name edge-tts edge-tts-service
```

## 使用说明

服务启动后，可以通过以下URL访问：

```
http://服务器IP:2020/dealAudio?text=要转换的文本&voice=语音类型
```

支持的语音类型：
- xiaoxiao
- xiaoyi
- yunjian
- yunxi
- yunxia
- yunyang
- xiaobei
- xiaoni
- hiugaai
- hiumaan
- wanlung
- hsiaochen
- hsioayu
- yunjhe
- Charline
- Gerard 