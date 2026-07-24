class Mobil:
  warna = "Merah" 
  merek = "Audi"

  def drive(self):
    print(self.merek, "sedang mengemudi")
  
  def stop(self):
    print(self.merek, "berhenti")
  
  def about_car(self):
    print("Merek : ", self.merek, ", Warna :", self.warna)