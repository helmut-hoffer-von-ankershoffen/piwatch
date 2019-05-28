from fastapi import FastAPI
from .modules import PiTraffic
import time

SouthRed = PiTraffic.Traffic("SOUTH", "RED")
SouthYellow = PiTraffic.Traffic("SOUTH", "YELLOW")
SouthGreen = PiTraffic.Traffic("SOUTH", "GREEN")

EastRed = PiTraffic.Traffic("EAST", "RED")
EastYellow = PiTraffic.Traffic("EAST", "YELLOW")
EastGreen = PiTraffic.Traffic("EAST", "GREEN")

NorthRed = PiTraffic.Traffic("NORTH", "RED")
NorthYellow = PiTraffic.Traffic("NORTH", "YELLOW")
NorthGreen = PiTraffic.Traffic("NORTH", "GREEN")

WestRed = PiTraffic.Traffic("WEST", "RED")
WestYellow = PiTraffic.Traffic("WEST", "YELLOW")
WestGreen = PiTraffic.Traffic("WEST", "GREEN")

Buzz = PiTraffic.Buzzer()

app = FastAPI()

@app.get("/traffic/kubewatch-webhook")
@app.post("/traffic/kubewatch-webhook")
def handle():
    NorthRed.on()
    EastRed.on()
    SouthRed.on()
    WestRed.on()
    time.sleep(1)
    NorthRed.off()
    EastRed.off()
    SouthRed.off()
    WestRed.off()
    NorthYellow.on()
    EastYellow.on()
    SouthYellow.on()
    WestYellow.on()
    time.sleep(1)
    NorthYellow.off()
    EastYellow.off()
    SouthYellow.off()
    WestYellow.off()
    NorthGreen.on()
    EastGreen.on()
    SouthGreen.on()
    WestGreen.on()
    time.sleep(1)
    NorthGreen.off()
    EastGreen.off()
    SouthGreen.off()
    WestGreen.off()
    return {"Still": "Watching"}