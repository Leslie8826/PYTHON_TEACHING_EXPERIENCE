import time
import numpy as np
import matplotlib.pyplot as plt

n=0
speedMax710 = 100
speedMin710 = 80

speedMax47 = 60
speedMin47 = 40

speedMax04 = 25
speedMin04 = 5

speedTrack = np.array([0,0,0,0,0,0,0,0,0,0,0,0])

while (n<=10):
  #Level 1
  if 0<=n<4:
    if n==0:
      print("LEVEL 1")
      time.sleep(2)
      print("You start at 6 MetroTech, Brooklyn")
      time.sleep(2)
      print("READY")
      time.sleep(1)
      print('SET')
      time.sleep(1)
      print("GOOOOO!!!")
      time.sleep(1)
    speedTrack[n] = float(input("\n Type your speed: "))
    if speedTrack[n]>speedMax710:
      print("\n You get arrested by the police\n")
      time.sleep(2)
      print("GAME OVER!!!")
      break
      
    if speedTrack[n]<speedMin710:
      print("\n You are a danger to others. Step out of your car\n")
      time.sleep(3)
      print("GAME OVER!!!")
      break
    
    if speedMin710<speedTrack[n]<=speedMin710+5:
      print("Increase your speed you are on the highway")
    
    if speedMax710-5<=speedTrack[n]<speedMax710:
      print(" Wooow slow down!!! There is a speed limit even on the highway")
    
  # Level 2
  if 4<=n<7:
    if n==4:
      time.sleep(2)
      print("\n Congrats! LEVEL 1 COMPLETE!!")
      time.sleep(2)
      print("\n This is level 2")
      time.sleep(2)
      print("\n You are downtown manhattan! you still have a long way to go")
      time.sleep(1)
      print("\n BEWARE OF THE SPEED LIMITS!!!!")
    time.sleep(2)
    speedTrack[n] = float(input("\n Type your speed: "))
    if speedTrack[n]>speedMax47:
      print("\n You get arrested by the police \n")
      time.sleep(2)
      print("GAME OVER!!!")
      break
     
    if speedTrack[n]<speedMin47:
      print("\n You are a danger to others. Step out of your car \n")
      time.sleep(3)
      print("GAME OVER!!!")
      break
    
    if speedMin47<speedTrack[n]<=speedMin47+10:
      print("Go faster please!!")
    
    if speedMax47-10<=speedTrack[n]<speedMax47:
      print(" You've got to slow down")
      
  # Level 3
  if 7<=n<10:
    if n==7:
      print("\n CONGRATULATIONS!! LEVEL 2 COMPLETE")
      time.sleep(2)
      print("\n This is Level 3. You are now in midtown manhattan!")
      time.sleep(2)
      print("\n Uptown Manhattan is your next stop!! Keep going!!")
    speedTrack[n] = float(input("\nType your speed: "))
    if speedTrack[n]>speedMax04:
      print("You get arrested by the police\n")
      time.sleep(3)
      print("GAME OVER!!!")
      break
      
    if speedTrack[n]<speedMin04:
      print("You are a danger for others. Step out of your car\n")
      time.sleep(3)
      print("GAME OVER!!!")
      break
    
    if speedMin04<speedTrack[n]<speedMin04+5:
      print("Speed up")
    
    if speedMax04-5<=speedTrack[n]<speedMax04:
      print(" SLOW DOWN YOU'RE IN TOWN!!!")
  #else:
  if n==10:
    print("\n You made it to uptown Manhattan")
    time.sleep(3)
    print("CONGRATULATIONS YOU WIN")
  n = n+1

print("\n Your speed values: \n")
time.sleep(2)
for i in range(0, 10):
  print(speedTrack[i]," ", end="")

time.sleep(2)
print("\n Your speed graph \n")
plt.plot(speedTrack)
plt.ylabel('Speed')
plt.show()
