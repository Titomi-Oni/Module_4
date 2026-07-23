#Class 1
class Japan():
    def captial(self):
        print ("Tokyo is the captial of Japan.")

    def language(self):
        print ("Japanese is the most widely spoken language of Japan.")

    def type(self):
        print ("Japan is a developed country.")


#Class 2
class Canada():
    def captial(self):
        print ("Ottawa is the capital of Canada.")

    def language(self):
        print ("English is the most widely spoken language of Canada.")

    def type(self):
        print ("Canada is a developed country.")

obj_jpn = Japan()
obj_cad = Canada()

for country in (obj_jpn, obj_cad):
    country.captial()
    country.language()
    country.type()