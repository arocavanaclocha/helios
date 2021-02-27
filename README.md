
<!-- Title -->
<h1 align="center" id="helios">
    helios 
</h1>
<!-- Tag line -->
<h3 align="center">Lighting Scenario Laboratory.</h3>

----
Our goal is to achieve the best mixing light for portraiting by shooting images testing with many different light configurations.
The result is a matrix of pictures to compare the best lighting,  check sensor meassurements (distance, etc) and help portrating amateurs optimizing the scene.
<p align="center">
    ![Matrix portrait](imgs/portrait_matrix.jpg)
</p>
<h1 align="center" id="PyDMXControl">
    <img src="imgs/portrait_matrix.jpg" alt="Matrix portrait" width="500"/>
</h1>

# Features
1. New/load/save scenarios with different configurations 
2. Compose scenario lighting by configuring different DMX512 lighting Luminaires 
3. Define different light transitions (Scenes) with different brightness, color temperature (cct), rgb 
4. Define camera shooting configuration and sensors

# Process 
## Architect > Describe scenario
Name and Remarks of the current scenario. 
## Architect > Compose scenario lighting
Defines the LuminaireSet, that is:
* all Luminaires available in the scenario
* if the light is White Dimable, CCT Tunable or RGB
* a unique name
* and a spatial position in the scenario
## Architect > Plan scenes screenplay
Defines the different scenes. Later we will configure the light for each scene.
##  Architect > Configure light scene
For each scene, each luminaire or the whole scenario can be edited: 
* step up/down brightness or set brightness by value
* step up/down cct or set cct by value
* set rgb by value
* turn on/off light by switching
* balance light spatially
![Matrix portrait](imgs/LightComposer.png)

## Architect > Frameset dynamics editor
```
# Scene:      |00--------------------------->01|01--------------------------->02|
# Frame:      |00|01|02|03|04|05|06|07|08|09|10|00|01|02|03|04|05|06|07|08|09|10|
# Sensor:     |X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X-|
# Shoot:      |-X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X|
# Time:       |00|01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16|17|18|19|20|21|
# 
```
# Scenario.Frameset
#                       .sequence [0,1,2]
#                       .nr_frames=[25,25]
#

## Architect > Frameset dynamics editor > Define sequence and frames
# Order sequence of scenes and set the number of frames for each scene transition
architect.Scenario.Frameset.sequence=[0,1,2]
architect.Scenario.Frameset.nr_frames=[25,25]


## Architect > Frameset dynamics editor > Define times [msec]
```
#
#             |------------------------frame------------------------------|
#             |---------idle1---------|---shot---|-sensor-|-----idle2-----|
```

# Reference code
* [test reference code](https://github.com/arocavanaclocha/helios/blob/main/test.py)
* [DMX reference code](https://github.com/MattIPv4/PyDMXControl/tree/master/tests)
