import pickle

def main():
    fin = open("level.dat","wb")
    levels = {
    "2": """
###########
#   P   B #
# H  B B  #
###       #
  #  P #P #
  #########""",
    "1": """
     #####
    ##   ##
  ### B B ###
 ##   # #   ##
##           ##
# B#  PPP #B  #
#     PHP     #
#  B# PPP  #B #
##           ##
 ##   # #   ##
  ### B B ###
    ##   ##
     #####""",
    "3": """
####################
#           P      #
#                  #
#     ###          #
#    B###       B###
#     ###         P#
#        B         #
#                  #
#####    H         #
#P                 #
#                  #
#                  #
####################"""
    }
    pickle.dump(levels,fin)
    fin.close()

if __name__ == "__main__":
    main()
