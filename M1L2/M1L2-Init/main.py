from Motor import Motor

motor1 = Motor("Hijau", "Suzuki")
motor2 = Motor("Biru", "Yamaha")

print("Sebelum digas")
print(motor1.color)
print(motor1.brand)
print(motor1.speed)

print("Sesudah digas")
motor1.gas(100)
print(motor1.speed)