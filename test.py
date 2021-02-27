# Helios > Create instance
lab = LightingLab()

#-------------------------------------------------------------------
# Helios > Development > Describe the testing scenario
#-------------------------------------------------------------------
# Define the current testing Scenario:
#  * name and remarks  
#  * created_date, updated_date
#  * the spatial scenario cube, where the DUT (Device Under Test) is in the center (default shape is 3x3x3)
helios.Scenario.new(name="Scenario: Laboratory iMM (PR3808)", remarks="Tests for defining most appropiate light for demo.", spatial_scenario_cube_shape=3)

#-------------------------------------------------------------------
# Helios > Development > Manage Luminaires 
#-------------------------------------------------------------------
# Defines the LuminaireSet, that is:
#  * all Luminaires available in the scenario
#  * if the light is White Dimable, CCT Tunable or RGB
#  * a unique name for referencing by name
#  * and the spatial scenario cube position in the scenario 
lab.Scenario.LuminaireSet.add(luminaire_args=[], luminaire_name="Top light", luminaire_start_channel=1, luminaire_type=[1,1,0], luminaire_xyz=helios.Luminaire.FrontTop())
lab.Scenario.LuminaireSet.add(luminaire_args=[], luminaire_name="Left light", luminaire_start_channel=2, luminaire_type=[1,1,0], luminaire_xyz=helios.Luminaire.FrontLeft())
lab.Scenario.LuminaireSet.add(luminaire_args=[], luminaire_name="Right light", luminaire_start_channel=3, luminaire_type=[1,1,0], luminaire_xyz=helios.Luminaire.FrontRight())
lab.Scenario.LuminaireSet.add(luminaire_args=[], luminaire_name="Bottom light", luminaire_start_channel=4, luminaire_type=[1,1,0], luminaire_xyz=helios.Luminaire.FrontBottom())
lab.Scenario.LuminaireSet.add(luminaire_args=[], luminaire_name="RGB perimetral ambient", luminaire_start_channel=5, luminaire_type=[1,1,1], luminaire_xyz=helios.Luminaire.FrontPerimetral())

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
# Helios > Development > Frameset dynamics editor
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


# Helios > Frameset dynamics editor > Define times [msec]
#
#             |------------------------frame------------------------------|
#             |---------idle1---------|---shot---|-sensor-|-----idle2-----|
#
lab.Scenario.Frameset.idle1_time = 1000
lab.Scenario.Frameset.shoot_time=500
lab.Scenario.Frameset.sensor_time=100
lab.Scenario.Frameset.idle2_time=500
 
movie = lab.Scenario.compose_frameset(scenes_configuration = architect.Scenario.Light.Photons,                                     
                                    transition_framesets = architect.Scenario.Frameset.nr_frames)
movie
