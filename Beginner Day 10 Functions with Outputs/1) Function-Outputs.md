# Functions with Outputs

     def format_name(f_name, l_name):
         print(f_name.title())
         print(l_name.title())
     format_name("Jeffrey", "JEFFREY")



     def format_name(f_name, l_name):
         formated_f_name = f_name.title()
         formated_l_name = l_name.title()
         print(f"{formated_f_name} {formated_l_name}")
     format_name("jEffReY", "JEFFREY")



     def format_name(f_name, l_name):
         formated_f_name = f_name.title()
         formated_l_name = l_name.title()
         return f"{formated_f_name} {formated_l_name}"
     formated_string = format_name("jEffReY", "JEFFREY")
     print(formated_string)



    def format_name(f_name, l_name):
        formated_f_name = f_name.title()
        formated_l_name = l_name.title()
        return f"{formated_f_name} {formated_l_name}"
    print(format_name("jEffReY", "JEFFREY"))





## Multiple return statements

     def format_name(f_name, l_name):
         #If user enters nothing, bypass return statement
         #return will end the function
         if f_name == "" or l_name == "":
             return "\nNo valid input provided."
         formated_f_name = f_name.title()
         formated_l_name = l_name.title()
         return f"\nYour name is: {formated_f_name} {formated_l_name}"

     print(format_name(input("What is your first name? "), input("What is your last name? ")))
