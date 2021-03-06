<!-- Title -->
<h1 align="center" id="helios">
    helios 
</h1>
<!-- Tag line -->
<h3 align="center">Lighting Scenario Laboratory.</h3>

----
# What's the point?
> The goal is to achieve the best light mixing by shooting multiple camera images with different lighting configurations. The result is a matrix of pictures for visual comparison of specialists. In the meantime, log sensor meassurements (like distance, etc) will be processed to help with the analysis. The proffesionals that can be interested are portrating amateurs, makeup artists, imaging for data science purposes and testing laboratories for better color rendering surfaces. All of them having in common the optimization of the best light.
<p align="center">
    <img src="imgs/portrait_matrix.jpg" alt="Matrix portrait" width="500"/>
</p>

# Hardware
The hardware will consist of:
* [ENTTEC DMX2USB](https://www.enttec.co.uk/en/product/controls/dmx-usb-interfaces/dmx-usb-interface/) 
* DMX compliant luminaires.


# Experiment Workflow 

The experiment consists of:
1. The system will make an explanation (text2speech), 
2. The system will ask the person under test if gives express consent of gathering their data and opinions according to local General Data Protection Regulation (GDPR). The whole process will be recorded.
3. After the consent, the survey starts. The person will keep static during the whole process.
4. The luminaires will change their status and in the meanwhile, the camera will take photos and the sensors will log with data for further analysis

<p align="center">
    <img src="imgs/experiment_procedure.png" alt="Experiment Procedure" width="900"/>
</p>

The design of the experiment consists of these phases:
Development   |  Pre-Production |  Production | Results
--------------|-------------|-------------|-------------
Prepares the experiment Settings | Prepares the experiment explanation and audio interaction. | Executes the experiment | ETL (Extraction, Transformation and Load) and visualization of all data

The development phase, consists of firstly, documenting the experiment by describing the testing scenario (e.g. 2 lights left-right and in the front, dimable and color tunable).
<p align="center">
    <img src="imgs/simple_2light_scenario.png" alt="Simple 2 light scenario" width="500"/>
</p>

The luminaires are registered in a database with its DMX512 information as well as spatial coordinates for better managing light. The light management will consist on brightness dimming, CCT (Color) tunning, setting RGB color and balancing light from different spatial locations.  

For the spatial balancing of light, we will create a **spatial scenario cube** or SCC, where the DUT (Device Under Test) is in the center: 
<p align="center">
    <img src="imgs/SpatialComposer.png" alt="Spatial Composer Sketch" width="500"/>
</p>
The default size of the spatial scenario cube  is a 3x3 matrix. This will be used for balancing light in the xyz coordinates.

Each luminaire is in one or several spatial coordinates.

For determining the whole range of light to be tested, we will define the different seed-scenes, e.g.:
1. Cold light coming from Left
2. Warm light coming from right
3. Warm light coming from everywhere 

Once created all scenes, you should compose scenes' lighting, editing each scene and luminaire: 
* step up/down brightness or set brightness by value
* step up/down cct or set cct by value
* set rgb by value
* turn on/off light by switching
* balance light spatially


After defining the scenes, we will create the Screenplay, that consists of:
* define the sequence of scenes (e.g. [0,1,2,3])
* define the ammount of frames for each transition (e.g. [25,25,25], 25 frames for each one of both transitions)


The resulting numpy array stores the whole lighting frameset:

```
 Scene:      |00------------------------------>01----------------------------->02---------------------------->03|
 Frame:      |00|01|02|03|04|05|06|07|08|09|10|00|01|02|03|04|05|06|07|08|09|10|00|01|02|03|04|05|06|07|08|09|10|
 Sensor:     |X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X-|
 Shoot:      |-X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X|
 Time:       |00|01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|26|27|28|29|30|31|32|
```

The last step before the execution is defining each time [msec]:
* idle1: sleep time, no action
* shot: time after the camera shot
* sensor: time after meassuring sensors data
* idle2: time after finishing the whole process
 
<p align="center">
    <img src="imgs/Frameset.png" alt="Frameset Sketch" width="500"/>
</p>

```
             |------------------------frame------------------------------|
             |---------idle1---------|---shot---|-sensor-|-----idle2-----|
```

## Development

Describe the testing scenario    | Manage Luminaires |Plan scenes' screenplay |Compose scenes' lighting |Frameset dynamics editor |
------------ | -------------|-----------------|-----------------|-----------------
Describe and compose spatialy the whole scenario |Manage the Luminaires' Master identifying luminaires and their characteristics.| Define the different lighting scenes accross the screenplay of the experiment. |For each scene, edit the combination of light brightness, CCT, RGB for all luminaires and balance light spatially from every orientation.|Define frameset scenes sequence order and number of frameshots between scenes. Define the sensors data sources to log data meanwhile. Define the timming for each task (camera shoot, sensors and idle times).

## Pre-Production
The system will explain with automatic audio, generated with text2speech, the following information:
* explanation of the experiment goals and procedure
* non disclosure agreement (NDA) for confidentiality purposes and other legal stuff like General Data Protection Regulation (GDPR)
* the whole process will be recorded with the express consent of the respondent
* to continue, the surveyed person must tell the name and give the consent.

## Production
Execute the process.


## Post-Production
Show results: 
* Portrait matrix, 
* lighting settings, 
* sensor data (Linear distance, LIDAR Movements heat map, temperature & Humidity, etc)
* Other post-processing, like RGB histogram analysis, etc


### Wireframe
Follow this [test reference code](https://github.com/arocavanaclocha/helios/blob/main/test.py).

* Helios > Development > Describe the testing scenario
* Helios > Development > Manage Luminaires 
* Helios > Development > Plan scenes' screenplay
* Helios > Development > Compose scenes' lighting
* Helios > Development > Configure screenplay dynamics
* Helios > Production > Action

Manage Luminaires
<p align="center">
    <img src="imgs/wireframe_luminaires.png" alt="Wireframe: Manage Luminaires" width="500"/>
</p>


Light Composer
<p align="center">
    <img src="imgs/LightComposer.png" alt="Light Composer Sketch" width="500"/>
</p>

# Model

```
    LightingLab
        |--Scenario
            |
            |--LuminaireSet
            |--ScreenPlay
            |--Light
            |--Frameset
            |--Settings      
            |--SpatialScenarioCube 
```


# Instalation
```
!git clone https://github.com/arocavanaclocha/helios.git 
!python /content/helios/core/IO.py
!python /content/helios/core/helios.py
import helios.core.IO as IO
import helios.core.helios as helios
    
```
# Reference code
* [DMX reference code](https://github.com/MattIPv4/PyDMXControl/tree/master/tests)
* [ENTTEC DMX2USB](https://www.enttec.co.uk/en/product/controls/dmx-usb-interfaces/dmx-usb-interface/)


# Status
- [x] Starting goals
- [ ] Features and wireframe 
- [ ] list syntax required (any unordered or ordered list supported)@mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [ ] ~~things not to do~~
