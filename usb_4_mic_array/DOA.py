from tuning import Tuning
import usb.core
import usb.util
import time

dev = usb.core.find(idVendor=0x2886, idProduct=0x0018)

if dev:
    Mic_tuning = Tuning(dev)
    print(Mic_tuning.direction)
    while True:
        try:
            if Mic_tuning.read('SPEECHDETECTED') == 1:
                print(Mic_tuning.direction)
                time.sleep(1)
        except KeyboardInterrupt:
            break