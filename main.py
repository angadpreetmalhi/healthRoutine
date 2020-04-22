from flask import Flask

app = Flask(__name__)

@app.route('/')
def source():   
      # Health management: This app will keep tracing of exercise and diet
        def getdate():
            import datetime
            return datetime.datetime.now()
        def lock():
            """ this function allow users to save data for daily workout
            and their diet
            """
            clientName=input("Enter Client's name")
            dietOrExercise = int(input("For diet Press 1 "
                                     "or For exercise Press 2"))
            if dietOrExercise==1:

                with open(clientName+"Diet","a") as clientData:
                    dietData = (input("Please enter Your diet\n")).capitalize()
                    clientData.write("["+str(getdate())+"] " + dietData+"\n")
            elif dietOrExercise==2:
                with open(clientName+"Ex","a") as clientData:
                    exerciseData = input("Please enter Your workout\n").capitalize()
                    clientData.write("["+str(getdate())+"]" + exerciseData+"\n")

        def findData():
            """
            this function allow users to keep track of their workout and
            diet
            :return:
            """
            clientName = input("Enter Client's name")
            dietOrExercise = int(input("For diet Press 1 "
                                       "or For exercise Press 2"))
            if dietOrExercise == 1:
                try:
                    readFile= open(clientName + "Diet")
                    print(readFile.read())
                    readFile.close()
                except:
                    readFile = open(clientName + "Diet","a")
                    readFile.close()
                    readFile = open(clientName + "Diet")
                    print(readFile.read())
                    readFile.close()
            elif dietOrExercise == 2:
                try:
                    readFile= open(clientName + "Ex")
                    print(readFile.read())
                    readFile.close()
                except:
                    readFile = open(clientName + "Ex","a")
                    readFile.close()
                    readFile = open(clientName + "Ex")
                    print(readFile.read())
                    readFile.close()
        readWrite =int(input("Please enter 1 for Lock "
                             "and 2 for retrieve"))
        if readWrite==1:
            lock()
        else:
            findData()
