import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image
import api_key
from api_key import base_rates, mod_rates
class App(tk.Tk):
    # api data
    client=api_key.client
    
    
    # colors
    bg_color = '#02111F'
    white = '#FFFFFF'
    black= '#000000'
    blue = '#22D3EE' # light blue
    dark_blue='#1D72BA' # currency # entry
    red = '#FF0000' #right-side
    dark_red="#E11414"
    violet = '#7F007F' #shared
    gray='#3C3C3C' # placeholder text

    def __init__(self):
        super().__init__()
        self.title('Currency Converter')
        self.geometry('1200x750')
        self['bg']=App.bg_color
        self.resizable(0,0)
        # Presets
        self.font=('Tahoma',16)
        self.bg_preset={'bg':App.bg_color}
        
        # Images
            # Blue 
        self.rounded_blue=self.resize("Images/Rectangle 1.png",100,50)
            # big blue
        self.rounded_big_blue=self.resize('Images/Rectangle 1.png',110,50)
            # Dark blue
        self.rounded_dark_blue=self.resize("Images/Rectangle 2.png",100,50)
            # Red
        self.rounded_red=self.resize("Images/Rectangle 3.png",140,50)
            # Gray
        self.rounded_gray=self.resize("Images/Rectangle 4.png",100,50)
            # small Gray
        self.rounded_small_gray=self.resize("Images/Rectangle 5.png",30,30)

            # Map
        self.map_img=self.resize("Images/Map.png",835,415)

        # Flags are 48x48
        self.flags={
            "EUR":ImageTk.PhotoImage(file="Images/Flags/Unknown.png"),"USD":ImageTk.PhotoImage(file="Images/Flags/United-States.png"),"JPY":ImageTk.PhotoImage(file="Images/Flags/Japan.png"),"BGN":ImageTk.PhotoImage(file="Images/Flags/Bulgaria.png"),"CZK":ImageTk.PhotoImage(file="Images/Flags/Czech-Republic.png"),"DKK":ImageTk.PhotoImage(file="Images/Flags/Denmark.png"),"GBP":ImageTk.PhotoImage(file="Images/Flags/United-Kingdom.png"),"HUF":ImageTk.PhotoImage(file="Images/Flags/Hungary.png"),"PLN":ImageTk.PhotoImage(file="Images/Flags/Poland.png"),"RON":ImageTk.PhotoImage(file="Images/Flags/Romania.png"),"SEK":ImageTk.PhotoImage(file="Images/Flags/Sweden.png"),"CHF":ImageTk.PhotoImage(file="Images/Flags/Switzerland.png"),"ISK":ImageTk.PhotoImage(file="Images/Flags/Iceland.png"),"NOK":ImageTk.PhotoImage(file="Images/Flags/Norway.png"),"HRK":ImageTk.PhotoImage(file="Images/Flags/Croatia.png"),"RUB":ImageTk.PhotoImage(file="Images/Flags/Russia.png"),"TRY":ImageTk.PhotoImage(file="Images/Flags/Turkey.png"),"AUD":ImageTk.PhotoImage(file="Images/Flags/Australia.png"),"BRL":ImageTk.PhotoImage(file="Images/Flags/Brazil.png"),"CAD":ImageTk.PhotoImage(file="Images/Flags/Canada.png"),"CNY":ImageTk.PhotoImage(file="Images/Flags/China.png"),"HKD":ImageTk.PhotoImage(file="Images/Flags/Hong-Kong.png"),"IDR":ImageTk.PhotoImage(file="Images/Flags/Indonesia.png"),"ILS":ImageTk.PhotoImage(file="Images/Flags/Israel.png"),"INR":ImageTk.PhotoImage(file="Images/Flags/India.png"),"KRW":ImageTk.PhotoImage(file="Images/Flags/South-Korea.png"),"MXN":ImageTk.PhotoImage(file="Images/Flags/Mexico.png"),"MYR":ImageTk.PhotoImage(file="Images/Flags/Malaysia.png"),"NZD":ImageTk.PhotoImage(file="Images/Flags/New-Zealand.png"),"PHP":ImageTk.PhotoImage(file="Images/Flags/Philippines.png"),"SGD":ImageTk.PhotoImage(file="Images/Flags/Singapore.png"),"THB":ImageTk.PhotoImage(file="Images/Flags/Thailand.png"),"ZAR":ImageTk.PhotoImage(file="Images/Flags/South-Africa.png"),"UNK":ImageTk.PhotoImage(file="Images/Flags/Unknown.png")
                    }
        self.symbols={"EUR":"€","USD":"$","JPY":"¥","BGN":"лв","CZK":"Kč","DKK":"kr","GBP":"£","HUF":"Ft","PLN":"zł","RON":"lei","SEK":"kr","CHF":"Fr.","ISK":"kr","NOK":"kr","HRK":"kn","RUB":"₽","TRY":"₺","AUD":"A$","BRL":"R$","CAD":"C$","CNY":"CN¥","HKD":"HK$","IDR":"Rp","ILS":"₪","INR":"₹","KRW":"₩","MXN":"MX$","MYR":"RM","NZD":"NZ$","PHP":"₱","SGD":"S$","THB":"฿","ZAR":"R","UNK":"?"}
        
        # text    - font size, line height, color, text-shadow
        # visual  - bg-color, border, border-rad, box-shadow
        # misc    - transition

        # Widgets
            # "Currency" 
        self.title_one=tk.Label(self,**self.widget_preset(App.bg_color,App.blue,('Tahoma',20,'bold')),text='Currency')
        self.title_one.place(relx=.45,rely=.03,anchor='n')
        
            # "Converter"
        self.title_two=tk.Label(self,**self.widget_preset(App.bg_color,App.white,('Tahoma',20,'bold')),text='Converter')
        self.title_two.place(relx=.56,rely=.03,anchor='n')

            # Base currency Frame 160x150
        self.base_frame=tk.Frame(self, bg=App.bg_color)
        self.base_frame.place(relx=.138,rely=.147,relwidth=.133,relheight=.2)

                # "Base" text
        self.base_text=tk.Label(self.base_frame,**self.widget_preset(App.bg_color,App.blue),text='Base')
        self.base_text.place(relx=.531,relwidth=.306,relheight=.16)

                # Widget flag
        self.base_flag=tk.Label(self.base_frame,image=self.flags["EUR"],bg=App.bg_color)
        self.base_flag.place(rely=.233)


                # Frame for base input currency
        self.base_curr_frame=tk.Frame(self.base_frame)
        self.base_curr_frame.place(relx=.375,rely=.233,relwidth=.625,relheight=.333)

                    # Image widget
        self.base_curr_container=tk.Label(self.base_curr_frame,image=self.rounded_blue)
        self.base_curr_container.place(relwidth=1,relheight=1)
        
                    # base currency type entry field 
        self.base_curr_input=tk.StringVar()
        self.base_curr_entry=tk.Entry(self.base_curr_container,**self.widget_preset(App.white,App.gray),borderwidth=0,highlightthickness=0,textvariable=self.base_curr_input)
        self.base_curr_entry.place(relwidth=1,relheight=1)

                    # Placeholder text for the entry field
        self.base_curr_entry.insert(0,"USD..")
                    # Event 
        self.base_curr_entry.bind("<FocusIn>",self.base_rm_curr)


                # Currency Symbol
        self.base_curr_symbol=tk.Label(self.base_frame,**self.widget_preset(App.bg_color,App.blue))
        self.base_curr_symbol.place(relx=.113,rely=.76)

                # Trace for line 94 and 106
        self.base_curr_input.trace_add('write',self.base_on_curr_input)

                # Frame for Currency amount
        self.base_amount_frame=tk.Frame(self.base_frame)
        self.base_amount_frame.place(relx=.375,rely=.667,relwidth=.625,relheight=.333)

                    # Img widget
        self.base_amount_container=tk.Label(self.base_amount_frame,image=self.rounded_dark_blue)
        self.base_amount_container.place(relwidth=1,relheight=1)
        
                    # Entry 
        self.base_amount_input=tk.StringVar()
        self.base_amount_entry=tk.Entry(self.base_amount_container,borderwidth=0,highlightthickness=0,**self.widget_preset(App.white,App.gray),textvariable=self.base_amount_input)
        self.base_amount_entry.place(relwidth=1,relheight=1)
        
                    # Placeholder
        self.base_amount_entry.insert(0,"0..")
        
                    # Event
        self.base_amount_entry.bind("<FocusIn>",self.base_rm_amount)


        # "->"
        self.middle_arrow=tk.Label(self,**self.widget_preset(App.bg_color,App.white),text='->')
        self.middle_arrow.place(relx=.5,rely=.21,anchor='c')

        # "Latest" frame
        self.latest_frame=tk.Frame(self)
        self.latest_frame.place(relx=.5,rely=.3,anchor='c',relwidth=.092,relheight=.066)

            # Image
        self.latest_container=tk.Label(self.latest_frame,image=self.rounded_big_blue)
        self.latest_container.place(relwidth=1,relheight=1)

                # "Latest" string
        self.latest=tk.Button(self.latest_container,**self.widget_preset(App.black,App.white,('Tahoma',16,'bold')),border=0,activebackground=App.white,activeforeground=App.bg_color,text='Latest',command=self.get_latest)
        self.latest.place(relwidth=1,relheight=1)


        # Target Frame
        self.targ_frame=tk.Frame(self,bg=App.bg_color)
        self.targ_frame.place(relx=.725,rely=.147,relwidth=.167,relheight=.253)

            # "Convert to"
        self.targ_text=tk.Label(self.targ_frame,**self.widget_preset(App.bg_color,App.red),text='Convert to')
        self.targ_text.place(relx=.375)

            # Flag
        self.targ_flag=tk.Label(self.targ_frame,image=self.flags["EUR"],bg=App.bg_color)
        self.targ_flag.place(rely=.175)

            # Target currency's frame
        self.targ_curr_frame=tk.Frame(self.targ_frame)
        self.targ_curr_frame.place(relx=.3,rely=.175,relwidth=.7,relheight=.25)

                # Container
        self.targ_curr_container=tk.Label(self.targ_curr_frame,image=self.rounded_red)
        self.targ_curr_container.place(relwidth=1,relheight=1)

                    # Target Entry field
        self.targ_curr_input=tk.StringVar()
        self.targ_curr_entry=tk.Entry(self.targ_curr_container,borderwidth=0,highlightthickness=0,**self.widget_preset(App.white,App.gray),textvariable=self.targ_curr_input)
        self.targ_curr_entry.place(relwidth=1,relheight=1)
       
                    # Placeholder
        self.targ_curr_entry.insert(0,"USD,CAD..")
        
                    # Event
        self.targ_curr_entry.bind("<FocusIn>",self.targ_rm_curr)

                # Symbol
        self.targ_curr_symbol=tk.Label(self.targ_frame,**self.widget_preset(App.bg_color,App.red))
        self.targ_curr_symbol.place(relx=.09,rely=.57)

        self.targ_curr_input.trace_add("write",self.targ_on_curr_input)
        
                # Frame Currency
        self.targ_amount_frame=tk.Frame(self.targ_frame)
        self.targ_amount_frame.place(relx=.3,rely=.5,relwidth=.5,relheight=.25)
        
                    # Img widget
        self.targ_amount_container=tk.Label(self.targ_amount_frame,image=self.rounded_gray)
        self.targ_amount_container.place(relwidth=1,relheight=1)

                        # Converted amount
        self.targ_amount_value=tk.StringVar()
        
        self.targ_amount_entry=tk.Entry(self.targ_amount_container,**self.widget_preset(App.white,App.white),state="readonly",readonlybackground=App.dark_red,textvariable=self.targ_amount_value)
        self.targ_amount_entry.place(relwidth=1,relheight=1)

                    # Trace 
        self.base_amount_input.trace_add("write",self.base_on_amount_input)
        
                # "Back" frame
        self.targ_back_frame=tk.Frame(self.targ_frame)

                # "Next" frame
        self.targ_next_frame=tk.Frame(self.targ_frame)

        # Map frame
        self.map_frame=tk.Frame(self)
        self.map_frame.place(relx=.153,rely=.44,relwidth=.696,relheight=.553)
        
        self.map=tk.Label(self.map_frame,image=self.map_img)
        self.map.place(relwidth=1,relheight=1)
        
        # MISC (References)
            # Only the frames, which I think destroys the children as well (?). 
            # They are only created because I want to see the  layout of the GUI from the code.
        self.buttons=[self.targ_back_frame,self.targ_next_frame]
            
        self.valid_entries=self.flags.keys()
        
        self.base_currency=""
        self.base_amount=""

        self.targ_currencies=[]
            # For the buttons on the right-side. We want it to not reset when a new entry has been added, 
            # hence it's removed from the targ_on_curr_input()
        self.index=0

        self.latest={}
        self.mod_rates={}

    def widget_preset(self,bg='white',fg='white',font=('Tahoma',16)):
        preset = {'bg':bg,'fg':fg,'font':font}
        return preset

    def resize(self,directory,width,height):
        base=Image.open(directory)
        resize=base.resize((width,height))
        photoimg=ImageTk.PhotoImage(resize)
        return photoimg
    
    # 3 of the same operations done in separate functions. 
    # This is because we can only reference the function, so we can't input any argument at all.
    def base_rm_curr(self,event):
        self.base_curr_entry.configure(fg=App.black)
        self.base_curr_entry.delete(0,tk.END)
        self.base_curr_entry.unbind("<FocusIn>")
        
    def base_rm_amount(self,event):
        self.base_amount_entry.configure(fg=App.black)
        self.base_amount_entry.delete(0,tk.END)
        self.base_amount_entry.unbind("<FocusIn>")
    def targ_rm_curr(self,event):
        self.targ_curr_entry.configure(fg=App.black)
        self.targ_curr_entry.delete(0,tk.END)
        self.targ_curr_entry.unbind("<FocusIn>")

    def get_latest(self):
        # Call the latest values
        self.latest=App.client.latest()
        print(self.latest["data"])
        if self.base_amount:
            self.base_on_amount_input()

        messagebox.showinfo("Success!","Obtained latest currency data!")
        messagebox.showinfo("Info", f"Available Currencies: {[key for key in self.flags.keys()]}")

    def base_on_curr_input(self,*args):
        # Get the input and turn into uppercase
        self.base_currency=self.base_curr_input.get().upper()

        # If the obtained string is a key-pair,
        if self.base_currency in self.valid_entries:
            # set the flag of the valid,
            self.base_upd_guis()
        else:
            # if not valid, change it to UNK (unknown)
            self.base_upd_guis(0)

            # and if "latest" has been pressed and an amount is input, update the table with 0 values, and update the converted amounts
            if self.latest and self.base_amount_input:
                self.update_table(0)
                self.targ_change_curr_amount()

        self.base_on_amount_input()

    
    def base_upd_guis(self,success=1):
        if success:
            self.base_flag.configure(image=self.flags[self.base_currency])
            self.base_curr_symbol.configure(text=self.symbols[self.base_currency])
            return
        
        self.base_flag.configure(image=self.flags["UNK"])
        self.base_curr_symbol.configure(text=self.symbols["UNK"])

    def update_table(self,success=1):
            if self.latest:
                if success:
                    self.mod_rates=mod_rates(self.latest,self.base_currency,self.base_amount)
                else:
                    
                    self.mod_rates=mod_rates(self.latest,"USD",0)

    def base_on_amount_input(self,*args):
        # Obtain string
        self.base_amount=self.base_amount_input.get()

        # Check to see if the input string is only numbers
        if self.base_amount.isnumeric():
            # Turn the string into a number
            self.base_amount=int(self.base_amount)
            # If the base currency is valid and "latest" button has been pressed,
            if self.base_currency in self.valid_entries and self.latest:
                # Update table in success mode (using input amount)
                self.update_table()
        else:
            # If it's not all numbers, all values will be 0
            self.update_table(0)
        
        # Regardless how the table is updated, update the currencies
        self.targ_change_curr_amount()
        
    def targ_change_curr_amount(self):
        if self.targ_currencies and self.mod_rates:
            self.targ_amount_value.set(self.mod_rates[self.targ_currencies[self.index]])
            
    def targ_on_curr_input(self,*args):
        # Get the string, turn into all uppercase, then split into a list,
        # but only include those who are valid.
        self.targ_currencies=[i for i in self.targ_curr_input.get().upper().split(",") if i in self.valid_entries]
        
        # In the case of the length fluctuating inbetween writing,
            # if there is a valid currency, regardless of length,
        if self.targ_currencies:
                # check if the index is greater or equal than last positional index,
            if self.index>=len(self.targ_currencies)-1:
                    # reduce the index to the last positional.
                if self.index>0:
                    self.index=len(self.targ_currencies)-1
                    
        # Remove the buttons if the input has 1 in length or 0
        if len(self.buttons)==0 or 1:
                if len(self.buttons)>0:
                    self.destroy_buttons()

        # If we have 2+ valid currencies,
        if len(self.targ_currencies)>1:
            # In the case of our index not being the last positional,
            if self.index!=len(self.targ_currencies)-1:
                # create a "next" button, but only if it hasn't been created before
                if self.targ_next_frame not in self.buttons:
                    self.create_next_button()

            # In the case of our index not being the first positional,
            if self.index!=0:
                # create a "back" button, but only if there isn't one already
                if self.targ_back_frame not in self.buttons:
                    self.create_back_button()
        
        # Update the flags. Only after the index operations are done.
            # Default flag if no valid currency is entered.
        if not self.targ_currencies:
            self.targ_flag.configure(image=self.flags["UNK"])
            self.targ_curr_symbol.configure(text=self.symbols["UNK"])
            return
        
        # Flag if a value is entered, using index (default 0)
        self.targ_upd_guis()


    def destroy_buttons(self):
        for i in self.buttons:
            i.destroy()
        self.buttons.clear()

    def next_curr(self):
        # Function will only work if our index is less than the positional last. 
        # Example: In a 3-len list, this button will only work if our index is 1 (1<3-1). 2 is the last positional index. It cannot work there.
        if self.index<len(self.targ_currencies)-1:
            self.index+=1
            # Update the GUIs with the new index value
            self.targ_upd_guis()

            # If the new index is the last, destroy this button widget, and remove its reference from the list.
            if self.index+1==len(self.targ_currencies):
                self.targ_next_frame.destroy()
                self.buttons.remove(self.targ_next_frame)

            # Create a "back" button if we are in index 1+.
            if self.index!=0 and self.targ_back_frame not in self.buttons:
                self.create_back_button()
    
    def back_curr(self):
        # This function will only work if the index is a non-zero number.
        if self.index>0:
            # Reduce the index.
            self.index-=1
            self.targ_upd_guis()

            # If the new index is the first, destroy this button widget, and remove its reference from the list
            if self.index==0:
                self.targ_back_frame.destroy()
                self.buttons.remove(self.targ_back_frame)

            # If the new index isn't the last positional,  
            if self.index!=len(self.targ_currencies)-1 and self.targ_next_frame not in self.buttons:
                # create a "next" button, only if it hasn't been created before.
                self.create_next_button()

    def targ_upd_guis(self):
        # Change flag and symbol.
        self.targ_flag.configure(image=self.flags[self.targ_currencies[self.index]])
        self.targ_curr_symbol.configure(text=self.symbols[self.targ_currencies[self.index]])

        # If possible, change converted amount as well.
        if self.latest:
            self.targ_change_curr_amount()

    def create_next_button(self):
                        # "Next" frame
        self.targ_next_frame=tk.Frame(self.targ_frame)
        self.targ_next_frame.place(relx=.65,rely=.775,relwidth=.15,relheight=.15)
                    # "Next" container
        self.targ_next_container=tk.Label(self.targ_next_frame,image=self.rounded_small_gray)
        self.targ_next_container.place(relwidth=1,relheight=1)
                        # Next button + ">" string
        self.targ_next_button=tk.Button(self.targ_next_container,text=">",**self.widget_preset(App.gray,App.white),border=0,activebackground=App.white,command=self.next_curr)
        self.targ_next_button.place(relwidth=1,relheight=1)

        self.buttons.append(self.targ_next_frame)

    def create_back_button(self):
                # "Back" frame
        self.targ_back_frame=tk.Frame(self.targ_frame)
        self.targ_back_frame.place(relx=.3,rely=.775,relwidth=.15,relheight=.15)
                    # "Back" container
        self.targ_back_container=tk.Label(self.targ_back_frame,image=self.rounded_small_gray)
        self.targ_back_container.place(relwidth=1,relheight=1)
                        # Back button + "<" string
        self.targ_back_button=tk.Button(self.targ_back_container,text="<",**self.widget_preset(App.gray,App.white,("Tahoma",16)),border=0,activebackground=App.white,command=self.back_curr)
        self.targ_back_button.place(relwidth=1,relheight=1)

        self.buttons.append(self.targ_back_frame)

if __name__ =='__main__':
    App().mainloop()
