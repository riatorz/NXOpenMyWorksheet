import sys
import NXOpen
import NXOpen.UF

def main(arg):
    """Takes a string argument, and shows it in a message box."""
    uf_session = NXOpen.UF.UFSession.GetUFSession()
    message = "The following arguments were passed to my journal:" + arg
    uf_session.Ui.DisplayMessage(message, 1)
    
if __name__ == '__main__':
    main(sys.argv[0])  # Somehow the arguments of the journal manager should be passed 