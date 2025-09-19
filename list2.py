# # list.
languages = ["js", "python", "go", "java"]

copyLang = languages.copy()

languages.append("TOC") # to add data
languages.insert(2, "flutter") # to add data in certain length
languages.remove("java") # to remove data
languages.sort() # to soritng data
languages.reverse() # to reverse
languages.pop() # to remove last item


print(copyLang) # to insert or copy from one obj

languages.clear() # to clear data

print(languages)