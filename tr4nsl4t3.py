import sys
import argparse
from googletrans import Translator

# Banner
banner2 = """
######## ########  ##        ##    ##  ######  ##       ##        ########  #######  ########  
   ##    ##     ## ##    ##  ###   ## ##    ## ##       ##    ##     ##    ##     ## ##     ## 
   ##    ##     ## ##    ##  ####  ## ##       ##       ##    ##     ##           ## ##     ## 
   ##    ########  ##    ##  ## ## ##  ######  ##       ##    ##     ##     #######  ########  
   ##    ##   ##   ######### ##  ####       ## ##       #########    ##           ## ##   ##   
   ##    ##    ##        ##  ##   ### ##    ## ##             ##     ##    ##     ## ##    ##  
   ##    ##     ##       ##  ##    ##  ######  ########       ##     ##     #######  ##     ## 

By Bl4dsc4n - V.1.0
"""



def translate_text(text, dest_lang='pt'):
    translator = Translator()
    translation = translator.translate(text, src='auto', dest=dest_lang)
    return translation.text

def main():
    parser = argparse.ArgumentParser(description="Translate text to Portuguese.")
    parser.add_argument("text", nargs="?", help="Text to translate")
    parser.add_argument("-d", "--dest-lang", default="pt", help="Destination language for translation")
    args = parser.parse_args()

    if args.text:
        translated_text = translate_text(args.text, args.dest_lang)
        print(translated_text)
    else:
        print(banner2)
        banner = """Usage examples:
    To translate text provided as an argument:
        python script.py "hello" -d fr

    To translate text provided as standard input:
        echo "hello" | python script.py -d es

    To translate from standard input with default destination language (Portuguese):
        python script.py < lista.txt

    To specify the destination language when using standard input:
        python script.py -d de < lista.txt

    To translate to the default destination language (Portuguese):
        python script.py "hello"

    To translate to a specific language:
        python script.py "hello" -d ja
        """
        print(banner)

if __name__ == "__main__":
    main()
