FROM python:3.10-slim

WORKDIR /app

# 安装edge-tts
RUN pip install fastapi edge-tts uvicorn -i https://pypi.tuna.tsinghua.edu.cn/simple

# 复制应用代码
COPY edge_tts.py /app/

# 暴露端口
EXPOSE 2020

# 启动命令
CMD ["uvicorn", "edge_tts:app", "--host", "0.0.0.0", "--port", "2020"] 