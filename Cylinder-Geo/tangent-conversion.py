import math

#Initializing PI and everything else
pi = 3.14159265359

xL = 0.0
offset = 0.0
ThetaP = 0.89

ux = 1.0
uxP = 0.0
uyP = 0.0

#Initializing our coordinates and cylinder
x = 2.0
y = 3.0

R = math.sqrt(x*x + y*y)
radius = 1.0

#Evaluating the angles and offset (tangent angles)
alpha = math.asin(radius/R)
phi = math.atan2(y, x)

if phi < 0.0:
    phi += 2.0*pi

if phi-alpha < 0.0:
    offset = 2.0*pi

Theta1 = phi-alpha+offset
Theta2 = phi+alpha+offset

print('Theta1: ' + str(Theta1))
print('Theta2: ' + str(Theta2))

#Building the linear and quadratic equation (intesecting angles)
m = math.tan(ThetaP)
b = y - m*x

descriminant = 4.0*pow(m*b,2)-4.0*(pow(m,2)+1.0)*(pow(b,2)-pow(radius,2))
sqrt_descriminant = math.sqrt(descriminant)

xL1 = (-2.0*m*b-sqrt_descriminant)/(2.0*(pow(m,2)+1.0))
xL2 = (-2.0*m*b+sqrt_descriminant)/(2.0*(pow(m,2)+1.0))

if abs(x-xL1) < abs(x-xL2):
    xL = xL1
else:
    xL = xL2

yL = m*xL + b

psi = math.atan2(yL,xL)
if psi < 0.0:
    psi += 2.0*pi

print('Psi: ' + str(psi))
print('Theta Prime: ' + str(ThetaP))

#Converting coordinates of incoming flow
ThetaConv = psi-pi/2

ThetaConvAng = ThetaConv*(180/pi)
uxP = ux*math.sin(ThetaConv)
uyP = ux*math.cos(ThetaConv)

print('Conversion Angle: ' + str(ThetaConv))
print('Ux Prime: ' + str(uxP))
print('Uy Prime: ' + str(uyP))
