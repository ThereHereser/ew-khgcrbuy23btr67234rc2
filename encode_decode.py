class process():
    def encode(text):
        text_for_out = text.lower()
        text_for_out = text_for_out.replace("a","/1-01/")
        text_for_out = text_for_out.replace("b","/3-20/")
        text_for_out = text_for_out.replace("c","/3-31/")
        text_for_out = text_for_out.replace("d","/6-165/")
        text_for_out = text_for_out.replace("e","/4-989/")
        text_for_out = text_for_out.replace("f","/7-776/")
        text_for_out = text_for_out.replace("g","/0-312/")
        text_for_out = text_for_out.replace("h","/2-412/")
        text_for_out = text_for_out.replace("j","/4-234/")
        text_for_out = text_for_out.replace("k","/3-345/")
        text_for_out = text_for_out.replace("l","/67-123978/")
        text_for_out = text_for_out.replace("m","/452-13515/")
        text_for_out = text_for_out.replace("n","/24675-63478/")
        text_for_out = text_for_out.replace("o","/2457-978125/")
        text_for_out = text_for_out.replace("p","/2456-35678/ ")
        text_for_out = text_for_out.replace("r","/6548-3858338/")
        text_for_out = text_for_out.replace("s","/2345-249576/")
        text_for_out = text_for_out.replace("t","/564-523453726/")
        text_for_out = text_for_out.replace("u","/24675-63478/")
        text_for_out = text_for_out.replace("v","/2457-978125/")
        text_for_out = text_for_out.replace("y","/2456-35678/")
        text_for_out = text_for_out.replace("z","/6548-3858338/")
        text_for_out = text_for_out.replace(".","/31-3113/")
        text_for_out = text_for_out.replace("@","/89-238734/")
        text_for_out = text_for_out.replace("#","/276-5284328/")
        text_for_out = text_for_out.replace("$","/534-239746/")
        text_for_out = text_for_out.replace("?","/453-243578723/")
        return(text_for_out)
    
    def decode(text):
        text_for_out = text.lower()
        text_for_out = text_for_out.replace("/1-01/","a")
        text_for_out = text_for_out.replace("/3-20/","b")
        text_for_out = text_for_out.replace("/3-31/","c")
        text_for_out = text_for_out.replace("/6-165/","d")
        text_for_out = text_for_out.replace("/4-989/","e")
        text_for_out = text_for_out.replace("/7-776/","f")
        text_for_out = text_for_out.replace("/0-312/","g")
        text_for_out = text_for_out.replace("/2-412/","h")
        text_for_out = text_for_out.replace("/4-234/","j")
        text_for_out = text_for_out.replace("/3-345/","k")
        text_for_out = text_for_out.replace("/67-123978/","l")
        text_for_out = text_for_out.replace("/452-13515/","m")
        text_for_out = text_for_out.replace("/24675-63478/","n")
        text_for_out = text_for_out.replace("/2457-978125/","o")
        text_for_out = text_for_out.replace("/2456-35678/ ","p")
        text_for_out = text_for_out.replace("/6548-3858338/","r")
        text_for_out = text_for_out.replace("/2345-249576/","s")
        text_for_out = text_for_out.replace("/564-523453726/","t")
        text_for_out = text_for_out.replace("/24675-63478/","u")
        text_for_out = text_for_out.replace("/2457-978125/","v")
        text_for_out = text_for_out.replace("/2456-35678/","y")
        text_for_out = text_for_out.replace("/6548-3858338/","z")
        text_for_out = text_for_out.replace("/31-3113/",".")
        text_for_out = text_for_out.replace("/89-238734/","@")
        text_for_out = text_for_out.replace("/276-5284328/","#")
        text_for_out = text_for_out.replace("/534-239746/","$")
        text_for_out = text_for_out.replace("/453-243578723/","?")
        return(text_for_out)