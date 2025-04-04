#number 2
def convert(farenheit):
  celcius=(5/9) *(farenheit-32)
 return(celcius)

farenheit=float(input("enter temperature in farenheit:"))
celcius=convert(farenheit)
print(f"temperature in celcius:{celcius:.2f}")
if celcius>20:
  print("its hot here")
else:
 print("its cold here")
