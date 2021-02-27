<!-- Title -->
<h1 align="center" id="helios">
    helios 
</h1>
<!-- Tag line -->
<h3 align="center">Lighting Scenario Laboratory.</h3>

----
# What's the point?
> The goal is to achieve the best light mixing by shooting multiple camera images with different lighting configurations. The result is a matrix of pictures to compare the best lighting configuration. In the meantime, log sensor meassurements (like distance, etc) will be processed to help with the analysis. The proffesionals that can be interested are portrating amateurs, imaging for data science purposes and testing laboratories for better color rendering surfaces. All of them having in common the optimization of the best light.

<p align="center">
    <img src="imgs/portrait_matrix.jpg" alt="Matrix portrait" width="500"/>
</p>

# Features 

Define the testing Scenario    | Manage and configure each Luminaire |Plan scenes' screenplay |Configure light for each scene |Frameset dynamics editor |Execute the experiment| Post-Processing
------------ | -------------|-----------------|-----------------|-----------------|-----------------|-----------------
Describe and compose spatialy the whole scenario |Manage the Luminaires' Master identifying luminaires and their characteristics.| Define the different lighting scenes accross the screenplay of the experiment. |For each scene, edit the combination of light brightness, CCT, RGB for all luminaires and balance light spatially from every orientation.|Define frameset scenes sequence order and number of frameshots between scenes. Define the sensors data sources to log data meanwhile. Define the timming for each task (camera shoot, sensors and idle times).| Automate the process following the previous steps.|Show results, like Portrait matrix, lighting configuration, sensor data (Linear distance, LIDAR Movements heat map, temperature & Humidity, etc). Post-processing, like RGB histogram analysis, etc


<p align="center">
    <img src="imgs/experiment_procedure.png" alt="Experiment Procedure" width="500"/>
</p>


# Wireframe  
**PREPARE EXPERIMENT SETTINGS**


1. Architect > Describe scenario
* name and remarks of the current scenario. 
* creation_date, updated_date, creation_user, updated_user
 
2. Architect > Compose spatial scenario
Define the spatial matrix: 
<p align="center">
    <img src="imgs/SpatialComposer.png" alt="Spatial Composer Sketch" width="500"/>
</p>

3. Architect > Compose scenario lighting
Manage the Luminaires' Master. 
Add/delete/edit Luminaires and configure DMX512 

Defines the LuminaireSet, that is:
* all Luminaires available in the scenario
* if the light is White Dimable, CCT Tunable or RGB
* a unique name
* and the spatial position in the scenario relative to the Device or person Under Test (DUT)
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

# Model

```
    Scenario
        |
        |--LuminaireSet
        |--ScreenPlay
        |--Light
        |--Frameset
        |--Settings
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


# Status
- [x] Starting goals
- [ ] Features and wireframe 
- [ ] list syntax required (any unordered or ordered list supported)@mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [ ] ~~things not to do~~
