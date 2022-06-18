# API for Taxi app backend

## Deploy on a VPS server
- Clone code in a path where no root access is needed
- install all dependencies (including uvicorn)
- create a file `sudo nano /etc/systemd/system/taxi.service`


```
[Unit]
Description=TAXI API
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=root
WorkingDirectory={Path to code in server}
ExecStart=uvicorn --host 0.0.0.0 --port 8000 main:app

[Install]
WantedBy=multi-user.target
```

- enable service and run it `sudo systemctl enable taxi` and `sudo systemctl start taxi`