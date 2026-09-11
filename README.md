## Simple Traditional Chatbot Project Prototype

### Introduction

A conventional chat bot reacts to users' queries by adhering to a set of rigid rules without applying any sophisticated artificial intelligence. The project showcases the creation of a basic chatbot application using Python and the Microsoft Bot Framework. The implementation includes multiple user prompts, pre-defined responses, and invalid input handling. The final prototype offers insights for further improvement of the chatbot.

### Development Environment Setup

An Anaconda environment was set up to isolate the project and prevent dependency issues. This decision was made for compatibility with the Microsoft Bot Framework, with Python version 3.8.2 being chosen. Isolated allowed for easier package management and ensured a consistent development environment. This environment was created by running the following command:

conda create -n MSAI631_MBF python=3.8.2

### Installing Project Dependencies

Once the environment has been activated, all of the necessary python libraries were installed from the requirements.txt file. The dependency file lists all the packages that are necessary to run the chatbot application. All packages were installed together to save in configuration effort and to keep compatibility. The installation was completed by the following command:

pip install -r requirements.txt

### Installing the Bot Framework Emulator

The chatbot was tested using the Microsoft Bot Framework Emulator that was installed to test the bot without deploying it to Azure. The emulator offers a user-friendly interface for sending messages to the chatbot and displaying its replies. Local testing also can help find connection problems and response errors when developing. This makes debugging easier prior to deployment.

### Running the Chatbot

Environment configuration and dependency installation were done and after that, the chatbot application was started. The application was run, and the local web server and chatbot services were started. When the chatbot was successful, it was ready to receive requests from the Bot Framework Emulator. The chatbot was launched using the following command:

python app.py

### Connecting to the Emulator

The local endpoint address was used to connect the bot to the chatbot via the Microsoft Bot Framework Emulator. Clicking to Open Bot and entering the proper endpoint was successful. It receives messages from the user and passes them on to the chatbot for processing. The following endpoint was used:

http://localhost:3978/api/messages

### Chatbot Testing

Once the connection was made, different user messages were conveyed to verify the functionality of the chatbot. Chatbot was able to respond to pre-defined messages, greetings and incorrect requests from a user. The conversation logs were useful to see each request and response, and any debugging was easy. The testing was successful and it was confirmed that the chatbot worked as expected.

### Project Features

The chatbot can use rule-based responses for greeting messages, predefined questions, and requests for capabilities. Date, time, help, and farewell commands were also added to for user interaction. Unrecognized inputs will respond with a default answer to direct the user to valid commands. Additional conversation rules can be easily added, thanks to the modular structure.

### Challenges Encountered

Dependency conflicts were reported if Python versions not supported in the environment were used to configure the environment. There were also cases of connection failure due to wrong endpoint configuration in the Bot Framework Emulator. The following were working with Python 3.8.2 and the right endpoint /api/messages. Further testing led to the fine-tuning of responses by the chatbots and enhanced handling of conversations.

### Knowledge Gained

The project gave hands-on experience in Python, Microsoft Bot Framework and Chatbot Development. The dependency isolation and version compatibility was shown through the use of environment management with Anaconda. Local testing made the debugging and validation process simpler before moving to the cloud. The process of developing a rule-based chatbot also helped gain insight into the conversation flow design.

### Conclusion

The project was a success, providing a full pipeline of a classic chatbot implementation with Python and the Microsoft Bot Framework. The configuration of the environment, installation of dependencies, running the chatbot and local testing were all completed successfully. Chatbot can execute variety of pre-defined interactions and offers consistent responses based on the rules. Because of the implementation, there are good grounds for further improvements and intelligent chatbot extensions in the future.
