from tkinter import*
import random

root=Tk()
root.title("Capitals and Capitals")
root.geometry("400x600")

Country_input=Entry(root,text="Country Section")
Capital_input=Entry(root,text="Capital Section")

Country_output=Label(root)
Capital_output=Label(root)

raCountry_output=Label(root)
raCapital_output=Label(root)

list_capital=[]
list_country=[]

def Show():
    country=Country_input.get()
    capital=Capital_input.get()
    
    list_capital.append(capital)
    list_country.append(country)
    
    Country_output["text"] = "Country : " + str(list_country)
    Capital_output["text"] = "Capital : " + str(list_capital)
    
def random_1():
    length_country=len(list_country)
    length_capital=len(list_capital)
    rando_country=random.randint(0,length_country-1)
    rando_capital=random.randint(0,length_capital-1)
    
    random_country_list=list_country[rando_country]
    random_capital_list=list_capital[rando_capital]
    
    raCountry_output["text"] = "Random Country : " + str(random_country_list)
    raCapital_output["text"] = "Random Capital : " + str(random_capital_list)
    
btn1=Button(root,text="Add to list",command=Show)


btn_rand=Button(root,text="Random List",command=random_1) 


Country_input.pack()
Capital_input.pack()

btn1.pack()

Country_output.pack()
Capital_output.pack()
    
btn_rand.pack()   

raCountry_output.pack()
raCapital_output.pack()

root.mainloop()