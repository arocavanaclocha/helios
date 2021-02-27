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

# Experiment Workflow 
The experiment consists of 3 phases:
Development   |  Production | Results
--------------|-------------|--------------
Prepares the experiment Settings | Executes the experiment | ETL (Extraction, Transformation and Load) and visualization of all data

## Development

Describe the testing scenario    | Manage Luminaires |Plan scenes' screenplay |Compose scenes' lighting |Frameset dynamics editor |
------------ | -------------|-----------------|-----------------|-----------------
Describe and compose spatialy the whole scenario |Manage the Luminaires' Master identifying luminaires and their characteristics.| Define the different lighting scenes accross the screenplay of the experiment. |For each scene, edit the combination of light brightness, CCT, RGB for all luminaires and balance light spatially from every orientation.|Define frameset scenes sequence order and number of frameshots between scenes. Define the sensors data sources to log data meanwhile. Define the timming for each task (camera shoot, sensors and idle times).

Follow this [test reference code](https://github.com/arocavanaclocha/helios/blob/main/test.py).
* Helios > Create instance
* Helios > Development > Describe the testing scenario
* Helios > Development > Manage Luminaires 
* Helios > Development > Plan scenes' screenplay
* Helios > Development > Compose scenes' lighting
* Helios > Development > Frameset dynamics editor

<p align="center">
    <img src="imgs/experiment_procedure.png" alt="Experiment Procedure" width="500"/>
    Experiment Procedure
</p>

The spatial scenario cube, where the DUT (Device Under Test) is in the center: 
<p align="center">
    <img src="imgs/SpatialComposer.png" alt="Spatial Composer Sketch" width="500"/>
</p>
The default size of the spatial scenario cube  is a 3x3 matrix. This will be used for balancing light in the xyz coordinates.


### Helios > Development > Manage Luminaires 
Add/delete/edit Luminaires and configure DMX512.


<p align="center">
    <img src="imgs/wireframe_luminaires.png" alt="Wireframe: Manage Luminaires" width="500"/>
</p>


###  Architect > Development > Plan scenes' screenplay
Defines the different scenes. Later we will configure the light for each scene.

###   Architect > Development > Compose scenes' lighting
For each scene, each luminaire or the whole scenario can be edited: 
* step up/down brightness or set brightness by value
* step up/down cct or set cct by value
* set rgb by value
* turn on/off light by switching
* balance light spatially
<p align="center">
    <img src="imgs/LightComposer.png" alt="Light Composer Sketch" width="500"/>
</p>

### Architect > Development > Frameset dynamics editor
Define frameset sequence order and number of frameshots between scenes:
```
# Scene:      |00--------------------------->01|01--------------------------->02|
# Frame:      |00|01|02|03|04|05|06|07|08|09|10|00|01|02|03|04|05|06|07|08|09|10|
# Sensor:     |X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X-|
# Shoot:      |-X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X|
# Time:       |00|01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16|17|18|19|20|21|
# 
```

### Architect > Development > Frameset dynamics editor > Define each time [msec]
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
## Production

## Post-Production
### Intelligence 
Show results (Portrait matrix, lighting settings, sensor data (Linear distance, LIDAR Movements heat map, temperature & Humidity, etc). Post-processing, like RGB histogram analysis, etc

Execute the experiment| Post-Processing
| Automate the process following the previous steps.|Show results (Portrait matrix, lighting settings and sensor data.

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
* [DMX reference code](https://github.com/MattIPv4/PyDMXControl/tree/master/tests)


# Status
- [x] Starting goals
- [ ] Features and wireframe 
- [ ] list syntax required (any unordered or ordered list supported)@mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [ ] ~~things not to do~~
