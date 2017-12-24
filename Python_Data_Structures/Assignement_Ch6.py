

#6.5 Write code using find() and string slicing (see section 6.10) 
#to extract the number at the end of the line below. 
#Convert the extracted value to a floating point number and print it out.
#rstrip()
#startwith("dgdgdgdgdg") for string object
text = "X-DSPAM-Confidence:    0.8475";
text_number=text.find(" ")
print(float(text[text_number+1: len(text)]))


