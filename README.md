### Минимальные системные требования
NVIDIA GPU с 16gb VRAM и выше

### Сборка докера
docker build --tag app_lerua .

### Запуск докера
docker run -it --gpus='all,"capabilities=compute"' \\
    --ipc=host --ulimit nofile=5000:5000 -p 80:80 app_lerua