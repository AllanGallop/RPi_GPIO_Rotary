## PYPI_Rotary
> KY040 Rotary Encoder Module


### Sections
* Description
* Features
* Install
* Usage
* Arguments


### Description
>A simple module for working with KY040 encoders on the Raspberry Pi SBC

### Features
1. Callback Functions
You can callback encoder actions such as `onchange`,`increment` and `decrement` to your own defined functions. /eg/:

    ```
    def MyFunction():
        print("Turned Clockwised!")
        
    ...
    encoder.register(increment=MyFunction)
    ...
    ```

2. Variable motion control
Specify how many 'ticks' of the encoder contribute to an action

3. Threading
This module uses threading to prevent blocking of the running script

4. Customisable pin configuration
Set which pins connect the encoder to the Raspberry PI GPIO

### Install
####Using PyPi: 
pip3 install RPi-GPIO-Rotary

### Arguments
##### Rotary [Constructor] (args)
Creates instance of rotary using the provided arguments: (clk,dt,sw,tck)

| Argument | Description | Optional | Default |
|----------|-------------|----------|---------|
| clk | Clock Pin | No | |
| dt | DT Pin | No | |
| sw | Button Switch Pin | Yes | |
| tck | Tick value (int), how many ticks contribute as a rotational movement | Yes | 2 |

##### Rotary.register(args)
Callbacks are optional and can be configured ad-hock providing the current rotary object is stopped / not started

| Argument | Description |
|----------|-------------|
| increment| Callback when encoder is turned clockwise|
| decrement| Callback when encoder is turned counter-clockwise|
|onchange | Callback on any change of rotation, returns current counter|
|pressed | Callback when button is pressed|

##### Rotary.start()
Starts monitoring the encoder

##### Rotary.stop()
Stops monitoring the encoder, useful when dealing with changes in the UI


### Examples
##### Simple

```
from RPi_GPIO_Rotary import rotary

## Define Callback functions
def cwTurn():
    print("CW Turn")

def ccwTurn():
    print("CCW Turn")

def buttonPushed():
    print("Button Pushed")

def valueChanged(count):
    print(count) ## Current Counter value

## Initialise (clk, dt, sw, ticks)
obj = rotary.Rotary(23,24,25,2)

 ## Register callbacks
obj.register(increment=cwTurn, decrement=ccwTurn)

## Register more callbacks
obj.register(pressed=buttonPushed, onchange=valueChanged) 

## Start monitoring the encoder
obj.start() 

...
## Your code here ##
...

## Stop monitoring
obj.stop()
```

##### Multple Encoders

```
from RPi_GPIO_Rotary import pypi

...
## Callback functions ##
...

## Setup First Encoder
menu_encoder = rotary.Rotary(23,24,25,2)
menu_encoder.register(increment=menu_up,decrement=menu_down,pressed=selected)
menu_encoder.start()

## Setup Second Encoder
volume_encoder = rotary.Rotary(17,27,22,1)
volume_encoder.register(onchange=setVolume,pressed=mute)
volume_encoder.start()

