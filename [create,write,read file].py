# We create text file with write (w) mode
f = open("trying.txt", "w")
# After created file some texts has been written
f.write("apple\nbanana\ncherry\nfig")
# And file closed in order not to let file keep memory in PC
f.close()

# In order not to make process file we opened it below in read (r) mode
f = open("trying.txt", "r")
print(f.read())
f.close()
