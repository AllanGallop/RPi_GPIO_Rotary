from RPi import GPIO
import threading, time

class Rotary:

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pins['clk'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.pins['dt'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.pins['sw'], GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def __init__(self,clk = None,dt = None,sw = None, tick = 2, bounce=500):
        if not clk or not dt or not sw:
            raise BaseException("Invalid Configuration: CLK, DT and SW must be specified")
        self.pins = {"clk":clk,"dt":dt,"sw":sw}
        self.ticks = tick
        self.bounce = bounce
        self.increment, self.decrement, self.switched, self.changed = None,None,None,None
        self.setup()


    def register(self, **params):
        if 'increment' in params:
            self.increment= params['increment']
        if 'decrement' in params:
            self.decrement = params['decrement']
        if 'pressed' in params:
            self.switched = params['pressed']
        if 'onchange' in params:
            self.changed= params['onchange'] 


    def watch(self, stop_event):
        clkLastState = GPIO.input(self.pins['clk'])
        counter = 0
        tick = 1
        pressed = 0
        while not stop_event.is_set():
            clkState = GPIO.input(self.pins['clk'])
            dtState = GPIO.input(self.pins['dt'])
            swState = GPIO.input(self.pins['sw'])
            
            if swState == 0:
                if pressed < int( (time.time()*1000)-self.bounce ):
                    if self.switched is not None:
                        pressed = int(time.time() * 1000)
                        self.switched()
            if clkState != clkLastState:
                if tick == self.ticks:
                    tick =1
                    if dtState != clkState:
                            counter += 1
                            if self.increment is not None:
                                self.increment()
                    elif dtState == clkState:
                            counter -= 1
                            if self.decrement is not None:
                                self.decrement()
                    if self.changed is not None:
                        self.changed(counter)
                else:
                    tick += 1
            clkLastState = clkState
            time.sleep(0.0025)

    def start(self):
        self.stop_event = threading.Event()
        self.th = threading.Thread(target=self.watch, args=[self.stop_event])
        self.th.setDaemon(True)
        self.th.start()
    
    def stop(self):
        self.stop_event.set()