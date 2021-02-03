from numpy import arctan2,random,sin,cos,degrees

def searchProgram(tent_GPS, plane_GPS, heading):
  """Search program to determine the minimum rotation angle between heading and tent
  
  Parameters
  ----------
  tent_GPS : obj
    dictionary containing lat and long coordinates of the tent
  plane_GPS : obj
    dictionary containing lat and long coordinate of the plane
  heading : int
    bearings notation in radians

  Returns
  -------
  double
    returns the minimum rotation angle
  
  bool
    returns if rotation is counterclockwise or not

  """
  # STEP 1: Calculating Difference in Longitude
  dL = tent_GPS["lon"] - plane_GPS["lon"]

  # STEP 2: Converting Longitude and Latitude to corresponding XY coordinates
  X = cos(tent_GPS["lat"])* sin(dL)
  Y = cos(plane_GPS["lat"])*sin(tent_GPS["lat"]) - sin(plane_GPS["lat"])*cos(tent_GPS["lat"])* cos(dL)

  # Step 3: Calculate Bearings in Radians and then converting to degrees
  bearing = (degrees(arctan2(X,Y))+360) % 360

  print("BEARING:", bearing)

  '''
  Calculating Angle of Rotation
  '''
  cc = False
  rotate = 0.0
  
  # Step 1: Calculate the difference in Bearings:
  dB = bearing - heading

  # Step 2: Check for smallest rotation
  if dB > 0:
    if dB > 180:
      dB = 360-dB
      cc = True
    rotate = dB
  
  elif dB < 0:
    if dB < -180:
      dB = 360+dB
    else:
      dB *= -1
      cc = True
    rotate = dB
  
  print("Counter Clockwise:", cc, "ANGLE:", rotate)
  return {"angle": rotate, "counterclockwise": cc}
