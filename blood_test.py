def interface():
  print("Blood Test Analysis")
  while True:
    print("\nOptions")
    print("1 - HDL")
    print("9 - Quit")
    choice = input("Enter an option: ")
    if choice == "9":
        return
    elif choice == "1":
        HDL_driver()
  
def HDL_driver():
    #Get data input
    HDL = get_HDL_input()
    #Analyze that data
    analysis = analyze_HDL(HDL)
    #Output the data
    output_HDL(HDL, analysis)

def get_HDL_input():
    HDL = input("Enter HDL level: ")
    return int(HDL)

def analyze_HDL(HDL):
    if HDL >= 60:
        return "Normal"
    elif 40 <= HDL < 60:
        return"Borderline Low"
    else:
        return "Low"

def output_HDL(HDL, analysis):
    print("The HDL entered as {}".format(HDL))
    print("This HDL level is {}".format(analysis))
    

interface()