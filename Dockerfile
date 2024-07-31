FROM registry.cn-hangzhou.aliyuncs.com/yrz_docker_images/python:3.8
COPY requirements.txt ./
RUN pip install  -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY . /flask_project/
#ADD ./tts.py /flask_project/
WORKDIR /flask_project/

CMD ["gunicorn", "edge-tts:app", "-c","gunicorn.conf"]
