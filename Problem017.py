thousandlength = len("thousand")
hundredlength = len("hundred")
ninetylength = len("ninety")
eightylength = len("eighty")
seventylength = len("seventy")
sixtylength = len("sixty")
fiftylength = len("fifty")
fourtylength = len("fourty")
thirtylength = len("thirty")
twentylength = len("twenty")
ninteenlength = len("nineteen")
eighteenlength = len("eighteen")
seventeenlength = len("seventeen")
sixteenlength = len("sixteen")
fifteenlength = len("fifteen")
fourteenlength = len("fourteen")
thirteenlength = len("thirteen")
twelvelength = len("twelve")
elevenlength = len("eleven")
tenlength = len("ten")
ninelength = len("nine")
eightlength = len("eight")
sevenlength = len("seven")
sixlength = len("six")
fivelength = len("five")
fourlength = len("four")
threelength = len("three")
twolength = len("two")
onelength = len("one")

def characterCount(num):
    thousands = num % 1000
    num -= 1000*thousands
    hundreds = num % 100
    num -= 100*hundreds
    tens = num % 10
    num -= 10*tens
    
    

