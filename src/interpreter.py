# This is the main function that is called when the program is run. It is a loop that will continue to run until the user types "exit".
# The user will be prompted to enter a command, and then the command will be executed. If the user enters an invalid command, the program will
# tell the user that the command is invalid.
# The user can also "use" a module, which is a file that contains a function. This function can be executed by the user by entering the command "run".
# If the user enters the command "show all", the program will list all of the available modules that the user can use.
# If the user enters the command "show options", the program will display the options available for the module that the user is currently using.
# If the user enters the command "set target", the program will set the target for the module that the user is currently using.
# The command "set command" can be used to set the command that will be executed by the "exploits.command_exec" module.
# The user can also set the command that will be executed by the "scanners.open_ports" module by entering the command "set port".
# If the user enters the command "run", the program will execute the function that is contained within the module that the user is currently using.
# If the user enters the command "exit", the program will exit.

import os

def reppConsole():
    # The name of the current module
    module = "repp"
    # The target IP address
    target = ""
    # The command to be executed
    command = ""
    while True:
        # Get the command from the user
        command = input(module + " $ ")
        # If the user wants to use an exploit
        if command == "use exploit":
            # Get the name of the exploit from the user
            exploit = "exploits." + input()
            # Import the exploit
            exec("import " + exploit)
            # Change the name of the current module
            module = exploit
        # If the user wants to use a scanner
        elif command == "use scanner":
            # Get the name of the scanner from the user
            scanner = "scanners." + input()
            # Import the scanner
            exec("import " + scanner)
            # Change the name of the current module
            module = scanner
        # If the user wants to see all of the exploits and scanners
        elif command == "show all":
            # Print all of the exploits
            for exploit in os.listdir("exploits"):
                if exploit == "__pycache__":
                    continue
                print(exploit)
            # Print all of the scanners
            for scanner in os.listdir("scanners"):
                if scanner == "__pycache__":
                    continue
                print(scanner)
        # If the user wants to see the options for the current module
        elif command == "show options" and module != "repp":
            # Print the options for the current module
            print("Target....................Target IP Address for payload")
        # If the user wants to set the target
        elif command == "set target" and module != "repp":
            # Get the target from the user
            target = input()
        # If the user wants to run the password disclosure exploit
        elif command == "run" and module == "exploits.password_disclosure":
            # Execute the exploit
            exec(module + ".exploit(" + "\"" + target + "\"" + ")")
        # If the user wants to run the open ports scanner
        elif command == "run" and module == "scanners.open_ports":
            # Execute the scanner
            exec(module + ".scanForOpenPorts(" + "\"" + target + "\"" + ")")
        # If the user wants to run the command execution exploit
        elif command == "run" and module == "exploits.command_exec":
            # Execute the exploit
            exec(module + ".executeCommand(" + "\"" + target + "\"" + ")")
        elif command == "run" and module == "exploits.pasde.pasde_command_exec":
            exec(module + ".executeCommand(" + "\"" + target + "\"" + " \"" + command + "\"" + ")")
        # If the user enters an invalid command
        else:
            # Print an error message
            print("Command not found")
