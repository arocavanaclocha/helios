import numpy as np


class Luminaire():
  NR_PHOTONS = 3

  def FrontTop():
    xyz = np.zeros([3,3,3])
    xyz[0,0,:]=1
    return xyz

  def FrontLeft():
    xyz = np.zeros([3,3,3])
    xyz[0,:,0]=1
    return xyz

  def FrontRight():
    xyz = np.zeros([3,3,3])
    xyz[0,:,2]=1
    return xyz

  def FrontBottom():
    xyz = np.zeros([3,3,3])
    xyz[0,2,:]=1
    return xyz

  def FrontPerimetral():
    xyz = np.zeros([3,3,3])
    xyz[0,0,:]=1
    xyz[0,:,0]=1
    xyz[0,:,2]=1
    xyz[0,2,:]=1
    return xyz

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

