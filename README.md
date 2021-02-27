
<!-- Title -->
<h1 align="center" id="helios">
    helios 
</h1>
<!-- Tag line -->
<h3 align="center">Lighting Scenario Laboratory.</h3>

----
# What is the point of this?
Our goal is to achieve the best mixing light for portraiting by shooting images testing with many different light configurations and spatial positions.
The result is a matrix of pictures to compare the best lighting configuration, check sensor meassurements (distance, etc) and help portrating amateurs optimizing the scene.

<p align="center">
    <img src="imgs/portrait_matrix.jpg" alt="Matrix portrait" width="500"/>
</p>

# Features
1. New/load/save scenarios with different configurations 
2. Compose scenario lighting by configuring different DMX512 lighting Luminaires 
3. Define different light transitions (Scenes) with different brightness, color temperature (cct) and rgb 
4. Define camera shooting configuration and sensors to determine all possible transitions while camera shooting
5. Show results: Portrait matrix, sensor data, lighting configuration

# Wireframe  
1. Architect > Describe scenario
* Name and Remarks of the current scenario. 

2. Architect > Compose spatial scenario
Define the spatial matrix: 
<p align="center">
    <img src="imgs/SpatialComposer.png" alt="Spatial Composer Sketch" width="500"/>
</p>

3. Architect > Compose scenario lighting
Defines the LuminaireSet, that is:
* all Luminaires available in the scenario
* if the light is White Dimable, CCT Tunable or RGB
* a unique name
* and the spatial position in the scenario relative to the Person Under Test (PUT)
<p align="center">
    <img src="imgs/wireframe_luminaires.png" alt="Wireframe: master with luminaires" width="500"/>
</p>

4.  Architect > Plan scenes screenplay
Defines the different scenes. Later we will configure the light for each scene.

5.  Architect > Configure light scene
For each scene, each luminaire or the whole scenario can be edited: 
* step up/down brightness or set brightness by value
* step up/down cct or set cct by value
* set rgb by value
* turn on/off light by switching
* balance light spatially
<p align="center">
    <img src="imgs/LightComposer.png" alt="Light Composer Sketch" width="500"/>
</p>

6. Architect > Frameset dynamics editor
Define frameset sequence order and number of frameshots between scenes:
```
# Scene:      |00--------------------------->01|01--------------------------->02|
# Frame:      |00|01|02|03|04|05|06|07|08|09|10|00|01|02|03|04|05|06|07|08|09|10|
# Sensor:     |X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X-|
# Shoot:      |-X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X|
# Time:       |00|01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16|17|18|19|20|21|
# 
```

7. Architect > Frameset dynamics editor > Define each time [msec]
Configure frame times following this workflow:
* idle1: sleep time, no action
* shot: time after the camera shot
* sensor: time after meassuring sensors data
* idle2: time after finishing the whole process
 
<p align="center">
    <img src="imgs/Frameset.png" alt="Frameset Sketch" width="500"/>
</p>
```
#
#             |------------------------frame------------------------------|
#             |---------idle1---------|---shot---|-sensor-|-----idle2-----|
```

# Instalation
```
!git clone https://github.com/arocavanaclocha/helios.git 
!python /content/helios/core/helios.py
import helios.core.helios as helios
```
# Reference code
* [test reference code](https://github.com/arocavanaclocha/helios/blob/main/test.py)
* [DMX reference code](https://github.com/MattIPv4/PyDMXControl/tree/master/tests)
