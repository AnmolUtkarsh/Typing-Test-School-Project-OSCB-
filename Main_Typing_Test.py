#Typing Test Club v1.2
#Made as School Project
#Developer of this CodeBase & BiVi: Anmol Utkarsh [Ofcourse]
#Used Advanced Proprietary Scoring Engine [BiVi Typing Test API Ecosystem infused]
#Also Code Present in GITHUB [OSCB] //Open Source Code Base under MIT License: https://github.com/AnmolUtkarsh/Typing-Test-School-Project-OSCB.git
#Developed without AI except the OS Path Documentation
#Keep in mind that this Specific Code Base uses BiVi Typing Test "v1" POST API and GET API. So adjust your code according to the latest BiVi API Versions.

#CodeBase:
import requests
import time
import pandas as pd
import os

#Created by AI:
csvFile = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "test_results.csv"
)
if os.path.exists(csvFile):
    df = pd.read_csv(csvFile)
else:
    df = pd.DataFrame()
#AI Artwork ends here! 



#All Handmade + Python Documentation starts here:
print("Hi there, welcome to Typing Test Club!")

while True:
    print("Please, tell us whether you want to create a new test or find the Tests using testId?:\n1: Create New Test\n2: Find Test (Server)\n3: Find Test (Locally)\n4: Exit")

    choice = input("Enter your choice:")

    

    if choice == "1":


        language = input("Enter language(press Enter for default[English200]) : ")

        if language == "":
            language = "english"

        count = input("Enter count : ")
        if count == "":
            url = "https://bivi.online/api/typing-test/v1/" + language
        else:
            url = "https://bivi.online/api/typing-test/v1/" + language + "?count=" + count

        #response = requests.get("https://bivi.online/typing-test/v1/english)
        try:
            requ = requests.get(url)
            requ.raise_for_status()
            response = requ.json()

        except Exception as er1:
            print("Error in making request to the BiVi API Server!")
            print("Error:", er1)
            continue

        except ValueError:
            print("BiVi API returned invalid JSON!")
            continue

        testId = response[1]["test"]["id"]
        test = " ".join(response[1]["test"]["words"])
        testLang = response[1]["test"]["language"]
        testcount = response[1]["test"]["count"]


        print("\nTest created!")
        print("Test Id:", testId)
        print("Test Language:", testLang)
        print("Test Word Count:", testcount)

        #print(data)

        print("\nYou have to type:")
        print(test)

        ready = input("\nAre you ready? (yes/no): ")

        if ready.lower() == "yes":
            try:
                print("\n3")
                time.sleep(2)

                print("2")
                time.sleep(2)

                print("1")
                time.sleep(0.5)

                print("\nSTART TYPING!:")
                startTime = time.time()
                typedText = input()
                endTime = time.time()
                durationSeconds = endTime - startTime


            except:
                print("Test got Errored")
                continue

            
            df = pd.read_csv(
                    csvFile, dtype={
                        "testId": "string",
                        "testText": "string",
                        "testLanguage": "string",
                        "testCount": "Int64",
                        "typedText": "string",
                        "durationSeconds": "float64"
                    }
                )

            df.loc[df["testId"] == testId, "typedText"] = typedText
            df.loc[df["testId"] == testId, "durationSeconds"] = round(durationSeconds, 2)

            df.to_csv(csvFile, index=False)

            print("\nTest completed!")
            print("Time:", round(durationSeconds, 2), "seconds")

        else:
            print("Test cancelled.")
            continue



"""
Keep in mind that in the below given POST API request to BiVi Typing Test API. BiVi API also support things like : 
testText, typedText, durationSeconds, showDecimals, showErrors, showCharactersInfo, showWordsInfo, showAlignment, showTiming, showIntegrity

For example, I want to get the values like Raw WPM or Accuracy and others in "DECIMAL" then add:

showDecimals:true

in the BELOW response POST Request. 
Try write this in below of the "durationSeconds". For more details please see https://bivi.online/api/docs. //Upcoming!
"""


        try:
            response = requests.post("https://bivi.online/api/typing-test/v1/write-result", json={
                "testId": testId,
                "testText": test,
                "typedText": typedText,
                "durationSeconds": durationSeconds
            })
            response.raise_for_status()
        except Exception as er:
            print("POST API error:", er)
            continue

        print("Result status:", response.status_code)
        response1 = response.json()
        result = response1.get("test", response1)
        newRow = pd.DataFrame({
            "testId": [testId],
            "testLanguage": [testLang],
            "testCount": [testcount],
            "testText": [test],
            "typedText": [typedText],
            "durationSeconds": [durationSeconds],
            "WPM": [result.get("nWPM")],
            "RawWPM": [result.get("rWPM")],
            "Accuracy": [result.get("accuracy")]
        })
        # print("Result response:", response.text)
        print("WPM:", [result.get("nWPM")])
        print("Raw WPM:", [result.get("rWPM")])
        print("Accuracy:", [result.get("accuracy")])

        file = os.path.exists(csvFile) and os.path.getsize(csvFile) > 0
        newRow.to_csv(csvFile, mode="a", index=False, header=not file)

    elif choice == "2":
        testId = input("Enter Test ID: ")
        url = "https://bivi.online/api/typing-test/v1/find/" + testId
        try:
            response = requests.get(url)
            response.raise_for_status()
            print("\nResponse:")
            print(response.json())
        except Exception as er:
            print("Error retrieving test from server:", er)


    elif choice == "3":
        testId = input("Enter Test ID: ")
        df1 = pd.read_csv(csvFile)
        result = df1[df1["testId"] == testId]
        if (result.empty):
            print("Test not found locally.")
        else:
            print("\nResult:")
            print(result);


    elif choice == "4" or choice.lower() == "exit": 
        print("\nThank you for using Typing Test Club!") 
        break


    else:
        print("Invalid choice.")

#Powered by BiVi Proprietary Advance Accuracy Scoring Engine [99.724% Accuracy among other Algorithms]
