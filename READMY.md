### Удаляет невзаимные подкписки

 Для корректной работы вас нужно в файле `main.py` указать github токен
 Перейдите в настройки вашего GitHub аккаунта: GitHub Settings -> Developer settings -> Personal access tokens.

 Найдите ваш токен и убедитесь, что у него есть право user:follow.

 а так же укажите ваш никнейм 


 далее скачиваем `requests`

 ```zsh
  pip3 install requests --break-system-packages
```

после чего можете запускать 
```zsh
  python3 main.py
```