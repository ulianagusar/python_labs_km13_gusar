format_tuple = ('Liverpool', 845.15, 21, 134, 358.45, 'price')
el0=format_tuple[0]
el1=round(format_tuple[1])
el2=format_tuple[2]
el3=str(format_tuple[3]).zfill(4)
el4=round((format_tuple[4]),1)
el5=format_tuple[5]
format_string = "The initial lot {5} of ${4} at the {0} auction exceeded the expected {5} by {2}%,but the lot with number {3} was nevertheless sold for ${1}"
print(format_string.format(el0,el1,el2,el3,el4,el5))