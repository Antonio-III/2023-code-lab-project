import requests
import freecurrencyapi


client=freecurrencyapi.Client("INSERT_YOUR_OWN_API_KEY_HERE")
latest=client.latest()

def mod_rates(latest,target_currency,input_amount):
    modified={}
    mod_base=base_rates(latest)
    
    for key,val in mod_base.items():
        val=val/mod_base[target_currency] * input_amount
        val=float(f"{val:.3f}")
        
        modified[key]=val
    return modified


def base_rates(arg1):
    base={}
    for key,val in arg1["data"].items():
        val=float(f"{val:.3f}")
        base[key]=val
    return base

if __name__ =="__main__":

    currency=input("Which currency would you like to see exchange rates of? \n").upper()
    amount=int(input(f"With how much {currency} would you like to see exchange rates of?\n"))

    print(f"{amount} {currency} is equal to: \n")
    print(mod_rates(latest,currency,amount))

