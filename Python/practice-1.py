# Konversi Temperature
print("\n|===== Program Konversi Temperatur =====|\n")

celcius: float = float(input("Masukkan suhu dalam celcius : "))

kelvin: float = celcius + 273
reamur: float = 4 / 5 * celcius
farenheit: float = 9 / 5 * celcius + 32

print("\nsuhu saat ini adalah ", celcius, "Celcius")
print("Kelvin\t : ", kelvin)
print("Farenheit : ", farenheit)
print("Reamur\t : ", reamur)