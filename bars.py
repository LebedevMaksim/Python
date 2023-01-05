from progress.bar import ChargingBar
import time


with ChargingBar('Processing', max=20) as bar:
    for i in range(20):
        # Do some work
        time.sleep(.1)
        bar.next()
