#fileros


ссылки на софт:
    Среда разработки Kinco DTOOLS и документация (EN)
    https://systemcontrol.ru/magazin/aon/kincohmi/softwareanddockincoautomation/softwarekincodtools

    краткая инструкция для Kinco DTOOLS на русском
    https://instruka.top/kinco-dtools-instrukcziya-na-russkom/
    https://systemcontrol.ru/articles/statyi/nastroikazashitiproekta

    https://kiplex.ru/help/documentation/
    https://rutube.ru/video/c8670e45fe833246b606c601483e95fd/

    modbus
    https://habr.com/ru/companies/advantech/articles/450234/
    МАТЧАСТЬ https://ipc2u.ru/articles/prostye-resheniya/modbus-rtu/
    https://www.modbustools.com/download.html
    https://ipc2u.ru/articles/prostye-resheniya/modbus-rtu/

    Weintek
    https://www.weintek.net/easybuilderpro.html
    https://owen-ufa.ru/shop/proizvoditeli/weintek/panel-operatora-7-mt8070ie-weintek/?etext=2202.KEuglKx45G0sDE7O8zX20mFrZHllaXhpc2t6emF1ZGI.b709ed3f9965e4d1c66fb8b7bfce73c7295501be&yclid=6394251974377996287

    python
    https://habr.com/ru/articles/339008/
    https://habr.com/ru/articles/339678/
    https://docs.golenishchev-electronics.ru/ru/smarttgm/pymodbus_smarttgm_guide
    https://www.licos-plc.ru/news/17.html
    https://rutube.ru/video/b6698084e0667853a2b805786dc160e8/
    https://ftp.owen.ru/CoDeSys3/98_Books/RaspberryCodesysV3Faq.pdf
    https://github.com/RAA80/python-owen/tree/main
    https://sourceforge.net/projects/pymodslave/files/latest/download   !! работает но float принимать не хочет

    pymodbus
    https://pymodbus.readthedocs.io/en/latest/ Документация и примеры кода, в т.ч. async

    others
    https://habr.com/ru/articles/680902/

    modbus linux
    https://www.embeddedpi.com/documentation/isolated-rs485/raspberry-pi-modbus-mbpoll-linux-installation
    https://www.modbusdriver.com/modpoll.html
    https://gitlab.com/helloysd/modpoll
    scadasploit.dev/posts/2021/07/hacking-modbus-tcp-simulation-in-linux/
    https://www.modbusdriver.com/diagslave.html
    https://redisant.com/mse
    https://shmmodbus.github.io/
    https://www.dalescott.net/modbus-development/

    ruby
    https://github.com/tallakt/modbus-cli

Устройства:
    1) Owen ПЛК110-60
    ModBus TCP 192.168.12.1:502 - Slave(Server)
    в проекте упоминается port 1200 - не знаю пока, есть ли в этом смысл?? ...

    Discrete Inputs —   дискретные входы устройства, доступны только для чтения.
                        Диапазон адресов регистров: с 10001 по 19999.
                        Имеют функцию «02» — чтение группы регистров

    Coils —             дискретные выходы устройства, или внутренние значения.
                        Доступны для чтения и записи.
                        Диапазон адресов регистров: с 20001 по 29999.
                        Имеет функции: «01» — чтения группы регистров,
                        «05» — запись одного регистра,
                        «15» — запись группы регистров

    Input Registers —   16-битные входы устройства.
                        Доступны только для чтения.
                        Диапазон адресов регистров: с 30001 по 39999.
                        Имеют функцию: «04» — чтение группы регистров

    Holding Registers — 16-битные выходы устройства, либо внутренние значения.
                        Доступны для чтения и записи.
                        Диапазон адресов регистров: с 40001 по 49999. Имеют



