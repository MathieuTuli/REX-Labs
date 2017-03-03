#partial credit to (github user) colinoflynn @ https://github.com/colinoflynn/dp832-gui/blob/master/dp832gui/dp832.py
#in your command prompt, type "pip install -U pyvisa"
#then just run this python script

import visa

class DP832(object):

    def __init__(self):
        pass

    def conn(self, constr="USB0::0x1AB1::0x0E11::DPXXXXXXXXXXX::INSTR"):
        """Attempt to connect to instrument"""
        rm = visa.ResourceManager()
        self.inst = rm.open_resource(constr)

    def identify(self):
        """Return identify string which has serial number"""
        return self.inst.query("*IDN?")

    def set(self):
        print("\nSetting Parameters: \nCH1 (30V/3A)\nCH2 (30V/3A)\nCH3 (5V/3A)\n")
        while True:
            channel=input("Channel? (CH?): ")
            if channel.upper()!="CH1" and channel.upper()!="CH2" and channel.upper()!="CH3": continue
            break
        while True:
            voltage=float(input("Voltage?: "))
            if voltage<0.0 or voltage>32.0: continue
            break
        while True:
            current=float(input("Current?: "))
            if current <0.0 or current>3.2: continue
            break
        self.inst.write(":APPL " +channel.upper()+","+str(voltage)+","+str(current))
        
    def readings(self):
        print("Current settings for CH1: ")
        temp=self.inst.query(":MEAS? CH1")
        print("    Voltage (V): "+temp,end="")
        temp=self.inst.query(":MEAS:CURR? CH1")
        print("    Current (A): "+temp,end="")
        temp=self.inst.query(":MEAS:POWE? CH1")
        print("    Power (W):"+temp,end="")

        print("Current settings for CH2: ")
        temp=self.inst.query(":MEAS? CH2")
        print("    Voltage (V): "+temp,end="")
        temp=self.inst.query(":MEAS:CURR? CH2")
        print("    Current (A): "+temp,end="")
        temp=self.inst.query(":MEAS:POWE? CH2")
        print("    Power (W):"+temp,end="")

        print("Current settings for CH3: ")
        temp=self.inst.query(":MEAS? CH3")
        print("    Voltage (V): "+temp,end="")
        temp=self.inst.query(":MEAS:CURR? CH3")
        print("    Current (A): "+temp,end="")
        temp=self.inst.query(":MEAS:POWE? CH3")
        print("    Power (W):"+temp,end="")
        
    def output(self):
        while True:
            channel=input("Channel? (CH?): ")
            if channel.upper()!="CH1" and channel.upper()!="CH2" and channel.upper()!="CH3": continue
            break
        while True:
            output=input("On/Off?: ")
            if output.lower()!="on" and output.lower()!="off": continue
            break
        self.inst.write(":OUTP " +channel.upper()+","+output.upper())

    def dis(self):
        del self.inst

    def writing(self, command=""):
        self.inst.write(command)

if __name__ == '__main__':
    test = DP832()
    #Insert your serial number here / confirm via Ultra Sigma GUI
    test.conn("USB0::0x1AB1::0x0E11::DP8C182402078::INSTR")
    while True:
        print("\nType \"end\" to stop")
        choice=input("Settings? (\"set\") \nReadings? (\"read\") \nTurn Channel On/Off? (\"output\")\n:")
        if choice=="read":test.readings()
        elif choice=="set":test.set()
        elif choice=="output":test.output()
        elif choice=="end": break
  
