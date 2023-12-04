
try:
    import RPi.GPIO as GPIO
except (ImportError, RuntimeError):
    class GPIO:
        LOW = 0
        HIGH = 1

        OUT = 0
        IN = 1

        BOARD = 10
        BCM = 11

        PUD_OFF = 20
        PUD_UP = 21
        PUD_DOWN = 22

        RISING = 31
        FALLING = 32
        BOTH = 33

        SERIAL = 40
        SPI = 41
        I2C = 42
        HARD_PWM = 43

        @classmethod
        def setmode(cls, mode):
            print(f'RPI.GPIO.setmode -> {mode}')

        @classmethod
        def setwarnings(cls, flag):
            print(f'RPI.GPIO.setwarnings -> {mode}')

        @classmethod
        def setup(cls, channel, state, initial=LOW, pull_up_down=PUD_OFF):
            print(f'RPI.GPIO.setup -> {channel}, {state}, {initial}, {pull_up_down}')

        @classmethod
        def output(cls, channel, outmode):
            print(f'RPI.GPIO.output -> {channel}, {outmode}')

        @classmethod
        def input(cls, channel):
            print(f'RPI.GPIO.input -> {channel}')
            return True

        @classmethod
        def cleanup(cls, channel=None):
            print(f'RPI.GPIO.cleanup -> {channel}')

        @classmethod
        def wait_for_edge(cls, channel, event, timeout=None):
            print(f'RPI.GPIO.wait_for_edge -> {channel}, {event}, {timeout}')
            return channel

        @classmethod
        def add_event_detect(cls, channel, event, callback=None, bouncetime=None):
            print(f'RPI.GPIO.add_event_detect -> {channel}, {event}, {callback}, {bouncetime}')

        @classmethod
        def add_event_callback(cls, channel, callback, bouncetime=None):
            print(f'RPI.GPIO.add_event_callback -> {channel}, {callback}, {bouncetime}')

        @classmethod
        def event_detected(cls, channel):
            print(f'RPI.GPIO.event_detected -> {channel}')

        @classmethod
        def remove_event_detect(cls, channel):
            print(f'RPI.GPIO.remove_event_detect -> {channel}')

        @classmethod
        def gpio_function(cls, channel):
            print(f'RPI.GPIO.gpio_function -> {channel}')
            return cls.IN

        class PWM:
            def __init__(self, channel, frequency):
                print(f'RPI.GPIO.PWM.__init__ -> {channel}, {frequency}')

            def start(self, duty_cycle):
                print(f'RPI.GPIO.PWM.start -> {duty_cycle}')

            def stop(self):
                print(f'RPI.GPIO.PWM.stop')

            def ChangeFrequency(self, frequency):
                print(f'RPI.GPIO.PWM.ChangeFrequency')

            def ChangeDutyCycle(self, duty_cycle):
                print(f'RPI.GPIO.PWM.ChangeDutyCycle -> {duty_cycle}')


class Pin:
    def __init__(self, channel, state , initial, pull_up_down):
        self.__channel = channel
        self.__state = state
        self.__initial = initial
        self.__pud = pull_up_down
        GPIO.setup(self.__channel, self.__state, self.__initial, self.__pud)

    def input(self) -> bool:
        if self.__state == GPIO.IN:
            return GPIO.input(self.__channel)
        else:
            raise ValueError('This channel state is OUT.')

    def output(self, value: bool):
        if self.__state == GPIO.OUT:
            GPIO.output(self.__channel, value)
        else:
            raise ValueError('This channel state is IN.')
