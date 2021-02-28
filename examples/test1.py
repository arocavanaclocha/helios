!git clone https://github.com/arocavanaclocha/helios.git 
!python /content/helios/core/IO.py
!python /content/helios/core/helios.py
!pip install gTTS
import helios.core.IO as IO
import helios.core.helios as helios
from IPython.display import Audio   
    
  # Helios > Create instance
lab = helios.LightingLab()

#-------------------------------------------------------------------
# Helios > Development > Describe the testing scenario
#-------------------------------------------------------------------
# Define the current testing Scenario:
#  * name, remarks
#  * the spatial scenario cube, where the DUT (Device Under Test) is in the center (default shape is 3x3x3)
#  * auto: created_date, updated_date 
lab.Scenario.new(name="Scenario: Laboratory iMM (PR3808)", 
                 remarks="Tests for defining most appropiate light for demo.", 
                 spatial_scenario_cube_shape=3)

#-------------------------------------------------------------------
# Helios > Development > Manage Luminaires 
#-------------------------------------------------------------------
# Defines the LuminaireSet, that is:
#  * all Luminaires available in the scenario
#  * if the light is White Dimable, CCT Tunable or RGB
#  * a unique name for referencing by name
#  * and the spatial scenario cube position in the scenario 
lab.Scenario.LuminaireSet.add(luminaire_args=[], luminaire_name="Top light", luminaire_start_channel=1, luminaire_type=[1,1,0], luminaire_xyz=lab.Scenario.FrontTop())
lab.Scenario.LuminaireSet.add(luminaire_args=[], luminaire_name="Left light", luminaire_start_channel=2, luminaire_type=[1,1,0], luminaire_xyz=lab.Scenario.FrontLeft())
lab.Scenario.LuminaireSet.add(luminaire_args=[], luminaire_name="Right light", luminaire_start_channel=3, luminaire_type=[1,1,0], luminaire_xyz=lab.Scenario.FrontRight())
lab.Scenario.LuminaireSet.add(luminaire_args=[], luminaire_name="Bottom light", luminaire_start_channel=4, luminaire_type=[1,1,0], luminaire_xyz=lab.Scenario.FrontBottom())
lab.Scenario.LuminaireSet.add(luminaire_args=[], luminaire_name="RGB perimetral ambient", luminaire_start_channel=5, luminaire_type=[1,1,1], luminaire_xyz=lab.Scenario.FrontPerimetral())

#-------------------------------------------------------------------
# Helios > Development > Plan scenes' screenplay
#-------------------------------------------------------------------
lab.Scenario.ScreenPlay.add(scene_name="Scene #1")
lab.Scenario.ScreenPlay.add(scene_name="Scene #2")

#-------------------------------------------------------------------
# Helios > Development > Compose scenes' lighting
#-------------------------------------------------------------------
lab.Scenario.compose_lights()

scene = 0
#helios.Scenario.Light
#   ...brightness(scene=scene, step=+50, luminaire=-1)
#   ...set_brightness(scene=scene, value=255, luminaire=-1)
#   ...set_cct(scene=scene, value=155, luminaire=-1)
#   ...cct(scene=scene, step=-25, luminaire=-1)
#   ...switch(luminaire=-1)
#
lab.Scenario.Light.set_cct(scene=scene, value=155, luminaire=-1)

#-------------------------------------------------------------------
# Helios > Development > Configure screenplay dynamics
#-------------------------------------------------------------------
#
# Scene:      |00--------------------------->01|01--------------------------->02|
# Frame:      |00|01|02|03|04|05|06|07|08|09|10|00|01|02|03|04|05|06|07|08|09|10|
# Sensor:     |X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X-|
# Shoot:      |-X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X|
# Time:       |00|01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16|17|18|19|20|21|
# 
# Scenario.Frameset
#                       .sequence [0,1,2]
#                       .nr_frames=[25,25]
#

# Helios > Frameset dynamics editor > Define sequence and frames
# Order sequence of scenes and set the number of frames for each scene transition
lab.Scenario.Frameset.sequence=[0,1,2]
lab.Scenario.Frameset.nr_frames=[25,25]


# Define times [msec]
#
#             |------------------------frame------------------------------|
#             |---------idle1---------|---shot---|-sensor-|-----idle2-----|
#
lab.Scenario.Frameset.idle1_time = 1000
lab.Scenario.Frameset.shoot_time=500
lab.Scenario.Frameset.sensor_time=100
lab.Scenario.Frameset.idle2_time=500
 
movie = lab.Scenario.compose_frameset(scenes_configuration = lab.Scenario.Light.Photons,                                     
                                    transition_framesets = lab.Scenario.Frameset.nr_frames)
movie

#-------------------------------------------------------------------
# Helios > Production > Action
#-------------------------------------------------------------------
lab.Scenario.experiment_description = "This is an example of how to automate the survey initial testing procedure."
sound_file = lab.Scenario.text2speech(text=lab.Scenario.experiment_description, language='en')
Audio( sound_file, autoplay=True)   
#lab.Scenario.go_action(movie)
