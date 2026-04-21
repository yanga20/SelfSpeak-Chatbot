# **SelfSpeak Chatbot**



### **Project Description**



##### SelfSpeak Chatbot is a secure AI voice chatbot that generates intelligent answers using a Large Language Model and converts those answers into speech.

##### The project allows users to interact with AI in a more natural voice-based way instead of only reading text responses.



### **Table of Contents**



##### 1\. Project Description

##### 2\. Features

##### 3\. Installation

##### 4\. How to Run

##### 5\. How to Use

##### 6\. Technologies Used

##### 7\. Limitations

##### 8\. Future Scope





### **Features**



1. ##### &#x20;AI-generated responses using LLM
2. ##### &#x20;Voice output using text-to-speech
3. ##### &#x20;Password authentication
4. ##### &#x20;Personalized startup voice sample
5. ##### &#x20;Local execution for privacy
6. ##### &#x20;Expandable for future voice cloning





### **Installation**



* ##### Install required Python libraries:

##### 

* ##### pip install -r requirements.txt

##### 

* ##### Install Ollama and pull the model (ollama pull phi)



### **How to Run the Project**

1. Open terminal and move to the project folder
cd SelfSpeak-chatbot
   ---
2. Install required libraries
pip install -r requirements.txt
   ---
3. Start the local AI model
 ollama run phi
   ---
4. ##### Run the chatbot

##### &#x20;   python selfspeak.py

### 

### **How to Use the Project**



##### 1\. Start the program

##### 2\. Enter the project password

##### 3\. A personal voice sample is played at startup

##### 4\. Type your question

##### 5\. AI generates answer

##### 6\. Chatbot speaks the answer aloud

##### 

##### Type: exit to close the chatbot.



### &#x20;**Technologies Used**



##### \- Python

##### \- Ollama

##### \- Phi language model

##### \- Edge-TTS

##### \- Requests library

##### \- Local REST API

##### \- GitHub



### **Limitations**

##### 

##### The current system can generate speech but cannot fully clone the user's exact voice because advanced voice cloning requires larger AI models and stronger hardware resources.





### Future Scope



##### \* Real voice cloning

##### \* Microphone input

##### \* Better UI

##### \* Cloud deployment

##### \* Stronger security

