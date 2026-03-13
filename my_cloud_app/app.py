import os
import datetime
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Мое облачное приложение</title>
    <style>
        body { font-family: Arial; max-width: 800px; margin: 50px auto; padding: 20px; }
        .info { background: #f0f0f0; padding: 20px; border-radius: 10px; }
        h1 { color: #0066cc; }
        .deploy-info { color: #666; font-size: 0.9em; }
    </style>
</head>
<body>
    <h1>🚀 Мое приложение в облаке!</h1>
    <div class="info">
        <p><strong>Статус:</strong> ✅ Приложение успешно развернуто</p>
        <p><strong>Сервер:</strong> {{ hostname }}</p>
        <p><strong>Время на сервере:</strong> {{ server_time }}</p>
        <p><strong>Порт:</strong> {{ port }}</p>
    </div>
    <div class="deploy-info">
        <p>Практика по теме: "Развертывание проектов в облаке"</p>
        <p>Создал: SENMART28</p>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(
        HTML_TEMPLATE,
        hostname=os.uname().nodename if hasattr(os, 'uname') else 'cloud-server',
        server_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        port=os.environ.get("PORT", 5000),
    )

@app.route("/health")
def health():
    """Endpoint для проверки работоспособности"""
    return {"status": "healthy", "timestamp": datetime.datetime.now().isoformat()}

@app.route("/info")
def info():
    """Информация о среде выполнения"""
    return {
        "python_version": os.sys.version,
        "environment": dict(os.environ),
        "working_dir": os.getcwd()
    }

@app.route("/owner")
def owner():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
    <title>Информация о влаельце сайта</title>
</head>
<body>
    <h1>Данный сайт создал SENMART28! (не YaKuts)</h1>
    <a href="https://github.com/SENMART28">Мой GitHub</a>
</body>
</html>
""")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("DEBUG", "False").lower() == "true"
    app.run(host='0.0.0.0', port=port, debug=debug)