def askDimension(PPrompt: str) -> float:
   Feed = float(input(f"Insert {PPrompt}: "))
   return Feed

PWidth = askDimension("width")
PHeight = askDimension("height")

def calcRectangleArea(PWidth: float, PHeight: float) -> float:
   Area = PWidth * PHeight
   return Area

Area = calcRectangleArea(PWidth, PHeight)
print("")
print(f"Area is {Area}²")
print("Program ending.")