import numpy as np
import uuid
import time
from datetime import datetime
from gtts import gTTS 
from IPython.display import Audio   


class Luminaire():
  NR_PHOTONS = 3

class ScenesDirector():
  Scenes = []

  def __init__(self):
    pass
    
  def add(self, scene_name):
    scene = {
              "id": len(self.Scenes),
              "name": scene_name
            }
    self.Scenes.append(scene)  

  def load(self, scenes):
    pass
  
  def count(self):
    return len(self.Scenes)  

  def serialize(self):
    return self.Scenes


class LuminairesDirector():  
  Luminaires = []

  def __init__(self):
    pass
    
  def add(self, luminaire_name, luminaire_start_channel, luminaire_args, luminaire_type, luminaire_xyz):
    luminaire = {
                  "id": len(self.Luminaires),
                  "name": luminaire_name,
                  "start_channel": luminaire_start_channel,
                  "args": luminaire_args,
                  "type":   luminaire_type,
                  "xyz": luminaire_xyz, 
                  "status": 1
                }
    self.Luminaires.append(luminaire)  
    
  
  def load(self, luminaires):
    pass
  
  def count(self):
    return len(self.Luminaires)  

  def serialize(self):
    return self.Luminaires
  
  
  def switch(self, luminaire):
    """ Turns ON/OFF:
        1. If luminaire==-1 Turns ALL ON/OFF 
        2. Else, turns ALL ON/OFF the given luminaire.
    """
    if (luminaire==-1):
      for luminaire in self.Luminaires:  
        luminaire["status"] = not luminaire["status"]
      return -1
    else:
      luminaire = self.Luminaires[luminaire]
      luminaire["status"] = not luminaire["status"]
      return luminaire["status"]

    
class LightComposer():    
  Photons = []  
  
  def __init__(self):
    pass


  def reset(self, nr_luminaires, nr_scenes):
    #Deletes current scenes   
    self.Photons = np.zeros((nr_luminaires, Luminaire.NR_PHOTONS, nr_scenes))   
  
  def count(self):
    return self.nr_scenes
  
  def brightness(self, scene, step, luminaire=-1):
    """ Increases/decreases brightness on a step basis.
        1. If luminaire==-1 General brightness will be changed
        2. Else, the given luminaire will change brightness.
    """
    if (luminaire==-1):
      self.Photons[:,:,scene] += step
    else:
      self.Photons[luminaire,:,scene] += step
    self.Photons[luminaire,:,scene] = np.clip(self.Photons[luminaire,:,scene], 0, 255)

  def set_brightness(self, scene, value, luminaire=-1):
    if (luminaire==-1):
      self.Photons[:,:,scene] = value
    else:
      self.Photons[luminaire,:,scene] = value
    self.Photons[luminaire,:,scene] = np.clip(self.Photons[luminaire,:,scene], 0, 255)

  
  def cct(self, scene, step, luminaire=-1):      
    """ Increases/decreases cct on a step basis.
        1. If luminaire==-1 General cct will be changed
        2. Else, the given luminaire will change cct.
    """
    if (luminaire==-1):
      self.Photons[:,0,scene] += step
      self.Photons[:,1,scene] -= step
    else:
      self.Photons[luminaire,0,scene] += step
      self.Photons[luminaire,1,scene] -= step
    self.Photons[luminaire,:,scene] = np.clip(self.Photons[luminaire,:,scene], 0, 255)


  def set_cct(self, scene, value, luminaire=-1):
    if (luminaire==-1):
      self.Photons[:,0,scene] = 255 - value
      self.Photons[:,1,scene] = value
    else:
      self.Photons[luminaire,0,scene] = 255 - value
      self.Photons[luminaire,1,scene] = value
    self.Photons[luminaire,:,scene] = np.clip(self.Photons[luminaire,:,scene], 0, 255)


  def serialize(self):
    return self.Photons

  
  
class FramesetEditor():   
  FramesetParams = {}
  
  def __init__(self):
    self.sequence = []    
    self.nr_frames = [25,25]  
    self.idle1_time = 1000  
    self.shoot_time = 500
    self.sensor_time = 100
    self.idle2_time = 500

  
  @property
  def sequence(self):
    return self.FramesetParams["sequence"]

  @sequence.setter
  def sequence(self, sequence):
    self.FramesetParams["sequence"] = sequence


  @property
  def nr_frames(self):
    return self.FramesetParams["nr_frames"]

  @nr_frames.setter
  def nr_frames(self, nr_frames):
    self.FramesetParams["nr_frames"] = nr_frames
        

  @property
  def idle1_time(self):
    return self.FramesetParams["idle1_time"]

  @idle1_time.setter
  def idle1_time(self, idle1_time):
    self.FramesetParams["idle1_time"] = idle1_time


  @property
  def shoot_time(self):
    return self.FramesetParams["shoot_time"]

  @shoot_time.setter
  def shoot_time(self, shoot_time):
    self.FramesetParams["shoot_time"] = shoot_time
      
    
  @property
  def sensor_time(self):
    return self.FramesetParams["sensor_time"]

  @sensor_time.setter
  def sensor_time(self, sensor_time):
    self.FramesetParams["sensor_time"] = sensor_time
      
    
  @property
  def idle2_time(self):
    return self.FramesetParams["idle2_time"]

  @idle2_time.setter
  def idle2_time(self, idle2_time):
    self.FramesetParams["idle2_time"] = idle2_time
    

  def serialize(self):
    return self.FramesetParams


class ScenarioDirector():
  LuminaireSet = LuminairesDirector()
  ScreenPlay = ScenesDirector()  
  Light = LightComposer()
  Frameset = FramesetEditor()
  Settings = []
  SpatialScenarioCube = None
  scenario_path = ""  

  def __init__(self):
    self.LuminaireSet = LuminairesDirector()
    self.ScreenPlay = ScenesDirector()  
    self.Light = LightComposer()
    self.Frameset = FramesetEditor()
    
  @property
  def created_date(self):
    return self.Settings["created_date"]

  @created_date.setter
  def created_date(self, created_date):
    self.Settings["created_date"] = created_date
    
  @property
  def updated_date(self):
    return self.Settings["updated_date"]

  @updated_date.setter
  def updated_date(self, updated_date):
    self.Settings["updated_date"] = updated_date
    
  
  def FrontTop(self):
    size = self.SpatialScenarioCube.shape[0]
    xyz = np.zeros([size,size,size])
    xyz[0,0,:]=1
    return xyz

  def FrontLeft(self):
    size = self.SpatialScenarioCube.shape[0]
    xyz = np.zeros([size,size,size])
    xyz[0,:,0]=1
    return xyz
  
  def FrontRight(self):
    size = self.SpatialScenarioCube.shape[0]
    xyz = np.zeros([size,size,size])
    xyz[0,:,size-1]=1
    return xyz
  
  def FrontBottom(self):
    size = self.SpatialScenarioCube.shape[0]
    xyz = np.zeros([size,size,size])
    xyz[0,size-1,:]=1
    return xyz

  
  def FrontPerimetral(self):
    size = self.SpatialScenarioCube.shape[0]
    xyz = np.zeros([size,size,size])
    xyz[0,0,:]=1
    xyz[0,:,0]=1
    xyz[0,:,size-1]=1
    xyz[0,size-1,:]=1
    return xyz
    

  def new(self, name, remarks, spatial_scenario_cube_shape=3):
    self.Settings = {
          "id": uuid.uuid1(),
          "name": name,
          "remarks": remarks
        }    
    self.SpatialScenarioCube = np.zeros([spatial_scenario_cube_shape,spatial_scenario_cube_shape,spatial_scenario_cube_shape]) 
    self.created_date = datetime.now()
    self.updated_date = self.created_date

  # Movie Workflow: Development, Pre-production, Production, Post production, Distribution
  def compose_lights(self):
    """
      compose lights
    """
    self.Light.reset(self.LuminaireSet.count(), self.ScreenPlay.count())


  def compose_frameset(self, scenes_configuration, transition_framesets):
    """
      scenes_configuration: array of scenes with luminaire and photon settings 
      transition_framesets: array with nr of framesets required for each transition between scenes
    """
    nr_luminaires, nr_photons, nr_scenes = scenes_configuration.shape

    frameset = np.zeros([nr_luminaires, nr_photons, np.sum(transition_framesets)])

    for i in range(nr_scenes):
      if(i<nr_scenes-1):
        for j in range(len(transition_framesets)):  
          scene_start = scenes_configuration[:,:,i]
          scene_end = scenes_configuration[:,:,i+1]
          gradients = (scene_start - scene_end)
          gradients = gradients/(transition_framesets[j]-1)
          scene_n = scene_start
          for k in range(transition_framesets[j]):
            if (k==0):
              frameset[:,:,k+i*transition_framesets[j-1]] = scene_start
            else:
              scene_n = scene_n - gradients
              frameset[:,:,k+i*transition_framesets[j-1]] = np.rint(scene_n)
    
    return frameset

  
  # -----------------------------------------------------
  # AUTOMATE SURVEY EXPLANATION
  # -----------------------------------------------------
  @property
  def experiment_description(self):
    return self.Settings["experiment_description"]

  @experiment_description.setter
  def experiment_description(self, experiment_description):
    self.Settings["experiment_description"] = experiment_description
  
  
  def text2speech(text, language):
    myobj = gTTS(text=text, lang=language, slow=False) 
    sound_file = "text.wav"
    myobj.save(sound_file) 
    return sound_file
  
  
  
  def go_action(self, frameset):    
    nr_luminaires, nr_photons, nr_frames = frameset.shape

    for frame in range(nr_frames):
      print(f'Frame {frame} start.')
      time.sleep(self.Frameset.idle1_time/1000)
      self.shoot()    
      self.meassure()    
      time.sleep(self.Frameset.idle2_time/1000)
      print(f'End of frame {frame}.')
  
  def shoot(self):
      print("shoot")
      time.sleep(self.Frameset.shoot_time/1000)
      
  def meassure(self):
      print("meassure")
      time.sleep(self.Frameset.sensor_time/1000)

  def serialize(self):
    self.Settings["luminaires"] = self.LuminaireSet.serialize()
    self.Settings["scenarios"] = self.ScreenPlay.serialize()
    if(self.Light != None):
      self.Settings["dynamics"] = self.Light.serialize()
    return self.Settings 
    

class LightingLab():
  Scenario = ScenarioDirector()
  
  def __init__(self):
    pass

  def serialize(self):
    print(self.Scenario.serialize())


  def load(self, file_name):
    pass

  def save(self, file_name):
    pass

  def save_as(self, file_name):
    pass


  def load(self, folder_path):
    """ Returns file list of scenarios in a given folder.
    """
    return IO.search_files(folder_path, '.json')
